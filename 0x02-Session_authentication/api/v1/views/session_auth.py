#!/usr/bin/env python3
"""Flask view that handles all routes for the session auth"""
from flask import request, jsonify, session
from api.v1.views import app_views
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_auth() -> str:
    """create a cookie with session id after user login"""
    email = request.form.get("email")
    password = request.form.get("password")
    if email is None:
        return jsonify({"error": "email missing"}), 400
    if password is None:
        return jsonify({"error": "password missing"}), 400
    user = User()
    user = user.search({"email": email})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404
    user = user[0]
    check = user.is_valid_password(str(password))
    if not check:
        return jsonify({"error": "wrong password"}), 401
    else:
        from api.v1.app import auth
        """create_session method do create session id and
        also add to user_id_by_session_id with key session_id
        that will be generated with value user id and return session id"""
        session_id = auth.create_session(user.id)
        """cookie name from env var then based on the cookie name assign
        the session id and response to user in form of cookie
        """
        session_name = os.getenv("SESSION_NAME", "_my_session_id")
        res = jsonify(user.to_json())
        res.set_cookie(session_name, session_id)
        return res
