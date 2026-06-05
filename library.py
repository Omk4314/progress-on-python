from datetime import datetime, timedelta


class Book:
    def __init__(self, title, author, isbn, is_available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"

    def mark_borrowed(self):
        self.is_available = False

    def mark_returned(self):
        self.is_available = True


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.loans = []  

    def __str__(self):
        return f"{self.name} (ID: {self.member_id})"

    def borrow_book(self, book, library):
        """Ask library to loan a book to this member."""
        if not isinstance(book, Book):
            print("Invalid book.")
            return False
        
        if not book.is_available:
            print("Book is currently not available")
            return False
        
        # Create the Loan (composition: Loan HAS Book and Member)
        due = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")
        loan = Loan(book, self, due)
        
        # Track it everywhere
        self.loans.append(loan)
        library.record_loan(loan)
        return True

    def return_book(self, loan, library):
        """Return a specific loan via the library."""
        if loan in self.loans:
            self.loans.remove(loan)
            library.close_loan(loan)
        else:
            print("Loan not found for this member.")


class Loan:
    def __init__(self, book, member, due_date):
        self.book = book          # Loan HAS a Book
        self.member = member      # Loan HAS a Member
        self.due_date = due_date

    def __str__(self):
        return f"Loan: {self.book.title} to {self.member.name}, due {self.due_date}"

    def __repr__(self):
        return f"Loan(book={self.book!r}, member={self.member!r}, due_date={self.due_date!r})"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []      # Library HAS Books
        self.members = []    # Library HAS Members
        self.loans = []      # Library HAS Loans

    def __str__(self):
        return f"{self.name}: {len(self.books)} books, {len(self.members)} members"

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)

    def register_member(self, member):
        if isinstance(member, Member):
            self.members.append(member)

    def record_loan(self, loan):
        """Called by Member.borrow_book to register a loan."""
        if isinstance(loan, Loan):
            loan.book.mark_borrowed()
            self.loans.append(loan)

    def close_loan(self, loan):
        """Called by Member.return_book to close a loan."""
        if loan in self.loans:
            loan.book.mark_returned()
            self.loans.remove(loan)

    def get_available_books(self):
        return [book for book in self.books if book.is_available]



if __name__ == "__main__":
    lib = Library("CS50 Library")

    b1 = Book("The C Programming Language", "Kernighan & Ritchie", "9780131103627")
    b2 = Book("Clean Code", "Robert C. Martin", "9780132350884")

    lib.add_book(b1)
    lib.add_book(b2)

    alice = Member("Alice", "M001")
    lib.register_member(alice)

    print("Available before borrow:", [b.title for b in lib.get_available_books()])
    
    alice.borrow_book(b1, lib)
    
    print("Available after borrow:", [b.title for b in lib.get_available_books()])
    print("Alice's loans:", alice.loans)
    
    alice.return_book(alice.loans[0], lib)
    
    print("Available after return:", [b.title for b in lib.get_available_books()])