from jsonschema import validate
from global_enums import GlobalErrorMessages

class Response():
    def __init__(self, response, json_data=None):
        self.response = response
        if json_data is not None:
            self.response_json = response.json().get(json_data)
        else:
            self.response_json = response.json()
        self.response_status = response.status_code

    def validate_by_jsonschema(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                validate(item, schema)
        else:
            validate(self.response_json, schema)
        return self

    def validate_by_pydantic(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema.model_validate(item)
        else:
            schema.model_validate(self.response_json)
        return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert self.response_status == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        return self

    def __repr__(self):
        return f"\nResponse body: {self.response_json}\nRequested URL: {self.response.url}\nResponse status code {self.response_status}" 
