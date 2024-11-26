import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routes import routes
from app.db.engine import create_db_and_table


@asynccontextmanager
async def lifespan(app:FastAPI):
    logging.warning("On start")
    create_db_and_table()
    yield
    logging.warning("On stop")



def create_app():
    app = FastAPI(title='Service for QA.GURU',lifespan=lifespan)
    app.include_router(routes, prefix='/v1/api', tags=['v1'])
    return app
