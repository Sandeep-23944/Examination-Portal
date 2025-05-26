# core/admin.py
from django.contrib import admin
from .models import Profile

# Register the Profile model with the admin panel
admin.site.register(Profile)
