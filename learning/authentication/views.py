from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login as auth_login
from .serializer import LoginSerializer

@api_view(['GET'])
# Create your views here.
def first_view(request):
    return JsonResponse({"message": "Hello World"})

def welcome(request):
    return JsonResponse({"greetings": "Welcome to Django Class"})

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    #Auth logic here:
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return JsonResponse({'message': 'Login Successful'})
    else:
        return JsonResponse({'message': 'Invalid Credentials'}, status=401)


