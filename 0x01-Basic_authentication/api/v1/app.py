#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None

if getenv("AUTH_TYPE") == "basic_auth":
    """if auth type is basic auth then create instance"""
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
else:
    """if auth type don't set or other type
    """
    from api.av1.auth.auth import Auth
    auth = Auth()


@app.before_request
def before_request():
    """check the request before any other action taken"""
    if auth is None:
        return

    paths = ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']

    if auth.require_auth(request.path, paths):
        """check if the request requre auth or not"""
        if auth.authorization_header(request) is None:
            """check request header if there is auth if not
            return unauthorized"""
            abort(401)

        if auth.current_user(request) is None:
            """if user not exist on authorized list return forbidden"""
            abort(403)


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """Unauthorized
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbid(error) -> str:
    """Forbidden
    """
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port, debug=True)
