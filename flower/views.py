from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .models import *
from .serializers import *


# Create your views here.
class FlowerListApiView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = FlowerSerializer

    def get_queryset(self):
        queryset = Flower.objects.filter(categories__in=[self.kwargs['cat_id']])

        return queryset
