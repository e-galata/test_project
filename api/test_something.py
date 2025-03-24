import pytest
from configuration import BASE_URL, GET_LIST_USERS, POST_CREATE_USER
from json_schema import GET_LIST_USER_SCHEMA
from basetestclasses import Response
from pydantic_schema import Get_List_Users, Get_List_Users_User, Get_List_User_Data, Post_Create_User
from generators import User 

def test_get_list_users(request_get_api):
    """
    In that test we try to get list of user, 
    validate json by schema, check the status code
    """
    (
        Response(request_get_api(BASE_URL, GET_LIST_USERS))
        .assert_status_code(200)
        .validate_by_jsonschema(GET_LIST_USER_SCHEMA)
        .validate_by_pydantic(Get_List_Users)
    )

@pytest.mark.random_user
def test_get_single_user(request_get_api, get_single_user_random, get_schema_from_data):
    """
    In that test we try to get random user from users,
    validate it by json from specific data
    check the status code
    """
    (
        Response(request_get_api(BASE_URL, GET_LIST_USERS, get_single_user_random(1,12)), 'data')
        .assert_status_code(200)
        .validate_by_jsonschema(get_schema_from_data(GET_LIST_USER_SCHEMA, 'properties', 'data'))
        .validate_by_pydantic(Get_List_Users_User)
    )


def get_user_check(base_url, endpoint, user, status_code, schema, request_get_api):
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
    """
    In that test we have parametrize data, we have two test, first check specific user from users list,
    second check list of user. In parametrize we send base url, endpoint url, number of user, status code and schema for validata data.
    After that we validate response with delivered data. 
    """
    get_user_check(base_url, endpoint, user, status_code, schema, request_get_api)

@pytest.mark.parametrize( 
    "generate_user",
    [
        {},
        {'locale': 'en_US'},
        {'locale': 'ru_RU'},
        {'name': 'Peter'},
        {'job': 'QA'},
        {'locale': 'ru_RU', 'job': 'Тестировщик'}
    ],
    indirect=True
)
def test_create_user(generate_user, request_post_api):
    """
    In this test data are generate by User generator, in parametrize we send only parameters for generator
    like {} - auto generated data
    {'locale': '...'} manual only locale specified, and so on
    to API will be delivered manual, auto or mixed user data like {name: str, job: str} - Post_Create_User schema
    locale is only need to choose the language of data, by default en_US
    """
    print(generate_user)
    post_create_user_check(generate_user, request_post_api)

def post_create_user_check(generate_user, request_post_api):
    (
        Response(request_post_api(BASE_URL, POST_CREATE_USER, generate_user))
        .assert_status_code(201)
        .validate_by_pydantic(Post_Create_User)
    )
