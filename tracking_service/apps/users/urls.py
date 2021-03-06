"""
    This module contains the users urls
"""

from django.urls import path
from .views import UserList, UserDetails

urlpatterns = [
    path('', UserList.as_view(), name="users-list"),
    path('<int:pk>/', UserDetails.as_view(), name="users-detail")
]
