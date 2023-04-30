from django.db import models

# Create your models here.

#  Romance, classic, comic, fantasy, horror, other.
genre_choices = (
    ('classic', 'Classic'),
    ('romantic', 'Romantic'),
    ('comic', 'Comic'),
    ('fantasy', 'Fantasy'),
    ('horror', 'Horror'),
    ('educational', 'Educational')
)

# Hardcover, eBook, Audiobook
book_type_choice = (
    ('hardcover', 'Hardcover'),
    ('ebook', 'E-Book'),
    ('audiobook', 'Audiobook')
)


class Book (models.Model):
    # Book name
    name = models.CharField(max_length=120)

    # The list is shown as a dropdown to the user.  The default value is specified as "classic"
    genre = models.CharField(
        max_length=12, choices=genre_choices, default='classic')

    # The list is shown as a dropdown to the user.  The default value is specified as "Hardcover"
    book_type = models.CharField(
        max_length=12, choices=book_type_choice, default='Hardcover')

    # 'help-text' allows to add a tooltip, which you will see below the form field in the admin panel
    price = models.FloatField(help_text='in US dollars $')

    # Author's name
    author_name = models.CharField(max_length=120)

    def __str__(self):
        return str(self.name)
