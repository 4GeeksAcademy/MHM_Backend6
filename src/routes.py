import os  
from flask import Flask ,request, jsonify, Blueprint 
# from flask_jwt_extended import create_access_token, get_jwt_identify, jwt_required 
from models import db, User, MentalHealthResources, MeditationSessions

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
    
@api.route('/login', methods=['POST'])
def login():
    email = request.json.get("email")
    password = request.json.get("password")

    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return jsonify({"message": "Incorrect email or password"}), 401

    return jsonify({"message": "You have successfully logged in."}), 200

    
#         access_token = create_access_token(identify=email)
#         return jsonify(access_token=access_token)

@api.route('/logout', methods=['POST', 'GET'])
def logout():
    return jsonify(message='User logged out successfully'), 200

# @api.route('/protected', methods=['GET'])
# @jwt_required()
# def protected():
#     current_user_id = get_jwt_identify()
#     user = User.query.get(current_user_id)

#     return jsonify({"id": id,"email": user.email}), 200

@api.route('/resource', methods=['GET'])
def resource():
    get_resource=request.get_json()
    title=get_resource["title"]
    description=get_resource["description"]
    type=get_resource["type"]
    url=get_resource["url"]
    resource=MentalHealthResources.query.filter_by(title=title).first()

    new_resource=MentalHealthResources(title=get_resource["title"])
                                       
    db.session.add(new_resource)
    db.session.commit()
    return jsonify(message='Your resource is ready.'), 200

@api.route('/meditation', methods=['GET'])
def meditation():
    get_session=request.get_json()
    title=get_session["title"]
    style=get_session["style"]
    theme=get_session["theme"]
    youtube_url=get_session["youtube_url"]
    meditation=MeditationSessions.query.filter_by(title=title).first()

    new_session=MeditationSessions(title=get_session["title"])
                                       
    db.session.add(new_session)
    db.session.commit()
    return jsonify(message='Your session is ready.'), 200

# @api.route('/journal', methods=['POST'])
# def journal_entries():
#     get_entry = request.get_json()
#     mood = get_entry["mood"]
#     content = get_entry["content"]

#     new_entry = JournalEntries(mood=mood, content=content)

#     db.session.add(new_entry)
#     db.session.commit()
#     return jsonify(message='Your new entry is available'), 200