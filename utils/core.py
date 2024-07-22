import json
import os
from functools import wraps

from serializers.user import CreateUserRequestModel

DATA_FILE = 'db/users.json'


def file_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'w', encoding='utf-8') as f:
                json.dump({}, f)  # Создаем пустой файл, если его нет
        with open(DATA_FILE, 'r+', encoding='utf-8') as f:
            users = json.load(f)
            result = func(users, *args, **kwargs)
            f.seek(0)  # Возвращаемся в начало файла
            f.truncate()  # Очищаем файл
            json.dump(users, f, ensure_ascii=False, indent=4)
            return result

    return wrapper

