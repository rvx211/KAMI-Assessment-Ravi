"""This is library for application custom exception"""
from rest_framework.exceptions import APIException


class BaseCustomException(APIException):
    """This is base exception class

    Args:
        APIException (object): Inherit API Exception class from Django REST Framework
    """
    detail = None
    status_code = None

    def __init__(self, detail: str, code: int) -> None:
        """This is initial base custom exception

        Args:
            detail (str): Exception detail
            code (int): Exception HTTP status code
        """
        super().__init__(detail, code)
        self.detail = detail
        self.status_code = code
