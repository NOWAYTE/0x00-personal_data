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
        if not path:
            return True
        if not excluded_paths:
            return True
        path = path if path.endswith('/') else path + '/'

        for e_path in excluded_paths:
            e_path = e_path if e_path.endswith('/') else e_path + '/'

            if path == excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Returns authorization header value
        """
        return request

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns current User
        """
        return request
