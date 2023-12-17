"""This module provide extended User model"""
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from core.managers import UserManager
from core.models import BaseModel

# Create your models here.
class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    """This is user model for the application

    Args:
        BaseModel (object): Base model object for the entire application
        AbstractBaseUser (object): Abstract base user object from Django
        PermissionsMixin (object): Permission mixin from Django
    """
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(_("password"), max_length=128)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ["email", "password"]

    class Meta:
        """This is meta class for User object
        """
        verbose_name = _('user')
        verbose_name_plural = _('users')
