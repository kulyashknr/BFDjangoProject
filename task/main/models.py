from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


# Create your models here.
class ReceiptManager(models.Manager):
    def for_user(self, user):
        return self.filter(created_by=user)

class RestaurantManager(models.Manager):
    def for_user(self, user):
        return self.filter(created_by=user)

class ReviewsManager(models.Manager):
    def for_user(self, user):
        return self.filter(created_by=user)


class Receipt(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # review = models.ForeignKey('Reviews', on_delete=models.CASCADE,related_name='reviews')
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE, related_name='restaurants')
    objects = ReceiptManager()


class Restaurant(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    tel = models.CharField(max_length=120)
    objects = RestaurantManager()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Reviews(models.Model):
    com_id = models.ForeignKey('Receipt', on_delete=models.CASCADE, null=True, related_name="reviews")
    created_date = models.DateTimeField(default=datetime.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=250)
    objects = ReviewsManager()