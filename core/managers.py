"""This module provide extended User Manager object"""
from django.contrib.auth.models import User, UserManager as CoreManager

class UserManager(CoreManager):
    """This is User Manager object that override Django's own User Manager

    Args:
        CoreManager (object): User Manager object from Django
    """
    def create_staff_user(
        self,
        username: str,
        email: str,
        password: str,
        **extra_fields: dict) -> User:
        """This method is to create KAMI Airline staff

        Args:
            username (str): Username of the staff
            email (str): Email of the staff
            password (str): Password of the staff

        Returns:
            User: Newly created user object
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        username = username or email
        user = self._create_user(username, email, password, **extra_fields)
        return user

    def create_admin_user(
        self,
        username: str,
        email: str,
        password: str,
        **extra_fields: dict) -> User:
        """This method is to create KAMI Airline admin

        Args:
            username (str): Username of the admin
            email (str): Email of the admin
            password (str): Password of the admin

        Returns:
            User: Newly created user object
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        username = username or email
        user = self._create_user(username, email, password, **extra_fields)
        return user

    def create_user(self, *args: tuple, **kwargs: dict) -> User:
        return self.create_staff_user(*args, **kwargs)

    def create_superuser(self, *args: tuple, **kwargs: dict) -> User:
        return self.create_admin(*args, **kwargs)
