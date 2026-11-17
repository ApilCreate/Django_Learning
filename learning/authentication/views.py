from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view

@api_view(['GET'])
# Create your views here.
def first_view(request):
    return JsonResponse({"message": "Hello World"})

def welcome(request):
    return JsonResponse({"greetings": "Welcome to Django Class"})