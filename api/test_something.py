import pytest
from configuration import BASE_URL, GET_LIST_USERS
from jsonschema_get import GET_LIST_USER_SCHEMA
from basetestclasses import Response
from pydantic_schema_get import Get_List_Users, Get_List_Users_User, Get_List_User_Data

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
        Response(request_get_api(BASE_URL, GET_LIST_USERS, get_single_user_random(1,12)), 'data')
        .assert_status_code(200)
        .validate_by_jsonschema(get_schema_from_data(GET_LIST_USER_SCHEMA, 'properties', 'data'))
        .validate_by_pydantic(Get_List_Users_User)
    )


def base_user_check(base_url, endpoint, user, status_code, schema, request_get_api):
    (
        Response(request_get_api(base_url, endpoint, user))
        .assert_status_code(status_code)
        .validate_by_pydantic(schema)
    )

@pytest.mark.parametrize(
    "base_url, endpoint, user, status_code, schema",
    [
        (
            BASE_URL,
            GET_LIST_USERS,
            2,
            200,
            Get_List_User_Data
        ),
        (
            BASE_URL,
            GET_LIST_USERS,
            None,
            200,
            Get_List_Users
        )
    ]
)
def test_all(base_url, endpoint, user, status_code, schema, request_get_api):
    base_user_check(base_url, endpoint, user, status_code, schema, request_get_api)
