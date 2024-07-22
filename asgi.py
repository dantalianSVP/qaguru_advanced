import uvicorn
from main import create_app

app = create_app()

if __name__ == '__main__':
    uvicorn.run('asgi:app', port=5000, log_level='debug')
