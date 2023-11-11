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
            path = path.rstrip('/') + '/'
            temp = []
            for i in excluded_paths:
                i = i.rstrip('/') + '/'
                temp.append(i)
            if path in temp:
                return False
            else:
                return True
        return True

    def authorization_header(self, request=None) -> str:
        """
        authorization header contents
        """
        if request is None:
            return None
        auth_header = request.headers.get('Authorization')
        if auth_header:
            return auth_header
        else:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        current authentication
        """
        return None
