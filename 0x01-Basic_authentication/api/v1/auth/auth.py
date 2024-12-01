#!/usr/bin/env python3
"""
This module defines the Auth class for handling API authentication.
It includes methods to manage authentication requirements for specific
paths, retrieve authorization headers, and determine the current user.
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """
    Auth class to manage API authentication.

    Provides methods to determine if authentication is required for
    specific paths, retrieve authorization headers, and identify
    the current user.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for a given path.
p
        Args:
            path (str): The path to check.
            excluded_paths (List[str]): A list of paths that do not require
            authentication.

        Returns:
            bool: True if authentication is required, False if the path is in
            excluded_paths.

        - Returns True if `path` is None.
        - Returns True if `excluded_paths` is None or empty.
        - The check is slash-tolerant, treating paths with and without a
          trailing slash as equivalent.
        """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if not path.endswith('/'):
            path += '/'

        for excluded in excluded_paths:
            if excluded.endswith('*'):
                if path.startswith(excluded[:-1]):
                    return False
            else:
                if path == excluded:
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the authorization header from the Flask request object.

        Args:
            request (Flask request): The request object.

        Returns:
            str: The value of the Authorization header if present,
                 otherwise None.
        """
        if request is None:
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current user based on the Flask request object.

        Args:
            request (Flask request): The request object.

        Returns:
            TypeVar('User'): The current user, if any. Currently returns None.
        """
        return None
