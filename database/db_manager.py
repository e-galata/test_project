from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, User

class DatabaseManager:
    def __init__(self, connection_string="sqlite:///:memory:"):
        self.engine = create_engine(connection_string)
        self.Session = sessionmaker(bind=self.engine)
        
    def create_tables(self):
        """Создаёт все таблицы в БД"""
        Base.metadata.create_all(self.engine)
        
    def get_session(self):
        """Возвращает новую сессию для работы с БД"""
        return self.Session()
    
    def add_test_data(self):
        """Наполняет БД тестовыми данными"""
        session = self.get_session()
        try:
            session.add_all([
                User(name="Alice", email="alice@example.com"),
                User(name="Bob", email="bob@test.org")
            ])
            session.commit()
        finally:
            session.close()
