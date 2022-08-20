from crypt import methods
from flask import Blueprint, request, jsonify

API = Blueprint("FFAPI", __name__)


@API.route('/login', methods = ['POST'])
def login():
    email = request.json["email"]
    password = request.json["password"]