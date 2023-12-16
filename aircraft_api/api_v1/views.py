"""This is aircraft views module"""
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .serializers import (AircraftSerializer, AircraftListSerializer)

# Create your views here.
class AircraftCalculationView(CreateAPIView):
    """This is Aircraft Calculation View

    Args:
        CreateAPIView (object): Django REST Framework CreateAPIView
    """
    serializer_class = AircraftSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        """This is override create function of the Aircraft Calculation View

        Args:
            request (Request): Aircraft calculation request

        Returns:
            Response: Aircraft calculation response
        """
        serializer = self.serializer_class(
            data=request.data,
            context={"user": request.user, "username": request.user.get_username()})
        if serializer.is_valid():
            message = serializer.create(serializer.validated_data)
            if message["status"] == status.HTTP_200_OK:
                return Response(message, status=status.HTTP_200_OK)
            return Response(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AircraftCalculationListView(CreateAPIView):
    """This is Aircraft Calculation List View

    Args:
        CreateAPIView (object): Django REST Framework CreateAPIView
    """
    serializer_class = AircraftListSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        """This is override create function of the Aircraft Calculation List View

        Args:
            request (Request): Aircraft calculation list request

        Returns:
            Response: Aircraft calculation list response
        """
        serializer = self.serializer_class(
            data=request.data,
            context={"user": request.user, "username": request.user.get_username()})
        if serializer.is_valid():
            message = serializer.create(serializer.validated_data)
            if message["status"] == status.HTTP_200_OK:
                return Response(message, status=status.HTTP_200_OK)
            return Response(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
