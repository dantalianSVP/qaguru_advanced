import os
from http import HTTPStatus

import dotenv
import httpx
import pytest


@pytest.fixture(autouse=True, scope="session")
def envs():
    dotenv.load_dotenv()


@pytest.fixture(scope="session")
def app_url():
    return os.getenv("APP_URL")


@pytest.fixture
def users(app_url):
    response = httpx.get(f"{app_url}/api/users/")
    assert response.status_code == HTTPStatus.OK
    return response.json()
