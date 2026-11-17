import pytest
from main import BooksCollector
import books_and_genre

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

    def test_set_genre_books(self):
        collector = BooksCollector()
        collector.add_new_book('Человек-паук: Враг в отражении')
        collector.set_book_genre('Человек-паук: Враг в отражении', 'Фантастика')        
        assert collector.books_genre['Человек-паук: Враг в отражении'] == 'Фантастика'
    

    
    def test_get_book_genre(self, collector_name_books_with_genre):
        collector = BooksCollector()
        collector.add_new_book(books_and_genre.kashtan)
        collector.get_book_genre(books_and_genre.genre_detectiv)        
        assert collector_name_books_with_genre.get_book_genre(books_and_genre.kashtan) == books_and_genre.genre_detectiv

    def test_get_books_with_specific_genre(self, collector_name_books_with_genre):        
        assert collector_name_books_with_genre.get_books_with_specific_genre(books_and_genre.genre_horror) == [books_and_genre.zombi, books_and_genre.annabel]

    def test_get_books_genre(self):
        collector = BooksCollector()        
        collector.add_new_book(books_and_genre.spider_man)
        collector.set_book_genre(books_and_genre.spider_man, books_and_genre.genre_fantastic)
        
        assert collector.get_books_genre()

    def test_get_books_for_children(self, collector_name_books_with_genre):        
        assert books_and_genre.kashtan not in collector_name_books_with_genre.get_books_for_children()
        assert collector_name_books_with_genre.get_books_for_children() == [books_and_genre.spider_man, books_and_genre.traktor]
    
    def test_add_book_in_favorites(self,collector_with_favorites):
        collector_with_favorites.add_book_in_favorites(books_and_genre.spider_man)        
        assert books_and_genre.spider_man in collector_with_favorites.books_genre
        assert books_and_genre.spider_man in collector_with_favorites.favorites

    def test_dublicat_add_book_in_favorites(self, collector_name_books_with_genre):
        collector_name_books_with_genre.add_book_in_favorites(books_and_genre.spider_man)
        collector_name_books_with_genre.add_book_in_favorites(books_and_genre.spider_man)
        assert len(collector_name_books_with_genre.favorites) == 1

    def test_delete_book_from_favorites(self, collector_with_favorites):
        collector_with_favorites.delete_book_from_favorites(books_and_genre.zombi)        
        assert books_and_genre.zombi not in collector_with_favorites.favorites

    def test_get_list_of_favorites_books(self, collector_with_favorites): 
        assert collector_with_favorites.get_list_of_favorites_books()
        