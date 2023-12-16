"""This is user views module"""
from rest_framework.generics import CreateAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .serializers.registration import UserRegistrationRequestSerializer
from .serializers.login import UserLoginSerializer

# Create your views here.
class UserRegistrationView(CreateAPIView):
    """This is user registration views

    Args:
        CreateAPIView (object): Django REST Framework CreateAPIView
    """
    serializer_class = UserRegistrationRequestSerializer
    permission_classes = []

    def create(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        """This is override create function of user registration view

        Args:
            request (Request): User registration request

        Returns:
            Response: User registration response
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            message = serializer.create(serializer.validated_data)
            if message["status"] == status.HTTP_200_OK:
                return Response(message, status=status.HTTP_200_OK)
            return Response(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(CreateAPIView):
    """This is user login view

    Args:
        CreateAPIView (object): Django REST Framework CreateAPIView
    """
    serializer_class = UserLoginSerializer
    permission_classes = []

    def create(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        """This is override create function of user login view

        Args:
            request (Request): User login request

        Returns:
            Response: User access token response
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user_token = serializer.create(serializer.validated_data)
            return Response(user_token, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    