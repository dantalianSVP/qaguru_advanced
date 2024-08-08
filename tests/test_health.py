from http import HTTPStatus

import httpx


def test_health_check(app_url: str):
    """Проверяем, готов ли сервер к тестированию."""
    response = httpx.get(f"{app_url}/status")
    assert response.status_code == HTTPStatus.OK
