from django.db import models
from .models import Receipt


class ReceiptForm(models.ModelForm):
    class Meta:
        fields = ['title', 'description', 'restaurant', 'created_by', 'review']

class RestaurantForm(models.ModelForm):
    class Meta:
        fields = ['name', 'address', 'tel', 'created_by']

class ReviewsForm(models.ModelForm):
    class Meta:
        fields = ["text", 'author']
