from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *
import random


# Create your views here.

class FlowerAlsoBrowsedApiView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = FlowerSerializer
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        queryset = list(Flower.objects.all())
        random_items = random.sample(queryset, min(len(queryset), 3))

        return random_items


class FlowerBestApiView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = FlowerSerializer
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        queryset = Flower.objects.order_by('-sold_quantity')
        return queryset


class FlowerListApiView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = FlowerSerializer
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        # queryset = Flower.objects.filter(categories__in=[(self.request.parser_context.get('kwargs').get('cat_id', '0'))])
        cat_id = self.request.GET.get('cat_id', None)
        search = self.request.GET.get('search_text', None)
        queryset = Flower.objects.all()
        if cat_id:
            queryset = queryset.filter(categories__in=[cat_id])
        if search:
            queryset = queryset.filter(title__icontains=search)
        print(queryset)
        return queryset


class FlowerDetailApiView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = FlowerSerializer
    authentication_classes = [JWTAuthentication]
    queryset = Flower.objects.all()


class CategoryListApiView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    authentication_classes = [JWTAuthentication]


class CategoryDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = CategorySerializer
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        queryset = Flower.objects.filter(categories__in=[self.kwargs['pk']])
        return queryset


class ReviewListAPIView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    authentication_classes = [JWTAuthentication]


class ReviewItemUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView, generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewValidateSerializer
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        if Review.objects.filter(author=request.user).exists():
            return Response({"detail": "requesting user already created review update or delete previour review"},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, *args, **kwargs):
        instance = Review.objects.get(author=request.user)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = Review.objects.get(author=request.user)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = Review.objects.get(author=request.user)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class FlowerViewSet(ModelViewSet):
    serializer_class = FlowerSerializer
    queryset = Flower.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]


class ColorViewSet(ModelViewSet):
    serializer_class = ColorSerializer
    queryset = Color.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]


class PhotoViewSet(ModelViewSet):
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewValidateSerializer
    queryset = Review.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
