from django.urls import path, include
from .views import UserList, UserDetails

urlpatterns = [
    path('', UserList.as_view(), name="users-list"),
    path('<int:pk>/', UserDetails.as_view(), name="users-detail")
]