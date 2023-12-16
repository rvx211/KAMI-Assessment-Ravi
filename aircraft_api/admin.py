"""This is admin site for aircraft"""
from django.contrib import admin
from .models import Aircraft

# Register your models here.
admin.site.register(Aircraft)
