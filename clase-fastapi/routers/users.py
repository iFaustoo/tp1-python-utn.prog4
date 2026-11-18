from fastapi import APIRouter, HTTPException, Query, status
from models.users import (
    User,
    UserUpdate,
    GetUsersResponse,
    CreateUserResponse,
    DeleteUserResponse,
)

router = APIRouter()

usuarios: list[User] = [
    User(id=1, name="juan perez"),
    User(id=2, name="pepe sanchez"),
]


@router.get("/user")
def get_users(
    is_active: bool | None = Query(default=None)
) -> GetUsersResponse:
    if is_active is None:
        users = usuarios
    else:
        users = [user for user in usuarios if user.is_active == is_active]
    return GetUsersResponse(users=users)


@router.put("/user/{user_id}")
def update_user(user_id: int, user_update: UserUpdate) -> User:
    for index, user in enumerate(usuarios):
        if user.id == user_id:
            updated_user = User(id=user_id, **user_update.model_dump())
            usuarios[index] = updated_user
            return updated_user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Usuario no encontrado",
    )


@router.delete("/user/{id}")
def delete_user(id: int) -> DeleteUserResponse:
    for user in usuarios:
        if user.id == id:
            usuarios.remove(user)
            return DeleteUserResponse(message="Usuario eliminado")

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Usuario no encontrado",
    )


@router.post("/user")
def create_user(user: User) -> CreateUserResponse:
    if any(existing_user.id == user.id for existing_user in usuarios):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Ya existe un usuario con ese id",
        )
    usuarios.append(user)
    return CreateUserResponse(message="Usuario creado")
