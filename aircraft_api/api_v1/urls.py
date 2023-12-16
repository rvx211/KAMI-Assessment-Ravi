"""This is aircraft v1 URLs"""
from django.urls import re_path

from .views import (AircraftCalculationView, AircraftCalculationListView)

urlpatterns = [
    re_path(
        r'^calculation/unit/$',
        AircraftCalculationView.as_view(),
        name='aircraft-calculation-unit'),
    re_path(
        r'^calculation/list/$',
        AircraftCalculationListView.as_view(),
        name='aircraft-calculation-list')
]
