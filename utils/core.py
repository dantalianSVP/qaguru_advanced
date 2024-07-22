import json

from serializers.user import CreateUserRequestModel


def save_user_to_json(user_data: CreateUserRequestModel):
    # Загружаем существующих пользователей
    try:
        with open('users.json', 'r', encoding='utf-8') as json_file:
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
        'email': user_data.email
    }

    # Добавляем нового пользователя в список
    users.append(user_entry)

    # Записываем обновлённый список пользователей обратно в файл
    with open('users.json', 'w', encoding='utf-8') as json_file:
        json.dump(users, json_file, ensure_ascii=False, indent=4)

    return user_id


def get_user_data_by_id(user_id):
    with open('users.json', 'r', encoding='utf-8') as json_file:
        users = json.load(json_file)
    for i in users:
        if i['id'] == user_id:
            return i
