from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('login/', views.login),
    path('receipts/',views.GenericReceiptList.as_view()),
    path('receipts/<int:pk>/',views.receipts_detail),
    path('receipts/update/<int:receipt_id>/', views.GenericReceiptDetail.as_view()),
    path('restaurants/',views.GenericRestaurantList.as_view()),
    path('restaurants/<int:restaurant_id>/', views.GenericRestaurantDetail.as_view()),
    path('reviews/',views.GenericReviewsList.as_view()),
    path('reviews/<int:reviews_id>/', views.GenericReviewsDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)