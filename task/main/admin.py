from django.contrib import admin
from .models import Receipt, Restaurant, Reviews

# Register your models here.
admin.site.register(Receipt)

admin.site.register(Restaurant)

admin.site.register(Reviews)