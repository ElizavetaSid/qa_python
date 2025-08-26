import pytest
from main import BooksCollector

@pytest.fixture
def collector(self):
        #Фикстура для создания экземпляра BooksCollector
    return BooksCollector()