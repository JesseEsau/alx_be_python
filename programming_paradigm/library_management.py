class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def list_available_books(self):
        for book in self._books:
            if book._is_checked_out == False:
                print(f"{book.title} {book.author}")

    def check_out_book(self, title):
        self.title = title
        for book in self._books:
            if book.title == self.title:
                book._is_checked_out = True

    def return_book(self, title):
        self.book = title
        for book in self._books:
            if book.title == self.title:
                book._is_checked_out = False
