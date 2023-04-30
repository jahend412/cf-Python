from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=120)
    notes = models.TextField()

# String representation of the object.  This means that a customer named Jake with ID=1 will show as Jake instead of 1
    def __str__(self):
        return str(self.name)
