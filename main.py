from fastapi import FastAPI

from api.routes import routes


def create_app():
    app = FastAPI(title='Service for QA.GURU')
    app.include_router(routes, prefix='/v1/api', tags=['v1'])
    return app
