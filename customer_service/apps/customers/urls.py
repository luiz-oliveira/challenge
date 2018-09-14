"""
    This module contains the customers urls
"""

from rest_framework import routers
from .views import CustomerView

ROUTER = routers.DefaultRouter()
ROUTER.register('', CustomerView, base_name='customers')

urlpatterns = [] + ROUTER.urls
