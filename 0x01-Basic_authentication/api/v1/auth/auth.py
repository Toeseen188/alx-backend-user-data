#!/usr/bin/env python3
"""
authentication of user data
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    class struction for all authentication
    """
    pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """check for authentication
        Return:
        - bool
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        authorization header contents
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        current authentication
        """
        return None
