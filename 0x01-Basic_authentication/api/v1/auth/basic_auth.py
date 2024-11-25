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
