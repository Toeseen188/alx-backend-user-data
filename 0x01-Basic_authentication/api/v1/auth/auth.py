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
        if path is not None and excluded_paths is not None or []:
            path = path.rstrip('/')
            for i in excluded_paths:
                excluded_paths = i.rstrip('/')
            if path in excluded_paths:
                return False
        return True

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
