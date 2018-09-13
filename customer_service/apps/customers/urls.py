from django.urls import path, include
from .views import CustomerList, CustomerDetails

urlpatterns = [
    path('customers/', CustomerList.as_view(), name="customer-list"),
    path('customers/<int:pk>/', CustomerDetails.as_view(), name="customer-detail")
]
