import pytest
from pydantic import BaseModel

from clients.exercises.exercise_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from clients.exercises.exercises_client import get_exercise_client, ExercisesClient
from fixtures.users import UserFixture, function_user


class ExercisesFixture(BaseModel):
    request: CreateExerciseRequestSchema
    response: CreateExerciseResponseSchema


@pytest.fixture
def exercises_client(function_user: UserFixture)->ExercisesClient:
    return get_exercise_client(function_user.authentication_user)

@pytest.fixture
def function_exercise(
        exercises_client: ExercisesClient,
        function_user: UserFixture
)->ExercisesFixture:
    request = CreateExerciseRequestSchema()
    response = exercises_client.create_exercise(request)
    return ExercisesFixture(request=request,response=response)