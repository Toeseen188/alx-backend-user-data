#!/usr/bin/env python3
"""
Basic Authentication
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ This class inherit from class Auth
    """
    pass

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        extract the string after 'Basic' in the authorization header
        """
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith('Basic '):
            return None

        token = authorization_header[len('Basic '):].strip()
        return token
