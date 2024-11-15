#!/usr/bin/env python3
"""
Manage API authentication
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """ Authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Checks path
        """

        return False

    def authorization_header(self, request=None) -> str:
        """ Returns authorization header value
        """
        return request

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns current User
        """
        return request
