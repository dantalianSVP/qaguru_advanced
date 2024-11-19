from http import HTTPStatus

from app.api.routes import routes
from app.db.engine import check_availability
from app.serializers.status import AppStatus


@routes.get('/status', status_code=HTTPStatus.OK)
async def status():
    return AppStatus(database=check_availability())
