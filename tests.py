import pytest
from main import BooksCollector

class TestBooksCollector:
    
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')        
        assert len(collector.books_genre) == 2
        
    @pytest.mark.parametrize('book_name, append_true', [('a'*40, True), ('a'*41, False)])
        
    def test_add_new_book_string_length(self, book_name, append_true):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert (book_name in collector.books_genre) == append_true

    def test_add_new_book_dublicate(self):
        collector = BooksCollector()
        collector.add_new_book('Человек-паук: Враг в отражении')
        collector.add_new_book('Человек-паук: Враг в отражении')        
        assert len(collector.books_genre) ==  1

    def test_install_genre_books(self):
        collector = BooksCollector()
        collector.add_new_book('Человек-паук: Враг в отражении')
        collector.set_book_genre('Человек-паук: Враг в отражении', 'Фантастика')        
        assert collector.books_genre['Человек-паук: Враг в отражении'] == 'Фантастика'
    
    @pytest.fixture
    def collector_name_books_with_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Человек-паук: Враг в отражении')
        collector.set_book_genre('Человек-паук: Враг в отражении', 'Фантастика')
        collector.add_new_book('Приключение синего трактора')
        collector.set_book_genre('Приключение синего трактора', 'Мультфильмы')
        collector.add_new_book('Зомби')
        collector.set_book_genre('Зомби', 'Ужасы')
        collector.add_new_book('Аннабель')
        collector.set_book_genre('Аннабель', 'Ужасы')
        collector.add_new_book('Виктор - Каштан')
        collector.set_book_genre('Виктор - Каштан', 'Детективы')
        return collector
    
    def test_get_book_genre(self, collector_name_books_with_genre):        
        assert collector_name_books_with_genre.get_book_genre('Виктор - Каштан') == 'Детективы'

    def test_get_books_with_specific_genre(self, collector_name_books_with_genre):        
        assert collector_name_books_with_genre.get_books_with_specific_genre('Ужасы') == ['Зомби', 'Аннабель']

    def test_get_books_genre(self, collector_name_books_with_genre):        
        assert collector_name_books_with_genre.get_books_genre()

    def test_get_books_for_children(self, collector_name_books_with_genre):        
        assert 'Виктор - Каштан' not in collector_name_books_with_genre.get_books_for_children()
        assert collector_name_books_with_genre.get_books_for_children() == ['Человек-паук: Враг в отражении', 'Приключение синего трактора']


    @pytest.fixture
    def collector_with_favorites(self, collector_name_books_with_genre):
        collector_name_books_with_genre.add_book_in_favorites('Аннабель')
        collector_name_books_with_genre.add_book_in_favorites('Зомби')
        return collector_name_books_with_genre
    

    def test_add_book_in_favorites(self,collector_with_favorites):
        collector_with_favorites.add_book_in_favorites('Человек-паук: Враг в отражении')        
        assert 'Человек-паук: Враг в отражении' in collector_with_favorites.books_genre
        assert 'Человек-паук: Враг в отражении' in collector_with_favorites.favorites

    def test_dublicat_add_book_in_favorites(self, collector_name_books_with_genre):
        collector_name_books_with_genre.add_book_in_favorites('Человек-паук: Враг в отражении')
        collector_name_books_with_genre.add_book_in_favorites('Человек-паук: Враг в отражении')
        assert len(collector_name_books_with_genre.favorites) == 1

    def test_delete_book_from_favorites(self, collector_with_favorites):
        collector_with_favorites.delete_book_from_favorites('Зомби')        
        assert 'Зомби' not in collector_with_favorites.favorites

    def test_get_list_of_favorites_books(self, collector_with_favorites):        
        assert 'Аннабель' in collector_with_favorites.favorites
        