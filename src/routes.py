import os  
from flask import Flask ,request, jsonify, Blueprint 
# from flask_jwt_extended import create_access_token, get_jwt_identify, jew_required 
# from flask_jwt_extended import JWTManager  
from models import db, User
# from utils import APIException

api = Blueprint('api', __name__)

@api.route('/signup', methods=['POST'])
def signup():
    rb=request.get_json()
    email = rb["email"]
    password = rb["password"]
    user=User.query.filter_by(email=email).first()

    if user:

        return jsonify(message='Email already registered'), 200

    new_user = User(email=rb["email"], password=rb["password"], is_active=True)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify(message='User register successfully'), 200
    except Exception as e:
        db.session.rollback()
        return jsonify(message=e), 200
    
@api.route('login', methods=['POST'])
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    user = User.query.filter_by(email=email).first()
    if user is None or not user.check_password(password):
        return jsonify({"msg": "Incorrect email or password"}, 401)

    return jsonify(message='You have successfully logged in.')

@api.route('logout', methods=['POST','GET'])
def logout():
    return jsonify(message='You have successfully logged out.')
    
# @api.route('/login', methods=['POST'])
# def login():
#     email = request.json.get("email", None)
#     password = request.json.get("password", None)

    # user = User.query.filter_by(email=email),first()
    # if user is None or not user.check_password(password):
    #     return jsonify({"msg": "Incorrect email or password"}, 401)

#         access_token = create_access_token(identify=email)
#         return jsonify(access_token=access_token)

# @api.route('/logout', methods=['POST, GET'])
# def logout():
#     return jsonify(message='User logged out successfully'), 200

# @api.route('/protected', methods=[GET])
# @jwt_required()
# def protected():
#     current_user_id = get_jwt_identify()
#     user = User.query.get(current_user_id)

#     return jsonify({"id": id,"username": user.username}), 200