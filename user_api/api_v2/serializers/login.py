"""This is the serializers module for the user object"""
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from core.exceptions.password import (
    PasswordEmptyException, PasswordDidNotExistsException)
from core.exceptions.username import (
    UsernameEmptyException, UsernameDidNotExistsException)
from user_api.models import User

class UserLoginSerializer(serializers.Serializer):
    """This is user login serializer

    Args:
        serializers (object): Django REST Framework serializer
    """
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs: dict) -> dict:
        """This is user login serializer validation

        Args:
            attrs (dict): Raw data

        Raises:
            UsernameEmptyException: Username empty exception
            PasswordEmptyException: Password empty exception
            PasswordDidNotExistsException: Password did not exists exception
            UsernameDidNotExistsException: Username did not exists exception

        Returns:
            dict: Validated data
        """
        username = attrs['username']
        password = attrs['password']
        if username in (None, ""):
            raise UsernameEmptyException
        elif password in (None, ""):
            raise PasswordEmptyException
        try:
            user = User.objects.get(username=username)
            password_correct = user.check_password(password)
            if not password_correct:
                raise PasswordDidNotExistsException
        except ObjectDoesNotExist as exc:
            raise UsernameDidNotExistsException from exc
        return attrs

    def create(self, validated_data: dict) -> dict:
        """This is override create function of user login serializer

        Args:
            validated_data (dict): user login validated data

        Returns:
            dict: User access token
        """
        user = User.objects.get(username=validated_data['username'])
        refresh = RefreshToken.for_user(user)
        user_token = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return user_token

    def update(self, instance: object, validated_data: dict) -> object:
        """This is update method of user login serializer

        Args:
            instance (object): User model
            validated_data (dict): User login validated data

        Returns:
            object: Updated user model
        """
        validated_data['modified_by'] = validated_data['username']
        return super().update(instance, validated_data)
