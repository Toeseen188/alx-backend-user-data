#!/usr/bin/env python3
"""
Basic Authentication
"""
from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """
        extract and decode token from base64
        """
        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            # try decoding to base64 byte
            decoded_bytes = base64.b64decode(base64_authorization_header)

            # convert bytes to string
            decoded_string = decoded_bytes.decode('utf-8')
            return decoded_string
        except Exception as e:
            return None
