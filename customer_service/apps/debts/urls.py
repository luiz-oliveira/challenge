from django.urls import path, include
from rest_framework import routers
from .views import DebtView

router = routers.DefaultRouter()
router.register('', DebtView, base_name='debts')

urlpatterns = [] + router.urls
