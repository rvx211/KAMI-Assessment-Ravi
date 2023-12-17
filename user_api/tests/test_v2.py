"""This is test cases for the user module"""
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from core.exceptions.username import (
    UsernameEmptyException,
    UsernameLengthAlphanumericException,
    UsernameAlreadyExistsException,
    UsernameDidNotExistsException
)
from core.exceptions.email import (
    EmailEmptyException,
    EmailFormatValidationException,
    EmailAlreadyExistsException
)
from core.exceptions.password import (
    PasswordEmptyException,
    PasswordLengthException,
    PasswordCharacterValidationException,
    PasswordDidNotExistsException
)
from ..models import User

# Create your tests here.
class UserAPITest(APITestCase):
    """This is the user test class

    Args:
        APITestCase (object): Django REST Framework APITestCase
    """
    def setUp(self) -> None:
        """This is setup function for the user test
        """
        self.register_user_url = 'v2:user-register'
        self.login_user_url = 'v2:user-login'
        self.register_user_1 = {
            "username": None, "email": "test01@email.com", "password": "&$P4ssw0rd01"
        }
        self.register_user_2 = {
            "username": "username02", "email": None, "password": "&$P4ssw0rd02"
        }
        self.register_user_3 = {
            "username": "username03", "email": "test03@email.com", "password": None
        }
        self.register_user_4 = {
            "username": "user", "email": "test04@email.com", "password": "&$P4ssw0rd04"
        }
        self.register_user_5 = {
            "username": "username", "email": "test05@email.com", "password": "&$P4ssw0rd05"
        }
        self.register_user_6 = {
            "username": "username06", "email": "test06emailcom", "password": "&$P4ssw0rd06"
        }
        self.register_user_7 = {
            "username": "username07", "email": "test07@email.com", "password": "&$P4"
        }
        self.register_user_8 = {
            "username": "username08", "email": "test07@email.com", "password": "password"
        }
        self.register_user_9 = {
            "username": "username09", "email": "test09@email.com", "password": "&$P4ssw0rd09"
        }
        self.register_user_10 = {
            "username": "username10", "email": "test10@email.com", "password": "&$P4ssw0rd10"
        }
        self.register_user_11 = {
            "username": "username11", "email": "test11@email.com", "password": "&$P4ssw0rd11"
        }
        self.login_user_1 = {
            "username": "", "password": "&$P4ssw0rdl01"
        }
        self.login_user_2 = {
            "username": "logintest02", "password": ""
        }
        self.login_user_3 = {
            "username": "logintest03", "password": "&$P4ssw0rdl03"
        }
        self.login_user_4 = {
            "username": "logintest04", "password": "&$P4ssw0rd1"
        }
        self.login_user_5 = {
            "username": "logintest05", "password": "&$P4ssw0rdl05"
        }
        User.objects.create_user(
            username="username09", email="test19@email.com", password="&$P4ssw0rd09")
        User.objects.create_user(
            username="username20", email="test10@email.com", password="&$P4ssw0rd10")
        User.objects.create_user(
            username="logintest01", email="logintest01@email.com", password="&$P4ssw0rdl01")
        User.objects.create_user(
            username="logintest02", email="logintest02@email.com", password="&$P4ssw0rdl02")
        User.objects.create_user(
            username="logintest04", email="logintest04@email.com", password="&$P4ssw0rdl04")
        User.objects.create_user(
            username="logintest05", email="logintest05@email.com", password="&$P4ssw0rdl05")

    def test_register_empty_username(self):
        """This is user registration test with empty username
        """
        response = self.client.post(reverse(self.register_user_url), data=self.register_user_1)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'], UsernameEmptyException.detail)

    def test_register_empty_email(self):
        """This is user registration test with empty email
        """
        response = self.client.post(reverse(self.register_user_url), data=self.register_user_2)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'], EmailEmptyException.detail)

    def test_register_empty_password(self):
        """This is user registration test with empty password
        """
        response = self.client.post(reverse(self.register_user_url), data=self.register_user_3)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'], PasswordEmptyException.detail)

    def test_register_less_username(self):
        """This is user registration test with short username bellow 6 caharacters
        """
        response = self.client.post(reverse(self.register_user_url), data=self.register_user_4)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'], UsernameLengthAlphanumericException.detail)

    def test_register_non_alphanumeric_username(self):
        """This is user registration test with non alphanumeric username
        """
        response = self.client.post(reverse(self.register_user_url), data=self.register_user_5)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'], UsernameLengthAlphanumericException.detail)

    def test_register_invalid_email(self):
        """This is user registration test with invalid email address
        """
        response = self.client.post(reverse(self.register_user_url), data=self.register_user_6)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'], EmailFormatValidationException.detail)

    def test_register_less_password(self):
        """This is user registration test with short password
        """
        response = self.client.post(reverse(self.register_user_url), data=self.register_user_7)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'], PasswordLengthException.detail)

    def test_register_invalid_password(self):
        """This is user registration test with invalid password
        """
        response = self.client.post(reverse(self.register_user_url), data=self.register_user_8)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'], PasswordCharacterValidationException.detail)

    def test_register_existing_username(self):
        """This is user registration test with username already exists
        """
        response = self.client.post(reverse(self.register_user_url), data=self.register_user_9)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'], UsernameAlreadyExistsException.detail)

    def test_register_existing_email(self):
        """This is user registration test with email already exists
        """
        response = self.client.post(reverse(self.register_user_url), data=self.register_user_10)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'], EmailAlreadyExistsException.detail)

    def test_register_valid_data(self):
        """This is user registration test with valid data
        """
        response = self.client.post(reverse(self.register_user_url), data=self.register_user_11)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.filter(username=self.register_user_11['username']).count(), 1)
        self.assertEqual(response.data['message'], f"User {self.register_user_11['username']} created successfully")

    def test_login_empty_username(self):
        """This is user login test with empty username
        """
        response = self.client.post(reverse(self.login_user_url), data=self.login_user_1)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'], UsernameEmptyException.detail)

    def test_login_empty_password(self):
        """This is user login test with empty password
        """
        response = self.client.post(reverse(self.login_user_url), data=self.login_user_2)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'], PasswordEmptyException.detail)

    def test_login_wrong_username(self):
        """This is user login test with wrong username
        """
        response = self.client.post(reverse(self.login_user_url), data=self.login_user_3)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'], UsernameDidNotExistsException.detail)

    def test_login_wrong_password(self):
        """This is user login test with wrong password
        """
        response = self.client.post(reverse(self.login_user_url), data=self.login_user_4)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'], PasswordDidNotExistsException.detail)

    def test_login_valid_data(self):
        """This is user login test with valid data
        """
        response = self.client.post(reverse(self.login_user_url), data=self.register_user_11)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual('access' in response.data, True)
        self.assertEqual('refresh' in response.data, True)
