from flask import Blueprint, request, jsonify
from http import HTTPStatus
from json import loads

from src.validators.userValidator import create_user_validator
from src.validators.validator import validator
from src.users.users import Users


app = Blueprint('users', __name__)

@app.route("/", methods=['POST'])
def create_user():
    data = loads(request.data)
    validator(create_user_validator, data)
    return jsonify(Users().insert(data)), HTTPStatus.CREATED