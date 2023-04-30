from django.db import models
from books.models import Book  # because we need to connect sales with books
# Create your models here.


class Sales (models.Model):

    # book is the foreign key referring to the Book class- you'll need to import it too
    # "CASCADE"implies that when a book is deleted all positions related to the book will be deleted.
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    # Number of books sold( of the same type within a transaction)
    quantity = models.PositiveIntegerField()

    # Total sale price.  For example, if a book's price is $10. and three are sold, the price will be 10*3 =$30.
    price = models.FloatField()

    # Date of sale - will be automatically set to the current date
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"id: {self.id}, book: {self.book.name}, quanity: {self.quantity}"
