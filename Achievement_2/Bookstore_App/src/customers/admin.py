from django.contrib import admin

# We must import the class here befoer we can register the class
from .models import Customer

# Register your models here.

admin.site.register(Customer)
