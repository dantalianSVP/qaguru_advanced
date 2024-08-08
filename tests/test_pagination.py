import httpx
import pytest

from serializers.pagination import PaginatedResponse


def test_base_pagination(app_url):
    response = httpx.get(f"{app_url}/users")
    resp = response.json()
    PaginatedResponse(**resp)


def test_count_value_in_repsonse(app_url):
    response = httpx.get(f"{app_url}/users")
    all_items = response.json()["items"]
    count_items = len(all_items)
    assert count_items == 19


@pytest.mark.parametrize('test_input, expected ', [(3, 3), (5, 5)])
def test_pagination_size(app_url, test_input, expected):
    response = httpx.get(f"{app_url}/users?page=1&size={test_input}")
    all_items = response.json()["items"]
    count_items = len(all_items)
    assert count_items == expected
