"""
    This module contains the customers urls
"""

from rest_framework_mongoengine import routers
from .views import CustomerView

# Mongo routers
router = routers.DefaultRouter()
router.register('', CustomerView, base_name='customers')

urlpatterns = [] + router.urls
