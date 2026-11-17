import pytest
from main import BooksCollector
import books_and_genre

@pytest.fixture
def collector_name_books_with_genre():
    collector = BooksCollector()
    collector.add_new_book(books_and_genre.spider_man)
    collector.set_book_genre(books_and_genre.spider_man, books_and_genre.genre_fantastic)
    collector.add_new_book(books_and_genre.traktor)
    collector.set_book_genre(books_and_genre.traktor, books_and_genre.genre_cartoon)
    collector.add_new_book(books_and_genre.zombi)
    collector.set_book_genre(books_and_genre.zombi, books_and_genre.genre_horror)
    collector.add_new_book(books_and_genre.annabel)
    collector.set_book_genre(books_and_genre.annabel, books_and_genre.genre_horror)
    collector.add_new_book(books_and_genre.kashtan)
    collector.set_book_genre(books_and_genre.kashtan, books_and_genre.genre_detectiv)
    return collector

@pytest.fixture
def collector_with_favorites(collector_name_books_with_genre):
    collector_name_books_with_genre.add_book_in_favorites(books_and_genre.annabel)
    collector_name_books_with_genre.add_book_in_favorites(books_and_genre.zombi)
    return collector_name_books_with_genre