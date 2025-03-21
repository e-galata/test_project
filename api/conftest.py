import pytest
import requests
import random

def _request_get_api(BASE_URL, GET_LIST_USERS, user=None):
    if user is not None:
        GET_LIST_USERS += f'/{user}'
    return requests.get(url=BASE_URL+GET_LIST_USERS)

@pytest.fixture
def request_get_api():
    return _request_get_api

def _get_single_user_random(id_from, id_to):
    return random.randint(id_from, id_to)

@pytest.fixture
def get_single_user_random():
    return _get_single_user_random

def _get_schema_from_data(schema, pathto, data):
    return {"data": schema[pathto][data]}

@pytest.fixture
def get_schema_from_data():
    return _get_schema_from_data
