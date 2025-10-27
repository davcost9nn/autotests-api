from httpx import Response
from typing import TypedDict

from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


class Exercise(TypedDict):
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class GetExercisesQueryDict(TypedDict):
    courseId: str

class GetExercisesResponseDict(TypedDict):
    exercises: list[Exercise]

class CreateExerciseResponseDict(TypedDict):
    exercises: list[Exercise]

class UpdateExerciseResponseDict(TypedDict):
    exercises: list[Exercise]

class CreateExerciseRequestDict(TypedDict):
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class UpdateExerciseRequestDict(TypedDict):
    title: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class ExercisesClient(APIClient):
    def get_exercises_api(self,query: GetExercisesQueryDict) -> Response:
        return self.get('/api/v1/exercises',params=query)

    def get_exercise_api(self,exercise_id: str) -> Response:
        return self.get(f'/api/v1/exercises/{exercise_id}')

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        return self.post('/api/v1/exercises', json=request)

    def update_exercise_api(self,exercise_id: str, request:UpdateExerciseRequestDict) -> Response:
        return self.patch(f'/api/v1/exercises/{exercise_id}', json=request)

    def delete_exercise_api(self,exercise_id: str) -> Response:
        return self.delete(f'/api/v1/exercises/{exercise_id}')


    def get_exercises(self,query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        response = self.get_exercises_api(query)
        return response.json()

    def get_exercise(self,exercise_id: str) -> GetExercisesResponseDict:
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def create_exercise(self,request: CreateExerciseRequestDict) -> CreateExerciseResponseDict:
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise(self, exercise_id: str, request:UpdateExerciseRequestDict) -> UpdateExerciseResponseDict:
        response = self.update_exercise_api(exercise_id,request)
        return response.json()

def get_exercise_client(user: AuthenticationUserDict) -> ExercisesClient:
    return ExercisesClient(client=get_private_http_client(user))