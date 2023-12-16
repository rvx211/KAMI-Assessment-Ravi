"""This is library for username custom exception"""
from rest_framework import status

from .base import BaseCustomException


class UsernameEmptyException(BaseCustomException):
    """This is username empty exception

    Args:
        BaseCustomException (object): Base custom exception class
    """
    def __init__(self):
        detail = "Username cannot be empty"
        super().__init__(detail, status.HTTP_400_BAD_REQUEST)

class UsernameLengthAlphanumericException(BaseCustomException):
    """This is username length and alphanumeric exception

    Args:
        BaseCustomException (object): Base custom exception class
    """
    def __init__(self):
        detail = "Username should be alphanumeric between 6 and 32 characters"
        super().__init__(detail, status.HTTP_400_BAD_REQUEST)

class UsernameAlreadyExistsException(BaseCustomException):
    """This is username already exists exception

    Args:
        BaseCustomException (object): Base custom exception class
    """
    def __init__(self):
        detail = "Username already exists"
        super().__init__(detail, status.HTTP_400_BAD_REQUEST)

class UsernameDidNotExistsException(BaseCustomException):
    """This is username did not exists exception

    Args:
        BaseCustomException (object): Base custom exception class
    """
    def __init__(self):
        detail = "Invalid username, please enter valid username"
        super().__init__(detail, status.HTTP_400_BAD_REQUEST)
