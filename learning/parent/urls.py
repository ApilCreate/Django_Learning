from django.urls import path
from .views import (
    view_parent,
    create_parent_entry,
    get_parent,
    update_parent,
    delete_parent,
)

urlpatterns = [
    path('all/', view_parent),
    path('create/',create_parent_entry ),
    path('<int:pk>/', get_parent),
    path('update/<int:pk>/', update_parent),
    path('delete/<int:pk>/', delete_parent),
]