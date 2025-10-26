from clients.api_client import APIClient
from httpx import  Response
from typing import TypedDict

class CreateUserRequestDict(TypedDict):
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class PublicUsersClient(APIClient):
    def create_user_api(self,request: CreateUserRequestDict) -> Response:
        return self.post('/api/v1/users',json=request)