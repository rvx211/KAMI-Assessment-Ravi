"""This is user v2 URLs"""
from django.urls import re_path

from .views import (UserLoginView, UserRegistrationView)

urlpatterns = [
    re_path(r'^login/$', UserLoginView.as_view(), name='user-login'),
    re_path(r'^registration/$', UserRegistrationView.as_view(), name='user-registration')
]
