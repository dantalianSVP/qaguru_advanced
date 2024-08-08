import json
import uvicorn
from main import create_app
from serializers.user import UserBaseSchema

app = create_app()

users: list[UserBaseSchema]

if __name__ == '__main__':
    with open("db/users.json") as f:
        users = json.load(f)
    for user in users:
        UserBaseSchema.model_validate(user)
    uvicorn.run('asgi:app', port=5001, log_level='debug')
