import logging
from contextlib import asynccontextmanager


import uvicorn
from fastapi import FastAPI
from fastapi_pagination import add_pagination

from app.api.routes import routes
from app.db.engine import create_db_and_table


@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.warning("On start")
    create_db_and_table()
    yield
    logging.warning("On stop")


def create_app():
    app = FastAPI(title='Service for QA.GURU', lifespan=lifespan)
    app.include_router(routes, prefix='/v1/api', tags=['v1'])
    return app

app = create_app()

add_pagination(app)

if __name__ == '__main__':
    create_db_and_table()
    uvicorn.run('main:app', port=5001, log_level='debug')

