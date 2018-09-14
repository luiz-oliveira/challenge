"""
    This module contains the user django-admin
"""
from django.contrib import admin
from .models import Debt

admin.site.register(Debt)
