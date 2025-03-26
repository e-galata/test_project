import pytest
from database.db_manager import DatabaseManager

@pytest.fixture(scope="module")
def db_manager():
    """Фикстура для инициализации БД (выполняется 1 раз за тест-сессию)"""
    manager = DatabaseManager("sqlite:///:memory:")
    manager.create_tables()
    manager.add_test_data()
    yield manager
    # Автоматический cleanup (БД в памяти удалится сама)

@pytest.fixture
def db_session(db_manager):
    """Фикстура для работы с сессией (откатывает изменения после теста)"""
    session = db_manager.get_session()
    yield session
    session.rollback()
    session.close()
