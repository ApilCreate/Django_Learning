from django.urls import path
from .views import organization_view

urlpatterns = [
    path('details/', organization_view),
]