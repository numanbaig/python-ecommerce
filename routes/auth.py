from flask import Blueprint, request, jsonify
from app import mongo, bcrypt
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    user = {
        "username": data['username'],
        "email": data['email'],
        "password": hashed_password
    }
    existing_user = mongo.db.users.find_one({"email": data['email']})
    if existing_user:
        return jsonify({'message': 'User already exists'}), 409

    mongo.db.users.insert_one(user)
    return jsonify({'message': 'User registered successfully'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = mongo.db.users.find_one({"email": data['email']})
    if user and bcrypt.check_password_hash(user['password'], data['password']):
        token = create_access_token(identity=str(user['_id']))
        return jsonify({'token': token}), 200
    return jsonify({'message': 'Invalid credentials'}), 401
