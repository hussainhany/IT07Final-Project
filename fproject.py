class Book:
    count = 0

    def __init__(self, title, author, level):
        Book.count += 1
        self.book_id = Book.count
        self.title = title
        self.author = author
        self.level = level
        self.available = True

    def __str__(self):
        return f"Book ID: {self.book_id}\nTitle: {self.title}\nAuthor: {self.author}\nLevel: {self.level}\nAvailability: {'Available' if self.available else 'Not Available'}"


class Member:
    count = 0

    def __init__(self, name, email, level):
        Member.count += 1
        self.member_id = Member.count
        self.name = name
        self.email = email
        self.level = level
        self.borrowed_books = []

    def __str__(self):
        return f"Member ID: {self.member_id}\nName: {self.name}\nEmail: {self.email}\nLevel: {self.level}\nBorrowed Books: {', '.join([book.title for book in self.borrowed_books])}"


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def edit_member(self, member_id, name, email, level):
        for member in self.members:
            if member.member_id == member_id:
                member.name = name
                member.email = email
                member.level = level
                break

    def show_member(self):
        print("Id\t|\tName\t|\t\tEmail\t\t\t|\tLevel")
        for member in self.members:
            print(f"{member.member_id}\t|\t{member.name}\t|\t{member.email}\t\t|\t{member.level}")

        print('-' * 70)
        print('-' * 70)

    def delete_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                self.members.remove(member)
                return True
        return False

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        print("Id\t|\tTitle\t|\t\tAuthor\t\t\t|\tLevel\t|\tStatus")
        for book in self.books:
            print(f"{book.book_id}\t|\t{book.title}\t|\t{book.author}\t\t|\t{book.level}\t|\t{book.available}")

        print('-' * 70)
        print('-' * 70)

    def find_book_by_id(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def find_member_by_id(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def borrow_book(self, member_id, book_id):
        member = self.find_member_by_id(member_id)
        book = self.find_book_by_id(book_id)
        if member is None or book is None:
            return "Invalid member ID or book ID."

        if book.available and member.level >= book.level:
            book.available = False
            member.borrowed_books.append(book)
            return "Book borrowed successfully."
        else:
            return "Book is not available or member level is not suitable for borrowing."

    def return_book(self, member_id, book_id):
        member = self.find_member_by_id(member_id)
        book = self.find_book_by_id(book_id)
        if member is None or book is None:
            return "Invalid member ID or book ID."

        if book in member.borrowed_books:
            book.available = True
            member.borrowed_books.remove(book)
            return "Book returned successfully."
        else:
            return "This member did not borrow this book."

    def print_menu(self):
        print(f"{'-'*70}Welcome to the Library System{'-'*70}")
        print("1. Add Member")
        print("2. Edit Member")
        print("3. Show Member")
        print("4. Delete Member")
        print("5. Add Book")
        print("6. Show Books")
        print("7. Borrow Book")
        print("8. Return Book")
        print("9. Exit")


def main():
    library = Library()

    while True:
        library.print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("* Enter member name: ")
            email = input("* Enter member email: ")
            level = input("* Enter member level (A, B, or C): ").upper()
            member = Member(name, email, level)
            library.add_member(member)
            print("# Member added successfully.")

        elif choice == "2":
            member_id = int(input("Enter member ID to edit: "))
            name = input("Enter new member name: ")
            email = input("Enter new member email: ")
            level = input("Enter new member level (A, B, or C): ").upper()
            library.edit_member(member_id, name, email, level)
            print("Member edited successfully.")

        elif choice == "3":
            library.show_member()

        elif choice == "4":
            member_id = int(input("Enter member ID to delete: "))
            result = library.delete_member(member_id)
            if result:
                print("Member deleted successfully.")
            else:
                print("Member not found.")

        elif choice == "5":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            level = input("Enter book level (A, B, or C): ").upper()
            book = Book(title, author, level)
            library.add_book(book)
            print("Book added successfully.")

        elif choice == "6":
            library.show_books()

        elif choice == "7":
            member_id = int(input("Enter member ID: "))
            book_id = int(input("Enter book ID: "))
            result = library.borrow_book(member_id, book_id)
            print(result)

        elif choice == "8":
            member_id = int(input("Enter member ID: "))
            book_id = int(input("Enter book ID: "))
            result = library.return_book(member_id, book_id)
            print(result)

        elif choice == "9":
            print("Exiting the library system...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
