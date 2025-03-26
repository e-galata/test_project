from enum import Enum

class ErrorMessages(Enum):
    """Шаблоны сообщений об ошибках для тестов"""
    COUNT_MISMATCH = "Expected {expected} users, got {actual}"
    VALUE_NOT_FOUND = "Value '{value}' not found in column '{column}' table '{table}'"
    EMAIL_NOT_FOUND = "Email with '{email}' not found"
