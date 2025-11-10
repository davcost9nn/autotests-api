from httpx import Response
from clients.api_client import APIClient
from clients.exercises.exercise_schema import GetExercisesQuerySchema, CreateExerciseRequestSchema, \
    UpdateExerciseRequestSchema, GetExercisesResponseSchema, CreateExerciseResponseSchema, UpdateExerciseResponseSchema, \
    GetExerciseQuerySchema
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema




class ExercisesClient(APIClient):
    def get_exercises_api(self,query: GetExercisesQuerySchema) -> Response:
        return self.get('/api/v1/exercises',params=query.model_dump(by_alias=True))

    def get_exercise_api(self,exercise_id: str) -> Response:
        return self.get(f'/api/v1/exercises/{exercise_id}')

    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        # Преобразование только здесь
        request_data = request.model_dump(by_alias=True)
        return self.post('/api/v1/exercises', json=request_data)

    def update_exercise_api(self,exercise_id: str, request:UpdateExerciseRequestSchema) -> Response:
        return self.patch(f'/api/v1/exercises/{exercise_id}', json=request.model_dump(by_alias=True))

    def delete_exercise_api(self,exercise_id: str) -> Response:
        return self.delete(f'/api/v1/exercises/{exercise_id}')


    def get_exercises(self,query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def get_exercise(self,exercise_id: str) -> GetExercisesResponseSchema:
        response = self.get_exercise_api(exercise_id)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        # Передаем модель как есть
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(self, exercise_id: str, request:UpdateExerciseRequestSchema) -> UpdateExerciseResponseSchema:
        response = self.update_exercise_api(exercise_id,request)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)

def get_exercise_client(user: AuthenticationUserSchema) -> ExercisesClient:
    return ExercisesClient(client=get_private_http_client(user))