import uvicorn
from fastapi_pagination import add_pagination

from app.db.engine import create_db_and_table
from app.main import create_app

app = create_app()

add_pagination(app)

# if __name__ == '__main__':
#     create_db_and_table()
#     uvicorn.run('asgi:app', port=5000, log_level='debug')
