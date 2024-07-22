from api.routes import routes
from serializers.user import CreateUserRequestModel, CreateUserResponseModel, UserBaseSchema
from utils.core import save_user_to_json, get_user_data_by_id


@routes.post(
    '/users',
    response_model=CreateUserResponseModel,
    status_code=200,
    summary='Создание нового пользователя'

)
async def create_user(user_data: CreateUserRequestModel):
    user_id = save_user_to_json(user_data)
    return CreateUserResponseModel(message="Пользователь успешно зарегистрирован", id=user_id)


@routes.get(
    '/users/{user_id}',
    response_model=UserBaseSchema,
    status_code=200,
    summary='Получение данных пользователя'

)
async def get_user(user_id: int):
    return get_user_data_by_id(user_id)
