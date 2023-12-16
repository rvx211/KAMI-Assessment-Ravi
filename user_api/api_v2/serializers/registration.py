"""This is the serializers module for the user object"""
import re

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from rest_framework import serializers

from core.exceptions.email import (
    EmailEmptyException,
    EmailFormatValidationException,
    EmailAlreadyExistsException)
from core.exceptions.password import (
    PasswordCharacterValidationException,
    PasswordEmptyException,
    PasswordLengthException)
from core.exceptions.username import (
    UsernameAlreadyExistsException,
    UsernameEmptyException,
    UsernameLengthAlphanumericException)
from user_api.models import User

class UserRegistrationRequestSerializer(serializers.ModelSerializer):
    """This is serializer for user registration request.

    Args:
        serializers (object): Model serializers from Django REST API Framework
    """
    class Meta:
        """This is the meta class for user registration request serializers
        """
        model = User
        fields = ['username', 'email', 'password']

    def validate_username(self, value: str) -> str:
        """This is function to validate username input

        Args:
            value (str): Username input

        Returns:
            str: Validated username
        """
        if value in (None, ""):
            raise UsernameEmptyException
        elif len(value) < settings.MINIMUM_USERNAME_LENGTH or not (
            re.search(r'[a-zA-Z]+', value) and re.search(r'\d+', value)
        ):
            raise UsernameLengthAlphanumericException
        elif User.objects.filter(username=value).exists():
            raise UsernameAlreadyExistsException
        return value

    def validate_password(self, value: str) -> str:
        """This is function to validate password input

        Args:
            value (str): Password input

        Returns:
            str: Validated password
        """
        if value in (None, ""):
            raise PasswordEmptyException
        elif len(value) < settings.MINIMUM_PASSWORD_LENGTH:
            raise PasswordLengthException
        elif not (re.search(r'[a-zA-Z]+', value) and \
            re.search(r'\d+', value) and \
            re.search(r'[!@#%^&*()_+-=[]{}|;\':\",./<>?~`]+', value) and \
            any(x.isupper() for x in value) and \
            any(x.islower() for x in value)):
            raise PasswordCharacterValidationException
        return value

    def validate_email(self, value: str) -> str:
        """This is function to validate email input

        Args:
            value (str): Email input

        Returns:
            str: Validated email
        """
        if value in (None, ""):
            raise EmailEmptyException
        try:
            validate_email(value)
            if User.objects.filter(username=value).exists():
                raise EmailAlreadyExistsException
        except ValidationError as exc:
            raise EmailFormatValidationException from exc
        return value

    def create(self, validated_data: dict) -> object:
        """This is override create method of user resgistration serializer

        Args:
            validated_data (dict): User registration validated data

        Returns:
            object: User model
        """
        return User.objects.create(validated_data)
