"""This is the serializers module for the user object"""
from rest_framework import serializers
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
