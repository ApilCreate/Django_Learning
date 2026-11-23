from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_teacher, name='create_teacher'),
    path('retrive/', views.retrive_teacher, name='retrive_teacher'),
    path('update/<int:pk>/', views.update_teacher, name='update_teacher'),
    path('delete/<int:pk>/', views.delete_teacher, name='delete_teacher'),
]