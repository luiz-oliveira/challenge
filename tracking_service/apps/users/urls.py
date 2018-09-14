from django.urls import path, include
from .views import UserList, UserDetails

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetails.as_view())
]