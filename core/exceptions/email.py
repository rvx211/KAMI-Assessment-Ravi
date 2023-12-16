"""This is library for email custom exception"""
from rest_framework import status

from .base import BaseCustomException


class EmailEmptyException(BaseCustomException):
    """This is email empty exception

    Args:
        BaseCustomException (object): Base custom exception class
    """
    def __init__(self):
        detail = "Email cannot be empty"
        super().__init__(detail, status.HTTP_400_BAD_REQUEST)

class EmailFormatValidationException(BaseCustomException):
    """This is email format validation exception

    Args:
        BaseCustomException (object): Base custom exception class
    """
    def __init__(self):
        detail = "Please enter a valid email address"
        super().__init__(detail, status.HTTP_400_BAD_REQUEST)

class EmailAlreadyExistsException(BaseCustomException):
    """This is email already exists exception

    Args:
        BaseCustomException (object): Base custom exception class
    """
    def __init__(self):
        detail = "Email already exists"
        super().__init__(detail, status.HTTP_400_BAD_REQUEST)
