#!/usr/bin/env python3
from flask import request
from typing import List, TypeVar


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for a given path.
        Currently, this always returns False, as `path` and `excluded_paths`
        will be used later for more specific behavior.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the authorization header from the Flask request object.
        Currently returns None, will be implemented later.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current user based on the Flask request object.
        Currently returns None, implementation to be added later.
        """
        return None
