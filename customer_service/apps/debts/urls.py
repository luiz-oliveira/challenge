"""
    This module contains the debits urls
"""

from rest_framework import routers
from .views import DebtView

ROUTER = routers.DefaultRouter()
ROUTER.register('', DebtView, base_name='debts')

urlpatterns = [] + ROUTER.urls
