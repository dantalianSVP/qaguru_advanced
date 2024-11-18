from http import HTTPStatus

from api.routes import routes
from db.engine import check_availability
from serializers.status import AppStatus


@routes.get('/status', status_code=HTTPStatus.OK)
async def status():
    return AppStatus(database=check_availability())
