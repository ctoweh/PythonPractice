class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.available = True

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Available: {'Yes' if self.available else 'No'}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            for book in self.books:
                print(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.available:
                    book.available = False
                    print(f"Successfully borrowed '{title}'.")
                else:
                    print(f"'{title}' is not available for borrowing.")
                return
        print(f"'{title}' not found in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if not book.available:
                    book.available = True
                    print(f"Successfully returned '{title}'.")
                else:
                    print(f"'{title}' is already available in the library.")
                return
        print(f"'{title}' not found in the library.")


# Example usage:
if __name__ == "__main__":
    library = Library()

    book1 = Book("Python Programming", "John Smith", "Programming")
    book2 = Book("Data Science Essentials", "Jane Doe", "Data Science")
    book3 = Book("Introduction to Algorithms", "Thomas Cormen", "Computer Science")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    library.display_books()

    library.borrow_book("Python Programming")
    library.borrow_book("Data Science Essentials")
    library.borrow_book("Introduction to Algorithms")

    library.return_book("Python Programming")
    library.return_book("Data Science Essentials")

    library.display_books()
