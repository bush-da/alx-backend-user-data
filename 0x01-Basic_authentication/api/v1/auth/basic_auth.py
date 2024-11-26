#!/usr/bin/env python3
"""
Basic auth module for the API
"""
from flask import request
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

        splited = short_version.split(':')
        return (splited[0], splited[1])
