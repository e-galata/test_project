from .sql_messages_enum import ErrorMessages
from sqlalchemy import exists

class BaseSQLTest:
    """Базовый класс для всех SQL-тестов"""
    
    def __init__(self, db_session):
        self.db_session = db_session

    def assert_user_count(self, table, expected):
        """Проверяет количество пользователей в БД"""
        actual = self.db_session.query(table).count()
        assert actual == expected, ErrorMessages.COUNT_MISMATCH.value.format(expected=expected, actual=actual)
    
    def assert_value_exists(self, table, column, value):
        """Проверяет наличие email в БД"""
        table_column_find_value = getattr(table, column)
        value_exists = self.db_session.query(exists().where(table_column_find_value == value)).scalar()
        assert value_exists, ErrorMessages.VALUE_NOT_FOUND.value.format(value=value, column=column, table=table.__tablename__)    

    def create_and_verify_user(self, table, name, email):
        """Создаёт пользователя и проверяет его сохранение"""
        new_user = table(name=name, email=email)
        self.db_session.add(new_user)
        self.db_session.commit()
        
        db_user = self.db_session.query(table).filter_by(email=email).first()
        assert db_user.email == email, ErrorMessages.EMAIL_NOT_FOUND.value.format(email=email)
