"""
Sample data script for the Library Management System.

How to run this:
    python manage.py shell < sample_data.py

This creates a few Authors, Books, Members, and Borrowing records
so you can test the list/detail pages and the relationships between models.
"""

from authors.models import Author
from books.models import Book
from members.models import Member
from borrowing.models import Borrowing

# ---- Authors ----
author1 = Author.objects.create(
    name="J.K. Rowling",
    bio="British author, best known for the Harry Potter series.",
    birth_date="1965-07-31",
    nationality="British",
)
author2 = Author.objects.create(
    name="George Orwell",
    bio="English novelist and essayist, known for 1984 and Animal Farm.",
    birth_date="1903-06-25",
    nationality="British",
)

# ---- Books (each linked to an Author via ForeignKey) ----
book1 = Book.objects.create(
    title="Harry Potter and the Philosopher's Stone",
    author=author1,
    isbn="9780747532699",
    publication_date="1997-06-26",
    genre="Fantasy",
    status="available",
)
book2 = Book.objects.create(
    title="1984",
    author=author2,
    isbn="9780451524935",
    publication_date="1949-06-08",
    genre="Dystopian",
    status="borrowed",
)
book3 = Book.objects.create(
    title="Animal Farm",
    author=author2,
    isbn="9780451526342",
    publication_date="1945-08-17",
    genre="Political Satire",
    status="available",
)

# ---- Members ----
member1 = Member.objects.create(
    name="Pranay",
    email="pranay@example.com",
    phone="01700000000",
    address="Hajiganj, Chittagong",
)
member2 = Member.objects.create(
    name="Rahim Uddin",
    email="rahim@example.com",
    phone="01800000000",
    address="Chittagong",
)

# ---- Borrowing (links a Member to a Book) ----
Borrowing.objects.create(
    book=book2,
    member=member1,
    return_date=None,
    is_returned=False,
)
Borrowing.objects.create(
    book=book1,
    member=member2,
    return_date="2026-06-01",
    is_returned=True,
)

print("Sample data created successfully!")
print(f"Authors: {Author.objects.count()}")
print(f"Books: {Book.objects.count()}")
print(f"Members: {Member.objects.count()}")
print(f"Borrowing records: {Borrowing.objects.count()}")
