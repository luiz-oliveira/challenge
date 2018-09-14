from django.urls import path, include
from .views import UserList, UserDetails

urlpatterns = [
    path('users/', UserList.as_view(), name="user-list"),
    path('users/<int:pk>/', UserDetails.as_view(), name="user-list")
]