import uvicorn
from fastapi_pagination import add_pagination

from main import create_app

app = create_app()

add_pagination(app)

if __name__ == '__main__':
    uvicorn.run('asgi:app', port=5000, log_level='debug')
