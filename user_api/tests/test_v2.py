"""This is test cases for User module"""
import ast

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from core.exceptions.username import (
    UsernameLengthAlphanumericException,
    UsernameDidNotExistsException
)
from core.exceptions.password import (
    PasswordLengthException,
    PasswordCharacterValidationException,
    PasswordDidNotExistsException
)
from ..models import User

# Create your tests here.
class UserAPITest(APITestCase):
    """This is user test class

    Args:
        APITestCase (object): Django REST Framework APITestCase
    """
    def setUp(self) -> None:
        """This is setup function for the user test
        """
        self.register_user_url = 'user_v2:user-registration'
        self.login_user_url = 'user_v2:user-login'
        self.register_user_1 = {
            "username": "", "email": "v2test01@email.com", "password": "&$P4ssw0rd01"
        }
        self.register_user_2 = {
            "username": "v2username02", "email": "", "password": "&$P4ssw0rd02"
        }
        self.register_user_3 = {
            "username": "v2username03", "email": "v2test03@email.com", "password": ""
        }
        self.register_user_4 = {
            "username": "user", "email": "v2test04@email.com", "password": "&$P4ssw0rd04"
        }
        self.register_user_5 = {
            "username": "username", "email": "v2test05@email.com", "password": "&$P4ssw0rd05"
        }
        self.register_user_6 = {
            "username": "v2username06", "email": "v2test06emailcom", "password": "&$P4ssw0rd06"
        }
        self.register_user_7 = {
            "username": "v2username07", "email": "v2test07@email.com", "password": "&$P4"
        }
        self.register_user_8 = {
            "username": "v2username08", "email": "v2test07@email.com", "password": "password"
        }
        self.register_user_9 = {
            "username": "v2username09", "email": "v2test09@email.com", "password": "&$P4ssw0rd09"
        }
        self.register_user_10 = {
            "username": "v2username10", "email": "v2test10@email.com", "password": "&$P4ssw0rd10"
        }
        self.register_user_11 = {
            "username": "v2username11", "email": "v2test11@email.com", "password": "&$P4ssw0rd11"
        }
        self.login_user_1 = {
            "username": "", "password": "&$P4ssw0rdl01"
        }
        self.login_user_2 = {
            "username": "v2logintest02", "password": ""
        }
        self.login_user_3 = {
            "username": "v2logintest03", "password": "&$P4ssw0rdl03"
        }
        self.login_user_4 = {
            "username": "v2logintest04", "password": "&$P4ssw0rd1"
        }
        self.login_user_5 = {
            "username": "v2logintest05", "password": "&$P4ssw0rdl05"
        }
        User.objects.create_user(
            username="v2username09", email="v2test19@email.com", password="&$P4ssw0rd09")
        User.objects.create_user(
            username="v2username20", email="v2test10@email.com", password="&$P4ssw0rd10")
        User.objects.create_user(
            username="v2logintest01", email="v2logintest01@email.com", password="&$P4ssw0rdl01")
        User.objects.create_user(
            username="v2logintest02", email="v2logintest02@email.com", password="&$P4ssw0rdl02")
        User.objects.create_user(
            username="v2logintest04", email="v2logintest04@email.com", password="&$P4ssw0rdl04")
        User.objects.create_user(
            username="v2logintest05", email="v2logintest05@email.com", password="&$P4ssw0rdl05")

    def test_register_empty_username(self):
        """This is user registration test with empty username
        """
        response = self.client.post(reverse(self.register_user_url), data=self.register_user_1)
        content = ast.literal_eval(response.content.decode("UTF-8"))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(content['username'], ['This field may not be blank.'])

    def test_register_empty_email(self):
        """This is user registration test with empty email
        """
        response = self.client.post(reverse(self.register_user_url), data=self.register_user_2)
        content = ast.literal_eval(response.content.decode("UTF-8"))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(content['email'], ['This field may not be blank.'])

    def test_register_empty_password(self):
        """This is user registration test with empty password
        """
        response = self.client.post(reverse(self.register_user_url), data=self.register_user_3)
        content = ast.literal_eval(response.content.decode("UTF-8"))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(content['password'], ['This field may not be blank.'])

    def test_register_less_username(self):
        """This is user registration test with short username bellow 6 caharacters
        """
        response = self.client.post(reverse(self.register_user_url), data=self.register_user_4)
        content = ast.literal_eval(response.content.decode("UTF-8"))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(content['detail'], UsernameLengthAlphanumericException().detail)

    def test_register_non_alphanumeric_username(self):
        """This is user registration test with non alphanumeric username
        """
        response = self.client.post(reverse(self.register_user_url), data=self.register_user_5)
        content = ast.literal_eval(response.content.decode("UTF-8"))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(content['detail'], UsernameLengthAlphanumericException().detail)

    def test_register_invalid_email(self):
        """This is user registration test with invalid email address
        """
        response = self.client.post(reverse(self.register_user_url), data=self.register_user_6)
        content = ast.literal_eval(response.content.decode("UTF-8"))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(content['email'], ['Enter a valid email address.'])

    def test_register_less_password(self):
        """This is user registration test with short password
        """
        response = self.client.post(reverse(self.register_user_url), data=self.register_user_7)
        content = ast.literal_eval(response.content.decode("UTF-8"))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(content['detail'], PasswordLengthException().detail)

    def test_register_invalid_password(self):
        """This is user registration test with invalid password
        """
        response = self.client.post(reverse(self.register_user_url), data=self.register_user_8)
        content = ast.literal_eval(response.content.decode("UTF-8"))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(content['detail'], PasswordCharacterValidationException().detail)

    def test_register_existing_username(self):
        """This is user registration test with username already exists
        """
        response = self.client.post(reverse(self.register_user_url), data=self.register_user_9)
        content = ast.literal_eval(response.content.decode("UTF-8"))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(content['username'], ['user with this username already exists.'])

    def test_register_existing_email(self):
        """This is user registration test with email already exists
        """
        response = self.client.post(reverse(self.register_user_url), data=self.register_user_10)
        content = ast.literal_eval(response.content.decode("UTF-8"))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(content['email'], ['user with this email already exists.'])

    def test_register_valid_data(self):
        """This is user registration test with valid data
        """
        response = self.client.post(reverse(self.register_user_url), data=self.register_user_11)
        content = ast.literal_eval(response.content.decode("UTF-8"))
        print(content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.filter(username=self.register_user_11['username']).count(), 1)
        self.assertEqual(content['message'], f"User {self.register_user_11['username']} created successfully")

    def test_login_empty_username(self):
        """This is user login test with empty username
        """
        response = self.client.post(reverse(self.login_user_url), data=self.login_user_1)
        content = ast.literal_eval(response.content.decode("UTF-8"))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(content['username'], ['This field may not be blank.'])

    def test_login_empty_password(self):
        """This is user login test with empty password
        """
        response = self.client.post(reverse(self.login_user_url), data=self.login_user_2)
        content = ast.literal_eval(response.content.decode("UTF-8"))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(content['password'], ['This field may not be blank.'])

    def test_login_wrong_username(self):
        """This is user login test with wrong username
        """
        response = self.client.post(reverse(self.login_user_url), data=self.login_user_3)
        content = ast.literal_eval(response.content.decode("UTF-8"))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(content['detail'], UsernameDidNotExistsException().detail)

    def test_login_wrong_password(self):
        """This is user login test with wrong password
        """
        response = self.client.post(reverse(self.login_user_url), data=self.login_user_4)
        content = ast.literal_eval(response.content.decode("UTF-8"))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(content['detail'], PasswordDidNotExistsException().detail)

    def test_login_valid_data(self):
        """This is user login test with valid data
        """
        response = self.client.post(reverse(self.login_user_url), data=self.login_user_5)
        content = ast.literal_eval(response.content.decode("UTF-8"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual('access' in content, True)
        self.assertEqual('refresh' in content, True)
