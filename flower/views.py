from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response


# Create your views here.
class TestApiView(APIView):
    def get(self, request):
        return Response(data={ "succesfusfslly" })
