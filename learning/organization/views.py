from django.http import JsonResponse


def first_view(request):
    return JsonResponse({"message": "Hello World"})


def welcome(request):
    return JsonResponse({"greetings": "Welcome to Django Class"})