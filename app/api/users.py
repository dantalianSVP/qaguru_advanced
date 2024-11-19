from datetime import datetime
from http import HTTPStatus
from typing import Iterable
from fastapi import HTTPException, status
from app.api.routes import routes
from app.serializers.user import CreateUserResponseModel, UserBaseSchema, UpdateUserResponseModel, \
    UserUpdate
from app.db import users


@routes.post(
    '/users',
    response_model=CreateUserResponseModel,
    status_code=HTTPStatus.CREATED,
    summary='Создание нового пользователя'

)
async def create_user(user_data: UserBaseSchema):
    UserBaseSchema.model_validate(user_data)
    user_id = users.create_user(user_data)
    return CreateUserResponseModel(message="Пользователь успешно зарегистрирован", id=user_id.id)


@routes.put(
    '/users/{user_id}',
    response_model=UpdateUserResponseModel,
    status_code=200,
    summary='Изменение данных пользователя'

)
async def update_user(user_id: int, user_data: UserUpdate):
    if user_id < 1:
        raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail='Invalid user_id')
    UserUpdate.model_validate(user_data)
    user = users.get_user(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Пользователь не найден в БД',
        )
    users.update_user(user_id, user_data)
    return UpdateUserResponseModel(updatedAt=str(datetime.now()))


@routes.delete(
    '/users/{user_id}',
    status_code=204,
    summary='Удаление пользователя пользователя'

)
async def delete_user(user_id: int):
    if user_id < 1:
        raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail='Invalid user_id')
    user = users.get_user(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Пользователь не найден в БД',
        )
    return users.delete_user(user_id)


@routes.get(
    '/users/{user_id}',
    response_model=UserBaseSchema,
    status_code=200,
    summary='Получение данных пользователя'

)
async def get_user(user_id: int):
    if user_id < 1:
        raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail='Invalid user_id')
    user = users.get_user(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Пользователь не найден в БД',
        )
    return user


@routes.get("/users", status_code=HTTPStatus.OK)
async def get_users() -> Iterable[UserBaseSchema]:
    return users.get_users()
