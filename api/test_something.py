import pytest
from jsonschema_get import GET_LIST_USER_SCHEMA
from basetestclasses import Response
from pydantic_schema_get import Get_List_Users, Get_List_Users_User

def test_get_list_users(get_list_users):
    (
        Response(get_list_users)
        .assert_status_code(200)
        .validate_by_jsonschema(GET_LIST_USER_SCHEMA)
        .validate_by_pydantic(Get_List_Users)
    )

@pytest.mark.random_user
def test_get_single_user(get_single_user):
    r, data_block, json_data = get_single_user
    (
        Response(r, json_data)
        .assert_status_code(200)
        .validate_by_jsonschema(data_block)
        .validate_by_pydantic(Get_List_Users_User)
    )
