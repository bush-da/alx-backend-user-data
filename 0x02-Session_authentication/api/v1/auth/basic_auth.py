#!/usr/bin/env python3
"""
Basic auth module for the API
"""
from flask import request
from models.base import Base
from models.user import User
from typing import List, TypeVar
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """
    Basic Authentication that inherit base Auth class
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Method that extract base64 encoded content from authorization header
        """
        if authorization_header is None or not isinstance(authorization_header,
                                                          str):
            return None
        checker = authorization_header.split(' ')
        if checker[0] != "Basic":
            return None
        return checker[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """Method that decode base64 encoded content from authorization header
        """
        try:
            decoded_content = base64.b64decode(base64_authorization_header)
            return decoded_content.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> str:
        """Extract username and email from decoded base64 content
        """
        short_version = decoded_base64_authorization_header
        if short_version is None or not isinstance(short_version, str):
            return (None, None)

        if ":" not in short_version:
            return (None, None)

        username, password = short_version.split(':', 1)
        return (username, password)

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """Get user from db or file then check the credentials of the
        user email and password and return user object
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        user = User()
        check_users_exist = user.count()
        if check_users_exist == 0:
            return None
        user = user.search({"email": user_email})
        # now user is a list of len 1 because .search method returns list
        if user:
            # get user object from user list
            user = user[0]
            check_pass = user.is_valid_password(user_pwd)
            if not check_pass:
                return None
            return user

    def current_user(self, request=None) -> TypeVar('User'):
        """Method that overload the super class Auth that get together
        all the pieces for Basic Authentication of API
        """
        header = self.authorization_header(request)
        base64_content = self.extract_base64_authorization_header(header)
        decoded_conte = self.decode_base64_authorization_header(base64_content)
        username, password = self.extract_user_credentials(decoded_conte)
        user = self.user_object_from_credentials(username, password)
        return user
