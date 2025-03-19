import requests
from jsonschema import validate
from global_enums import GlobalErrorMessages
from configuration import BASE_URL, GET_LIST_USERS
from schema_get import GET_LIST_USER_SCHEMA

def test_get_list_users():
    response = requests.get(url=BASE_URL+GET_LIST_USERS)
    received_post = response.json()
    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert len(received_post) == 6, GlobalErrorMessages.WRONG_ELEMENTS_COUNT.value
    validate(received_post, GET_LIST_USER_SCHEMA)
