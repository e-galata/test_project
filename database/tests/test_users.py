import pytest
from database.baseclasses import BaseSQLTest
from database.models import User

@pytest.mark.parametrize("table, expected", [
    (User, 2)
])
def test_user_count(db_session, table, expected):
    """Проверяем, что тестовые данные добавились"""
    BaseSQLTest(db_session).assert_user_count(table, expected)

@pytest.mark.parametrize("table, column, value", [
    (User, "email", "alice@example.com"),
    (User, "email", "bob@test.org")
])
def test_find_row_value(db_session, table, column, value):
    """
    Проверяем существует ли значения для поля
    Передаем сессию (соединение с бд), таблицу, колонну, значение
    """
    BaseSQLTest(db_session).assert_value_exists(table, column, value)


@pytest.mark.parametrize("table, name, email", [
    (User, "John", "john@doe.com"),
    (User, "Jane", "jane@doe.org")
])
def test_add_new_user(db_session, table, name, email):
    """
    Создаем пользователя в таблице users, с name, email
    проверяем по email есть ли этот пользователь в базе
    """
    BaseSQLTest(db_session).create_and_verify_user(table, name, email)
