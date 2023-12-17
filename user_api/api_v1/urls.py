"""This is user v1 URLs"""
from django.urls import re_path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (UserLoginView, UserRegistrationView)

urlpatterns = [
    re_path(r'^login/$', UserLoginView.as_view(), name='user-login'),
    re_path(r'^login/refresh/$', TokenRefreshView.as_view(), name='user-refresh'),
    re_path(r'^registration/$', UserRegistrationView.as_view(), name='user-registration')
]
