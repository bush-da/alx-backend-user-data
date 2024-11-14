#!/usr/bin/env python3
"""Manage the API authentication"""
from flask import request


class Auth():
    """Authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Return false"""
        return False

    def authorization_header(self, request=None) -> str:
        """Authorization header"""
        return None
    def current_user(self, request=None) -> TypeVar('User'):
        """current user"""
        return None
