import pytest

# Импортируем класс BooksCollector из соответствующего модуля
from main import BooksCollector


class TestBooksCollector:

    @pytest.mark.parametrize("book_name", [
        "The Hobbit",
        "1984",
        "To Kill a Mockingbird",
    ])
    def test_add_new_book(self, collector, book_name):
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()

    @pytest.mark.parametrize("book_name, genre", [
        ("The Hobbit", "Фантастика"),
        ("1984", "Детективы"),
        ("To Kill a Mockingbird", "Мультфильмы"),
    ])
    def test_set_book_genre(self, collector, book_name, genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    @pytest.mark.parametrize("initial_books, genre, expected_books", [
        ({"The Hobbit": "Фантастика", "1984": "Детективы"}, "Фантастика", ["The Hobbit"]),
        ({"The Hobbit": "Фантастика", "1984": "Детективы"}, "Детективы", ["1984"]),
        ({"The Hobbit": "Фантастика", "1984": "Детективы"}, "Мультфильмы", []),
    ])
    def test_get_books_with_specific_genre(self, collector, initial_books, genre, expected_books):
        collector.books_genre = initial_books
        assert collector.get_books_with_specific_genre(genre) == expected_books

    @pytest.mark.parametrize("initial_books, expected_books", [
        ({"The Hobbit": "Фантастика", "1984": "Детективы", "To Kill a Mockingbird": "Мультфильмы"}, ["The Hobbit", "To Kill a Mockingbird"]),
        ({"The Hobbit": "Фантастика", "1984": "Детективы"}, ["The Hobbit"]),
        ({"To Kill a Mockingbird": "Мультфильмы"}, ["To Kill a Mockingbird"]),
    ])
    def test_get_books_for_children(self, collector, initial_books, expected_books):
        collector.books_genre = initial_books
        assert collector.get_books_for_children() == expected_books

    @pytest.mark.parametrize("book_name", [
        "The Hobbit",
        "1984",
        "To Kill a Mockingbird",
    ])
    def test_add_book_in_favorites(self, collector, book_name):
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize("initial_favorites, book_name, expected_favorites", [
        (["The Hobbit"], "The Hobbit", []),
        (["The Hobbit", "1984"], "1984", ["The Hobbit"]),
    ])
    def test_delete_book_from_favorites(self, collector, initial_favorites, book_name, expected_favorites):
        collector.favorites = initial_favorites
        collector.delete_book_from_favorites(book_name)
        assert collector.get_list_of_favorites_books() == expected_favorites

    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book("The Hobbit")
        collector.add_book_in_favorites("The Hobbit")
        assert collector.get_list_of_favorites_books() == ["The Hobbit"]
