from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

from clients.files.files_client import File
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client
from clients.users.private_users_client import User


class Course(TypedDict):
    id: str
    title: str
    maxScore: int
    minScore: int
    description: str
    previewFile: File
    estimatedTime: str
    createdByUser: User

class CreateCourseResponseDict(TypedDict):
    course: Course

class GetCoursesQueryDict(TypedDict):
    userId: str

class CreateCourseRequestDict(TypedDict):
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId: str

class UpdateCourseRequestDict(TypedDict):
    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None

class CoursesClient(APIClient):
    def get_courses_api(self, query: GetCoursesQueryDict) -> Response:
        return self.get('/api/v1/courses',params=query)

    def get_course_api(self,course_id: str) -> Response:
        return self.get(f'/api/v1/courses/{course_id}')

    def create_course_api(self, request: CreateCourseRequestDict) -> Response:
        return self.post('/api/v1/courses', json=request)

    def update_course_api(self, course_id: str, request:UpdateCourseRequestDict) -> Response:
        return self.patch(f'/api/v1/courses/{course_id}', json=request)

    def delete_course_api(self,course_id: str) -> Response:
        return self.delete(f'/api/v1/courses/{course_id}')

    def create_course(self,request: CreateCourseRequestDict) -> CreateCourseResponseDict:
        response = self.create_course_api(request)
        return response.json()

def get_courses_client(user: AuthenticationUserDict) -> CoursesClient:
    return CoursesClient(client=get_private_http_client(user))
