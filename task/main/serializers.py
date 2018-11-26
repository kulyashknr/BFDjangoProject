from rest_framework import serializers
from .models import Receipt, Restaurant, Reviews
from django.contrib.auth.models import User
from datetime import datetime

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')



class RestaurantModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'address', 'tel')



class ReviewsModelSerializer(serializers.ModelSerializer):
    #com_id = ReceiptModelSerializer(read_only=False)
    created_date = serializers.DateTimeField(read_only = True, default=datetime.now)
    class Meta:
        model = Reviews
        fields = ('id','com_id', 'text', 'created_date')

class ReceiptCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Receipt
        fields = ('id', 'title', 'description')

class ReceiptModelSerializer(serializers.ModelSerializer):
    #restaurant =  RestaurantModelSerializer()
    #review = ReviewsModelSerializer()

    class Meta:
        model = Receipt
        fields = ('id', 'title', 'description', 'created_by','restaurant','review')

class ReceiptAllSerializer(serializers.ModelSerializer):
    restaurant =  RestaurantModelSerializer()
    review = ReviewsModelSerializer()
    created_by = UserSerializer()
    class Meta:
        model = Receipt
        fields = ('id', 'title', 'description', 'created_by','restaurant','review')