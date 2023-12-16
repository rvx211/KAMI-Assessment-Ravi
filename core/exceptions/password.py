"""This is library for password custom exception"""
from rest_framework import status

from .base import BaseCustomException


class PasswordEmptyException(BaseCustomException):
    """This is password empty exception

    Args:
        BaseCustomException (object): Base custom exception class
    """
    def __init__(self):
        detail = "Password cannot be empty"
        super().__init__(detail, status.HTTP_400_BAD_REQUEST)

class PasswordLengthException(BaseCustomException):
    """This is password length exception

    Args:
        BaseCustomException (object): Base custom exception class
    """
    def __init__(self):
        detail = "Password should not be less than 8 characters"
        super().__init__(detail, status.HTTP_400_BAD_REQUEST)

class PasswordCharacterValidationException(BaseCustomException):
    """This is password character validation exception

    Args:
        BaseCustomException (object): Base custom exception class
    """
    def __init__(self):
        detail = "Password should be a combination of alphanumeric with" +\
            " one uppercase, one lowercase and one special character"
        super().__init__(detail, status.HTTP_401_UNAUTHORIZED)

class PasswordDidNotExistsException(BaseCustomException):
    """This is password did not exists exception

    Args:
        BaseCustomException (object): Base custom exception class
    """
    def __init__(self):
        detail = "Invalid password, please enter valid password"
        super().__init__(detail, status.HTTP_400_BAD_REQUEST)
