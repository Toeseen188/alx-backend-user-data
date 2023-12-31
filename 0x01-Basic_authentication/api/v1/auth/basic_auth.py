#!/usr/bin/env python3
"""
Basic Authentication
"""
from flask import request as flask_request, abort
from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


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
            return e

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """
        extract user credentials from authorization header
        Return:
        - user email and password from the 64base decode
        - tuple (str, str)
        """
        if decoded_base64_authorization_header is None:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        email, password = decoded_base64_authorization_header.split(":", 1)

        return email, password

    def user_object_from_credentials(self,
                                     user_email: str, user_pwd:
                                     str) -> TypeVar('User'):
        """
        takes user objs from credentials(email, password)
        Return:
        - User objects
        """
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        # search through saved user object to see if user_email is found
        user_obj = User()
        found_users = user_obj.search({'email': user_email})

        if not found_users:
            return None

        user = found_users[0]

        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """overload Auth and retrieve all the User instances from the request
        """
        # if request is not provided, use flask request
        if request is None:
            request = flask_request

        header = self.authorization_header(request)

        extract = self.extract_base64_authorization_header(header)

        credentials = self.decode_base64_authorization_header(extract)

        if credentials is None:
            return None

        email, password = self.extract_user_credentials(credentials)
        user = self.user_object_from_credentials(email, password)

        if user is None:
            return None

        return user
