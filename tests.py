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



from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.add_new_book('1984')
        assert len(collector.get_books_genre()) == 2

    def test_set_book_genre_valid(self):
        collector = BooksCollector()
        collector.add_new_book('Алхимик')
        collector.set_book_genre('Алхимик', 'Фантастика')
        assert collector.get_book_genre('Алхимик') == 'Фантастика'

    def test_set_book_genre_invalid(self):
        collector = BooksCollector()
        collector.add_new_book('Песнь льда и огня')
        collector.set_book_genre('Песнь льда и огня', 'Фэнтези')
        assert collector.get_book_genre('Песнь льда и огня') == ''

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Алхимик')
        collector.set_book_genre('Алхимик', 'Фантастика')
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')

        books = collector.get_books_with_specific_genre('Фантастика')
        assert books == ['Алхимик']

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Бэмби')
        collector.set_book_genre('Бэмби', 'Мультфильмы')
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')

        books_for_children = collector.get_books_for_children()
        assert 'Бэмби' in books_for_children
        assert 'Шерлок Холмс' not in books_for_children

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Алхимик')
        collector.set_book_genre('Алхимик', 'Фантастика')
        collector.add_book_in_favorites('Алхимик')
        assert 'Алхимик' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.set_book_genre('Мастер и Маргарита', 'Фантастика')
        collector.add_book_in_favorites('Мастер и Маргарита')
        collector.delete_book_from_favorites('Мастер и Маргарита')
        assert 'Мастер и Маргарита' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')
        collector.add_book_in_favorites('1984')
        favorites = collector.get_list_of_favorites_books()
        assert favorites == ['1984']

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Преступление и наказание')
        collector.set_book_genre('Преступление и наказание', 'Детективы')
        books_genre = collector.get_books_genre()
        assert books_genre == {'Преступление и наказание': 'Детективы'}

    def test_add_new_book_name_too_long(self):
        collector = BooksCollector()
        collector.add_new_book('Г' * 41)
        assert len(collector.get_books_genre()) == 0
