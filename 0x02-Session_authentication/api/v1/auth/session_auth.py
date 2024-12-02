#!/usr/bin/env python3
"""This module defines a class the will be used for session auth
"""
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """Defines session based auth
    """

    user_id_by_session_id = dict()

    def create_session(self, user_id: str = None) -> str:
        """method creates a session id for user with uuid4
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
