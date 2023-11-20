#!/usr/bin/env python3
"""
session Authorization
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """ THe session class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        that creates a Session ID for a user_id:
        Return:
         - None if user_id is None
         - None if user_id is not a string
        Otherwise:
         - Generate a Session ID using uuid module and uuid4() like id in Base
        Return:
         - the Session ID
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = uuid.uuid4()
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Return:
         - None if session_id is None
         - None if session_id is not a string
        Return:
         - the value (the User ID) for the key session_id in the dictionary user_id_by_session_id.
         """
        if session_id is None or not isinstance(session_id, str):
            return None
        value = self.user_id_by_session_id.get(session_id)
        return value
