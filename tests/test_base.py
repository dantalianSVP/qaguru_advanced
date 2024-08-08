import datetime

import httpx
import pytest

from serializers.user import UserBaseSchema, CreateUserResponseModel, UpdateUserResponseModel


user_data_update = {
    'name': 'upd',
    'phone': 'upd',
    'email': 'upd',
    'login': 'upd',
    'password': 'upd',
    'updatedAt': str(datetime.datetime.now())
}

new_user = {
    'name': 'new_user',
    'phone': 'new',
    'email': 'new',
    'login': 'new',
    'password': 'new',
    'createAt': str(datetime.datetime.now())
}


def test_create_user(app_url):
    response = httpx.post(f'{app_url}/users', json=new_user)
    resp = response.json()
    CreateUserResponseModel(**resp)
    assert response.status_code == 200


@pytest.mark.parametrize("user_id", ["3", "12"])
def test_get_user(user_id,app_url):
    response = httpx.get(f'{app_url}/users' + "/" + user_id)
    resp = response.json()
    UserBaseSchema(**resp)
    assert response.status_code == 200


def test_delete_user(app_url):
    response = httpx.post(f'{app_url}/users', json=new_user)
    resp = response.json()
    user_id = resp["id"]
    response = httpx.delete(f'{app_url}/users' + "/" + str(user_id))
    assert response.status_code == 204
    response = httpx.get(url=app_url + "/" + str(user_id))
    assert response.status_code == 404


def test_update_user(app_url):
    resp = httpx.post(f'{app_url}/users', json=new_user).json()
    user_id = resp["id"]
    response = httpx.put(f'{app_url}/users' + "/" + str(user_id), json=user_data_update)
    resp = response.json()
    UpdateUserResponseModel(**resp)
    assert response.status_code == 200
