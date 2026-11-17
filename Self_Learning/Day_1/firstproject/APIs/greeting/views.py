from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

def hello(request):
    return JsonResponse({"message": "Hello and welcome!!!"})
