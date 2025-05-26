import csv
import os

class BookNotFoundException(Exception): pass
class BookAlreadyBorrowedException(Exception): pass
class MemberLimitExceededException(Exception): pass

class Book:
    def __init__(self, title, is_borrowed=False):
        self.title = title
        self.is_borrowed = is_borrowed

    def to_row(self):
        return [self.title, str(self.is_borrowed)]

class Member:
    def __init__(self, name, borrowed_books=None):
        self.name = name
        self.borrowed_books = borrowed_books if borrowed_books else []

    def to_row(self):
        return [self.name, ",".join(self.borrowed_books)]

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.load_data()

    def load_data(self):
        if os.path.exists("books.csv"):
            with open("books.csv", newline='') as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) >= 2:
                        title = row[0]
                        is_borrowed = row[1] == "True"
                        self.books.append(Book(title, is_borrowed))

        if os.path.exists("members.csv"):
            with open("members.csv", newline='') as f:
                reader = csv.reader(f)
                for row in reader:
                    name = row[0]
                    borrowed = row[1].split(",") if len(row) > 1 and row[1] else []
                    self.members.append(Member(name, borrowed))


    def save_data(self):
        with open("books.csv", "w", newline='') as f:
            writer = csv.writer(f)
            for book in self.books:
                writer.writerow(book.to_row())

        with open("members.csv", "w", newline='') as f:
            writer = csv.writer(f)
            for member in self.members:
                writer.writerow(member.to_row())

    def add_book(self, title):
        self.books.append(Book(title))
        self.save_data()
        print(f"Book '{title}' added.")

    def add_member(self, name):
        self.members.append(Member(name))
        self.save_data()
        print(f"Member '{name}' added.")

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundException(f"Book '{title}' not found.")

    def find_member(self, name):
        for member in self.members:
            if member.name == name:
                return member
        raise Exception(f"Member '{name}' not found.")

    def borrow_book(self, member_name, book_title):
        member = self.find_member(member_name)
        book = self.find_book(book_title)

        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"'{book_title}' is already borrowed.")
        if len(member.borrowed_books) >= 3:
            raise MemberLimitExceededException(f"{member_name} has reached the limit.")

        book.is_borrowed = True
        member.borrowed_books.append(book_title)
        self.save_data()
        print(f"{member_name} borrowed '{book_title}'.")

    def return_book(self, member_name, book_title):
        member = self.find_member(member_name)
        book = self.find_book(book_title)

        if book_title in member.borrowed_books:
            member.borrowed_books.remove(book_title)
            book.is_borrowed = False
            self.save_data()
            print(f"{member_name} returned '{book_title}'.")
        else:
            print(f"{member_name} didn't borrow '{book_title}'.")

def menu():
    lib = Library()

    while True:
        print("\nLibrary Menu")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                title = input("Enter book title: ")
                lib.add_book(title)
            elif choice == "2":
                name = input("Enter member name: ")
                lib.add_member(name)
            elif choice == "3":
                name = input("Enter member name: ")
                title = input("Enter book title: ")
                lib.borrow_book(name, title)
            elif choice == "4":
                name = input("Enter member name: ")
                title = input("Enter book title: ")
                lib.return_book(name, title)
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid option.")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    menu()
