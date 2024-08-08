from http import HTTPStatus

from api.routes import routes


@routes.get('/status', status_code=HTTPStatus.OK)
async def status():
    return {"status": "available"}
