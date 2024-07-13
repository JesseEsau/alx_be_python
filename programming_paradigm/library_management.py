class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out_book(self, title):
        self.title = title
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book._is_checked_out = True
            elif book.title != title or book._is_checked_out:
                print("This book is not available!")

    def return_book(self):
        for book in self._books:
            if book.title and book._is_checked_out:
                book._is_checked_out = False


class Library():
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def list_available_books(self):
        for book in self._books:
            if not book._is_checked_out:
                print(f"{book.title} {book.author}")

    def check_out_book(self, title):
        self.title = title
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book._is_checked_out = True
            elif book.title != title or book._is_checked_out:
                print("This book is not available!")

    def return_book(self, title):
        for book in self._books:
            if book.title == title and book._is_checked_out:
                book._is_checked_out = False
