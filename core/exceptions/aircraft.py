"""This is library for aircraft custom exception"""
from rest_framework import status

from .base import BaseCustomException


class AircraftIDEmptyException(BaseCustomException):
    """This is aircraft ID empty exception

    Args:
        BaseCustomException (object): Base custom exception class
    """
    def __init__(self):
        detail = "Aircraft ID cannot be empty"
        super().__init__(detail, status.HTTP_400_BAD_REQUEST)

class AircraftIDNotInteger(BaseCustomException):
    """This is aircraft ID not integer exception

    Args:
        BaseCustomException (object): Base custom exception class
    """
    def __init__(self) -> None:
        detail = "Aircraft ID must be integer"
        super().__init__(detail, status.HTTP_400_BAD_REQUEST)

class AircraftPassengerEmptyException(BaseCustomException):
    """This is aircraft passenger empty exception

    Args:
        BaseCustomException (object): Base custom exception class
    """
    def __init__(self):
        detail = "Aircraft passenger cannot be empty"
        super().__init__(detail, status.HTTP_400_BAD_REQUEST)

class AircraftPassengerNotInteger(BaseCustomException):
    """This is aircraft passenger not integer exception

    Args:
        BaseCustomException (object): Base custom exception class
    """
    def __init__(self) -> None:
        detail = "Aircraft passenger must be integer"
        super().__init__(detail, status.HTTP_400_BAD_REQUEST)

class AircraftListEmptyException(BaseCustomException):
    """This is aircraft list empty exception

    Args:
        BaseCustomException (object): Base custom exception class
    """
    def __init__(self):
        detail = "Aircraft list cannot be empty"
        super().__init__(detail, status.HTTP_400_BAD_REQUEST)
