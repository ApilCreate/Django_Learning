from django.urls import path
from .views import View_Students

urlpatterns = [
    path('std/',View_Students),
]