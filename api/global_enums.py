from enum import Enum

class GlobalErrorMessages(Enum):
    WRONG_ELEMENTS_COUNT = "Unexpected number of elements counted"
    WRONG_STATUS_CODE = "Received status code is not equal to expected."
