import pytest
import requests
import random
from configuration import BASE_URL, GET_LIST_USERS
from jsonschema_get import GET_LIST_USER_SCHEMA

@pytest.fixture
def get_list_users():
    response = requests.get(url=BASE_URL+GET_LIST_USERS)
    return response

@pytest.fixture
def get_single_user():
    r = requests.get(url=BASE_URL+GET_LIST_USERS+'/'+str(random.randint(1,12)))
    json_data = 'data'
    data_block = {"data": GET_LIST_USER_SCHEMA['properties'][json_data]}
    return r, data_block, json_data
