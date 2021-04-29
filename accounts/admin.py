from django.contrib import admin

# Register your models here.

from . models import *
from . models import Customer

admin .site.register(Customer)
admin .site.register(Product)
admin .site.register(Tag)
admin .site.register(Order)


