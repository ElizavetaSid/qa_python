import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.fixture
    def collector(self):
        #Фикстура для создания экземпляра BooksCollector
        return BooksCollector()

    # Тесты для add_new_book
    def test_add_new_book_valid_name(self, collector):
        #Тест добавления книги с валидным названием
        collector.add_new_book('Война и мир')
        assert 'Война и мир' in collector.books_genre
        assert collector.books_genre['Война и мир'] == ''

    def test_add_new_book_max_length_name(self, collector):
        #Тест добавления книги с максимальной длиной названия (40 символов)
        long_name = 'A' * 40
        collector.add_new_book(long_name)
        assert long_name in collector.books_genre

    def test_add_new_book_too_long_name(self, collector):
        #Тест попытки добавления книги с слишком длинным названием
        too_long_name = 'A' * 41
        collector.add_new_book(too_long_name)
        assert too_long_name not in collector.books_genre

    # Тесты для set_book_genre
    def test_set_book_genre_valid(self, collector):
        #Тест установки валидного жанра для существующей книги
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')
        assert collector.books_genre['1984'] == 'Фантастика'

    def test_set_book_genre_nonexistent_book(self, collector):
        #Тест установки жанра для несуществующей книги
        collector.set_book_genre('Несуществующая книга', 'Фантастика')
        assert 'Несуществующая книга' not in collector.books_genre

    def test_set_book_genre_invalid_genre(self, collector):
        #Тест установки невалидного жанра
        collector.add_new_book('Мастер и Маргарита')
        collector.set_book_genre('Мастер и Маргарита', 'Несуществующий жанр')
        assert collector.books_genre['Мастер и Маргарита'] == ''


    # Тесты для get_book_genre
    def test_get_book_genre_existing_book(self, collector):
        #Тест получения жанра существующей книги
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'


    def test_get_book_genre_book_without_genre(self, collector):
        #Тест получения жанра книги без установленного жанра
        collector.add_new_book('Книга без жанра')
        assert collector.get_book_genre('Книга без жанра') is None

    # Тесты для get_books_with_specific_genre
    def test_get_books_with_specific_genre_nonexistent(self, collector):
        #Тест получения книг с несуществующим жанром
        result = collector.get_books_with_specific_genre('Несуществующий жанр')
        assert result == []

    # Тесты для get_books_genre
    def test_get_books_genre_with_books(self, collector):
        #Тест получения словаря с книгами
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.set_book_genre('Книга 1', 'Фантастика')
        
        result = collector.get_books_genre()
        assert len(result) == 2
        assert result['Книга 1'] == 'Фантастика'
        assert result['Книга 2'] == ''

    # Тесты для get_books_for_children
    def test_get_books_for_children_no_age_rating(self, collector):
        #Тест получения книг без возрастного рейтинга
        collector.add_new_book('Детская книга')
        collector.add_new_book('Взрослая книга')
        collector.set_book_genre('Детская книга', 'Мультфильмы')
        collector.set_book_genre('Взрослая книга', 'Ужасы')
        
        result = collector.get_books_for_children()
        assert result == ['Детская книга']

    # Тесты для add_book_in_favorites
    def test_add_book_in_favorites_valid(self, collector):
        #Тест добавления валидной книги в избранное
        collector.add_new_book('Любимая книга')
        collector.add_book_in_favorites('Любимая книга')
        assert 'Любимая книга' in collector.favorites

    def test_add_book_in_favorites_nonexistent_book(self, collector):
        #Тест добавления несуществующей книги в избранное
        collector.add_book_in_favorites('Несуществующая книга')
        assert 'Несуществующая книга' not in collector.favorites

    # Тесты для delete_book_from_favorites
    def test_delete_book_from_favorites_existing(self, collector):
        #Тест удаления существующей книги из избранного
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.delete_book_from_favorites('Книга')
        assert 'Книга' not in collector.favorites
    
    def test_delete_book_from_favorites_nonexistent(self, collector):
        #Тест удаления несуществующей книги из избранного
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        initial_favorites = collector.favorites.copy()
        collector.delete_book_from_favorites('Несуществующая книга')
        assert collector.favorites == initial_favorites

    # Тесты для get_list_of_favorites_books
    def test_get_list_of_favorites_books_empty(self, collector):
        #Тест получения пустого списка избранного
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_with_books(self, collector):
        #Тест получения списка избранного с книгами
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.add_book_in_favorites('Книга 1')
        collector.add_book_in_favorites('Книга 2')
        
        result = collector.get_list_of_favorites_books()
        assert len(result) == 2
        assert 'Книга 1' in result
        assert 'Книга 2' in result