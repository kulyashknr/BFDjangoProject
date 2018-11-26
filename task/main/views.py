from django.contrib.auth.models import AnonymousUser
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import ReceiptModelSerializer, ReceiptAllSerializer,RestaurantModelSerializer, ReceiptCreateSerializer,ReviewsModelSerializer
from .models import Receipt, Restaurant, Reviews
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.http import Http404
from django.contrib.auth.models import User

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is None:
        return Response({'error': 'nepravilno'})

    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key})


@api_view(['GET'])
def receipts_detail(request, pk):
    try:
        receipt = Receipt.objects.get(id=pk)
    except Receipt.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReceiptAllSerializer(receipt)
        return Response(serializer.data)

class GenericReceiptList(generics.ListCreateAPIView):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptCreateSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Receipt.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class GenericReceiptDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptModelSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    lookup_field = 'receipt_id'

    def get_object(self):
        return Receipt.objects.get(id=self.kwargs[self.lookup_field])

    def get_queryset(self):
        return Receipt.objects.for_user(self.request.user)

class GenericRestaurantList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantModelSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Restaurant.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class GenericRestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantModelSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    lookup_field = 'restaurant_id'

    def get_object(self):
        return Restaurant.objects.get(id=self.kwargs['restaurant_id'])

    def get_queryset(self):
        return Restaurant.objects.for_user(self.request.user)


class GenericReviewsList(generics.ListCreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsModelSerializer
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Reviews.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class GenericReviewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsModelSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    lookup_field = 'reviews_id'

    def get_object(self):
        return Reviews.objects.get(id=self.kwargs[self.lookup_field])

    def get_queryset(self):
        return Reviews.objects.for_user(self.request.user)