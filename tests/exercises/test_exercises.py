from http import HTTPStatus

import pytest

from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercise_schema import CreateExerciseResponseSchema, CreateExerciseRequestSchema, \
    GetExerciseResponseSchema, \
    UpdateExerciseRequestSchema, UpdateExerciseResponseSchema, GetExercisesResponseSchema, GetExercisesQuerySchema
from clients.exercises.exercises_client import ExercisesClient
from fixtures.courses import CourseFixture, function_course
from fixtures.exercises import ExercisesFixture
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import assert_create_exercise_response, assert_get_exercise_response, \
    assert_update_exercise_response, assert_exercise_not_found_response, assert_get_exercises_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.exercises
@pytest.mark.regression
class TestExercises:
    def test_create_exercise(self,exercises_client:ExercisesClient,function_course):
        request = CreateExerciseRequestSchema(
            course_id=function_course.response.course.id
        )
        response = exercises_client.create_exercise_api(request)
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_exercise_response(request,response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())


    def test_get_exercise(
            self,
            exercises_client:ExercisesClient,
            function_exercise:ExercisesFixture
    ):

        exercise_id = function_exercise.response.exercise.id
        response = exercises_client.get_exercise_api(exercise_id)
        response_data = GetExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_exercise_response(response_data,function_exercise.response)

        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_update_exercise(
            self,
            exercises_client: ExercisesClient,
            function_exercise: ExercisesFixture
    ):



        exercise_id = function_exercise.response.exercise.id
        request = UpdateExerciseRequestSchema()
        response = exercises_client.update_exercise_api(exercise_id=exercise_id,request=request)
        response_data = UpdateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_exercise_response(request,response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())



    def test_delete_exercise(
            self,
            exercises_client:ExercisesClient,
            function_exercise: ExercisesFixture
    ):
        exercise_id = function_exercise.response.exercise.id
        exercises_client.delete_exercise_api(exercise_id)
        response = exercises_client.get_exercise_api(exercise_id)
        response_data = InternalErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.NOT_FOUND)
        assert_exercise_not_found_response(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_get_exercises(
            self,
            exercises_client: ExercisesClient,
            function_exercise: ExercisesFixture,
            function_course: CourseFixture
    ):

        course_id = function_course.response.course.id

        query = GetExercisesQuerySchema(course_id=course_id)
        response = exercises_client.get_exercises_api(query=query)
        response_data = GetExercisesResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_exercises_response(response_data, [function_exercise.response])

        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())


