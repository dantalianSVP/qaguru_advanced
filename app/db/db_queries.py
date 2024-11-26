import dotenv

dotenv.load_dotenv()
import json
from datetime import datetime
from app.serializers.user import CreateUserRequestModel
from app.utils.core import file_handler


def add_user(user_data: CreateUserRequestModel):
    """:param user_data - объект данных пользователя"""
    try:
        with open('db/users.json', 'r', encoding='utf-8') as json_file:
            users = json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        users = []

    # Генерируем новый идентификатор пользователя
    user_id = len(users) + 1
    user_entry = {
        'id': user_id,
        'name': user_data.name,
        'login': user_data.login,
        'phone': user_data.phone,
        'password': user_data.password,
        'email': user_data.email,
        'createAt': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'updatedAt': ''
    }

    # Добавляем нового пользователя в список
    users.append(user_entry)

    # Записываем обновлённый список пользователей обратно в файл
    with open('db/users.json', 'w', encoding='utf-8') as json_file:
        json.dump(users, json_file, ensure_ascii=False, indent=4)

    return user_id


def get_user_by_id(user_id: int):
    with open('db/users.json', 'r', encoding='utf-8') as json_file:
        users = json.load(json_file)
    for user in users:
        if user.get('id') == user_id:
            return user


@file_handler
def update_user_by_id(users: list, user_id: int, user_data):
    # Ищем пользователя по ID
    for user in users:
        if user.get('id') == user_id:
            user.update(user_data)
            user['updatedAt'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


@file_handler
def delete_user_by_id(users: list, user_id: int):
    # Ищем пользователя по ID
    for user in users:
        if user.get('id') == user_id:
            users.remove(user)
