from flask import Blueprint, jsonify, request
from .models import User
from .db import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return 'Hello, World!'

@bp.route('/users')
def users():
    users = User.query.all()
    user_list = [{'id':user.id, 'username':user.name} for user in users]
    return jsonify(user_list)


# @bp.route('/users', methods=['GET'])
# def get_users():
#     users = User.query.all()
#     return jsonify([user.as_dict() for user in users])

# @bp.route('/user', methods=['POST'])
# def add_user():
#     data = request.get_json()
#     new_user = User(name=data['name'], email=data['email'], age=data['age'])
#     db.session.add(new_user)
#     db.session.commit()
#     return jsonify(new_user.as_dict()), 201

# @bp.route('/user/<int:id>', methods=['PUT'])
# def update_user(id):
#     data = request.get_json()
#     user = User.query.get_or_404(id)
#     user.name = data['name']
#     user.email = data['email']
#     user.age = data['age']
#     db.session.commit()
#     return jsonify(user.as_dict())

# @bp.route('/user/<int:id>', methods=['DELETE'])
# def delete_user(id):
#     user = User.query.get_or_404(id)
#     db.session.delete(user)
#     db.session.commit()
#     return '', 204
