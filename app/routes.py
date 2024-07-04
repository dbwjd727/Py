from flask import Blueprint, jsonify
from app.services import UserService

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "hello world!!!!!!!"

@main.route('/usernames')
def users():
    usernames = UserService.get_all_usernames()
    userId = UserService.get_all_userId()
    return jsonify(usernames, userId)

    

