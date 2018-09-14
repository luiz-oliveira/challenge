from django.urls import path, include
from rest_framework import routers
from .views import CustomerView

router = routers.DefaultRouter()
router.register('', CustomerView, base_name='customers')

urlpatterns = [] + router.urls
