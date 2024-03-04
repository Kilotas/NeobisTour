from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import Response
from rest_framework import status
from .models import Tour, TourCategory, Review, Booking
from .serializers import TourSerializer, TourCategorySerializer, ReviewSerializer, BookingSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, status
from .models import User
from .permissions import UserPermission
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from .models import Tour
from .serializers import TourSerializer

class TourDetailAPIView(APIView):
    @extend_schema(
        description="Get a specific tour by id",
        responses={200: TourSerializer()},
    )
    def get(self, request, pk):
        try:
            tour = Tour.objects.get(pk=pk)
            serializer = TourSerializer(tour)
            return Response(serializer.data)
        except Tour.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @extend_schema(
        description="Update details of a specific tour by id",
        request=TourSerializer,
        responses={200: TourSerializer()},
    )
    def put(self, request, pk):
        try:
            tour = Tour.objects.get(pk=pk)
            serializer = TourSerializer(tour, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Tour.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @extend_schema(
        description="Delete a specific tour by id",
        responses={204: None},
    )
    def delete(self, request, pk):
        try:
            tour = Tour.objects.get(pk=pk)
            tour.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Tour.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class TourListCreateAPIView(APIView):

    @extend_schema(
        description="Get a list of tours",
        responses={200: TourSerializer(many=True)},
    )
    def get(self, request):
        tours = Tour.objects.all()
        serializer = TourSerializer(tours, many=True)
        return Response(serializer.data)

    @extend_schema(
        description="Create a new tour",
        request=TourSerializer,
        responses={201: TourSerializer()},
    )
    def post(self, request):
        serializer = TourSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TourCategoryListCreateAPIView(APIView):
    @extend_schema(
        description="Get a list of tour categories",
        responses={200: TourCategorySerializer(many=True)},
    )

    def get(self, request):
        categories = Review.objects.all()
        serializer = ReviewSerializer(categories, many=True)
        return Response(serializer.data)

    @extend_schema(
        description="Create a new tour category",
        request=TourCategorySerializer,
        responses={201: TourCategorySerializer()},
    )

    def post(self, request):
        serializer = TourCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReviewListCreateAPIView(APIView):
    @extend_schema(
        description="Get a list of reviews",
        responses={200: ReviewSerializer(many=True)},
    )
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    @extend_schema(
        description="Create a new review",
        request=ReviewSerializer,
        responses={201: ReviewSerializer()},
    )

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookingListCreateAPIView(APIView):
    @extend_schema(
        description="Get a list of bookings",
        responses={200: BookingSerializer(many=True)},
    )
    def get(self, request):
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

    @extend_schema(
        description="Create a new booking",
        request=BookingSerializer,
        responses={201: BookingSerializer()},
    )
    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
'''
class UserCreateAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''
class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [UserPermission]

    @extend_schema(
        description="This endpoint allows you to perform operations on users."
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        description="Retrieve a specific user by ID.",
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        description="Create a new user.",
        request=UserSerializer,
        responses={201: UserSerializer()},
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        description="Update an existing user by ID.",
        request=UserSerializer,
        responses={200: UserSerializer()},
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        description="Partial update an existing user by ID.",
        request=UserSerializer,
        responses={200: UserSerializer()},
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        description="Delete a user by ID.",
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)




