import allure

from clients.api_client import APIClient
from httpx import Response
from clients.courses.courses_schema import GetCoursesQuerySchema, CreateCourseRequestSchema, UpdateCourseRequestSchema, \
    CreateCourseResponseSchema
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from tools.routes import APIRoutes




class CoursesClient(APIClient):
    @allure.step("Get courses")
    def get_courses_api(self, query: GetCoursesQuerySchema) -> Response:
        return self.get(APIRoutes.COURSES, params=query.model_dump(by_alias=True))

    @allure.step("Get course by id {course_id}")
    def get_course_api(self,course_id: str) -> Response:
        return self.get(f"{APIRoutes.COURSES}/{course_id}")

    @allure.step("Create course")
    def create_course_api(self, request: CreateCourseRequestSchema) -> Response:
        return self.post(APIRoutes.COURSES, json=request.model_dump(by_alias=True))

    @allure.step("Update course by id {course_id}")
    def update_course_api(self, course_id: str, request:UpdateCourseRequestSchema) -> Response:
        return self.patch(
            f"{APIRoutes.COURSES}/{course_id}",
            json=request.model_dump(by_alias=True)
        )

    @allure.step("Delete course by id {course_id}")
    def delete_course_api(self,course_id: str) -> Response:
        return self.delete(f"{APIRoutes.COURSES}/{course_id}")


    def create_course(self, request: CreateCourseRequestSchema) -> CreateCourseResponseSchema:
        response = self.create_course_api(request)
        return CreateCourseResponseSchema.model_validate_json(response.text)

def get_courses_client(user: AuthenticationUserSchema) -> CoursesClient:
    return CoursesClient(client=get_private_http_client(user))
