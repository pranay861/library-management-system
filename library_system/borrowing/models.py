from django.db import models
from books.models import Book
from members.models import Member


class Borrowing(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrowings')
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='borrowings')
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.book.title} -> {self.member.name}"
