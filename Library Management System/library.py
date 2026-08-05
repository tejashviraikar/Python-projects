import json
from json.tool import main
import os


# ----------------------------
# Book Class
# ----------------------------
class Book:

    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "available": self.available
        }


# ----------------------------
# Library Class
# ----------------------------
class Library:

    def __init__(self, filename="books.json"):
        self.filename = filename
        self.books = []
        self.load_books()

    # ----------------------------
    # Load Books
    # ----------------------------
    def load_books(self):

        if os.path.exists(self.filename):

            try:
                with open(self.filename, "r") as file:
                    data = json.load(file)

                    self.books = [
                        Book(
                            book["title"],
                            book["author"],
                            book["isbn"],
                            book["available"]
                        )
                        for book in data
                    ]

            except json.JSONDecodeError:
                self.books = []

        else:
            self.books = []

    # ----------------------------
    # Save Books
    # ----------------------------
    def save_books(self):

        with open(self.filename, "w") as file:

            json.dump(
                [book.to_dict() for book in self.books],
                file,
                indent=4
            )
        # ----------------------------
    # Add Book
    # ----------------------------
    def add_book(self):

        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        isbn = input("Enter ISBN: ")

        for book in self.books:
            if book.isbn == isbn:
                print("A book with this ISBN already exists.")
                return

        new_book = Book(title, author, isbn)

        self.books.append(new_book)

        self.save_books()

        print("Book added successfully!")

    # ----------------------------
    # View Books
    # ----------------------------
    def view_books(self):

        if not self.books:
            print("\nNo books available.")
            return

        print("\n========== BOOK LIST ==========")

        for index, book in enumerate(self.books, start=1):

            status = "Available" if book.available else "Issued"

            print(f"\nBook {index}")
            print(f"Title  : {book.title}")
            print(f"Author : {book.author}")
            print(f"ISBN   : {book.isbn}")
            print(f"Status : {status}")

        print("===============================")

    # ----------------------------
    # Search Book
    # ----------------------------
    def search_book(self):

        keyword = input("Enter book title or ISBN: ").lower()

        found = False

        for book in self.books:

            if keyword in book.title.lower() or keyword == book.isbn:

                status = "Available" if book.available else "Issued"

                print("\nBook Found")
                print("----------------------")
                print(f"Title  : {book.title}")
                print(f"Author : {book.author}")
                print(f"ISBN   : {book.isbn}")
                print(f"Status : {status}")

                found = True

        if not found:
            print("Book not found.")

    # ----------------------------
    # Issue Book
    # ----------------------------
    def issue_book(self):

        isbn = input("Enter ISBN of the book: ")

        for book in self.books:

            if book.isbn == isbn:

                if book.available:
                    book.available = False
                    self.save_books()
                    print("Book issued successfully!")
                else:
                    print("Book is already issued.")

                return

        print("Book not found.")

    # ----------------------------
    # Return Book
    # ----------------------------
    def return_book(self):

        isbn = input("Enter ISBN of the book: ")

        for book in self.books:

            if book.isbn == isbn:

                if not book.available:
                    book.available = True
                    self.save_books()
                    print("Book returned successfully!")
                else:
                    print("Book is already available.")

                return

        print("Book not found.")

# ----------------------------
# Display Menu
# ----------------------------
def display_menu():

    print("\n" + "=" * 40)
    print("     LIBRARY MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")
    print("=" * 40)


# ----------------------------
# Main Function
# ----------------------------
def main():

    library = Library()

    while True:

        display_menu()

        try:

            choice = int(input("Enter your choice (1-6): "))

            if choice == 1:
                library.add_book()

            elif choice == 2:
                library.view_books()

            elif choice == 3:
                library.search_book()

            elif choice == 4:
                library.issue_book()

            elif choice == 5:
                library.return_book()

            elif choice == 6:
                print("\nThank you for using Library Management System!")
                break

            else:
                print("Please select a valid option.")

        except ValueError:
            print("Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()