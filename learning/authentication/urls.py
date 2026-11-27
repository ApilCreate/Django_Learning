from django.urls import path
from .views import first_view, welcome, login

urlpatterns = [
    path('first/', first_view, name='first_view'),
    path('greeting/', welcome, name='greetings'),
    path('login/', login)
]