import allure
from httpx import Response
from tools.routes import APIRoutes
from clients.api_client import APIClient
from clients.exercises.exercise_schema import GetExercisesQuerySchema, CreateExerciseRequestSchema, \
    UpdateExerciseRequestSchema, GetExercisesResponseSchema, CreateExerciseResponseSchema, UpdateExerciseResponseSchema, \
    GetExerciseQuerySchema
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema




class ExercisesClient(APIClient):
    @allure.step("Get exercise")
    def get_exercises_api(self,query: GetExercisesQuerySchema) -> Response:
        return self.get(APIRoutes.EXERCISES,params=query.model_dump(by_alias=True))

    @allure.step("Get exercise by id {exercise_id}")
    def get_exercise_api(self,exercise_id: str) -> Response:
        return self.get(f'{APIRoutes.EXERCISES}/{exercise_id}')

    @allure.step("Create exercise")
    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:

        request_data = request.model_dump(by_alias=True)
        return self.post(APIRoutes.EXERCISES, json=request_data)

    @allure.step("Update exercise")
    def update_exercise_api(self,exercise_id: str, request:UpdateExerciseRequestSchema) -> Response:
        return self.patch(f'{APIRoutes.EXERCISES}/{exercise_id}', json=request.model_dump(by_alias=True))

    @allure.step("Delete exercise")
    def delete_exercise_api(self,exercise_id: str) -> Response:
        return self.delete(f'{APIRoutes.EXERCISES}/{exercise_id}')


    def get_exercises(self,query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def get_exercise(self,exercise_id: str) -> GetExercisesResponseSchema:
        response = self.get_exercise_api(exercise_id)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:

        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(self, exercise_id: str, request:UpdateExerciseRequestSchema) -> UpdateExerciseResponseSchema:
        response = self.update_exercise_api(exercise_id,request)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)

def get_exercise_client(user: AuthenticationUserSchema) -> ExercisesClient:
    return ExercisesClient(client=get_private_http_client(user))