#!/usr/bin/env python3
"""
Basic auth module for the API
"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    Basic Authentication that inherit base Auth class
    """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """method that extract base64 encoded content from authorization header
        """
        if authorization_header == None or type(authorization_header) != str:
            return None
        checker = authorization_header.split(' ')
        if checker[0] != "Basic":
            return None
        return checker[1]
