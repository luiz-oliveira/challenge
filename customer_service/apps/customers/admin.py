"""
    This module contains the user django-admin
"""
from django.contrib import admin
from .models import Customer

admin.site.register(Customer)
