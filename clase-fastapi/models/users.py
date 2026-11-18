from pydantic import BaseModel
from typing import List


class User(BaseModel):
    id: int
    name: str
    is_active: bool = True


class UserUpdate(BaseModel):
    name: str
    is_active: bool


class GetUsersResponse(BaseModel):
    users: List[User]


class CreateUserResponse(BaseModel):
    message: str


class DeleteUserResponse(BaseModel):
    message: str
