from datetime import datetime

from fastapi import HTTPException, status

from api.routes import routes
from serializers.user import CreateUserRequestModel, CreateUserResponseModel, UserBaseSchema, UpdateUserResponseModel
from db.db_queries import add_user, get_user_by_id, update_user_by_id, delete_user_by_id


@routes.post(
    '/users',
    response_model=CreateUserResponseModel,
    status_code=200,
    summary='Создание нового пользователя'

)
async def create_user(user_data: CreateUserRequestModel):
    user_id = add_user(user_data)
    return CreateUserResponseModel(message="Пользователь успешно зарегистрирован", id=user_id)


@routes.get(
    '/users/{user_id}',
    response_model=UserBaseSchema,
    status_code=200,
    summary='Получение данных пользователя'

)
async def get_user(user_id: int):
    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Пользователь не найден в БД',
        )
    return get_user_by_id(user_id)


@routes.put(
    '/users/{user_id}',
    response_model=UpdateUserResponseModel,
    status_code=200,
    summary='Изменение данных пользователя'

)
async def update_user(user_id: int, user_data: UserBaseSchema):
    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Пользователь не найден в БД',
        )
    update_user_by_id(user_id, user_data)
    return UpdateUserResponseModel(updatedAt=str(datetime.now()))


@routes.delete(
    '/users/{user_id}',
    status_code=204,
    summary='Удаление пользователя пользователя'

)
async def delete_user(user_id: int):
    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Пользователь не найден в БД',
        )
    return delete_user_by_id(user_id)
