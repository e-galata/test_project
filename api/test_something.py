import requests
from configuration import BASE_URL, GET_LIST_USERS
from jsonschema_get import GET_LIST_USER_SCHEMA
from basetestclasses import Response
from pydantic_schema_get import Get_List_Users

def test_get_list_users():
    r = requests.get(url=BASE_URL+GET_LIST_USERS)
    response = Response(r)
    response.assert_status_code(200).validate_by_jsonschema(GET_LIST_USER_SCHEMA).validate_by_pydantic(Get_List_Users)
