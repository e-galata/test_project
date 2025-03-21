import pytest
from configuration import BASE_URL, GET_LIST_USERS
from jsonschema_get import GET_LIST_USER_SCHEMA
from basetestclasses import Response
from pydantic_schema_get import Get_List_Users, Get_List_Users_User

def test_get_list_users(request_get_api):
    (
        Response(request_get_api(BASE_URL, GET_LIST_USERS))
        .assert_status_code(200)
        .validate_by_jsonschema(GET_LIST_USER_SCHEMA)
        .validate_by_pydantic(Get_List_Users)
    )

@pytest.mark.random_user
def test_get_single_user(request_get_api, get_single_user_random, get_schema_from_data):
    (
        Response(request_get_api(BASE_URL, GET_LIST_USERS, user = get_single_user_random(1,12)), 'data')
        .assert_status_code(200)
        .validate_by_jsonschema(get_schema_from_data(GET_LIST_USER_SCHEMA, 'properties', 'data'))
        .validate_by_pydantic(Get_List_Users_User)
    )
