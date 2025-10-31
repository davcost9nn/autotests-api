from clients.api_client import APIClient
from httpx import Response
from clients.courses.courses_schema import GetCoursesQuerySchema, CreateCourseRequestSchema, UpdateCourseRequestSchema, \
    CreateCourseResponseSchema
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema





class CoursesClient(APIClient):
    def get_courses_api(self, query: GetCoursesQuerySchema) -> Response:
        return self.get('/api/v1/courses',params=query)

    def get_course_api(self,course_id: str) -> Response:
        return self.get(f'/api/v1/courses/{course_id}')

    def create_course_api(self, request: CreateCourseRequestSchema) -> Response:
        return self.post('/api/v1/courses', json=request)

    def update_course_api(self, course_id: str, request:UpdateCourseRequestSchema) -> Response:
        return self.patch(f'/api/v1/courses/{course_id}', json=request)

    def delete_course_api(self,course_id: str) -> Response:
        return self.delete(f'/api/v1/courses/{course_id}')

    def create_course(self, request: CreateCourseRequestSchema) -> CreateCourseResponseSchema:
        # Преобразуем с использованием алиасов (camelCase)
        request_data = request.model_dump(by_alias=True)
        response = self.create_course_api(request_data)
        return CreateCourseResponseSchema.model_validate_json(response.text)

def get_courses_client(user: AuthenticationUserSchema) -> CoursesClient:
    return CoursesClient(client=get_private_http_client(user))
