import json

from flask import current_app, request, Response, jsonify, render_template
from web import db as webdb
from web.users import users


@users.route('/users', methods= ['POST'])
def register_user():
    """
    Create a new user
    :return:
    """
    resp = jsonify()
    resp.status_code = 201
    return resp
