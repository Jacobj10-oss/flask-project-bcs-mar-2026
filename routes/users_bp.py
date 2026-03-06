from flask import Blueprint, request
from models.user import User
from extensions import db
from sqlalchemy import select
from werkzeug.security import generate_password_hash, check_password_hash

users_bp = Blueprint("users_bp",__name__)

# SCREAMING_SNAKE_CASE
HTTP_NOT_FOUND = 404
HTTP_SERVER_ERROR = 500
HTTP_USER_ERROR = 400
HTTP_CREATED = 201



@users_bp.post("/signup")
def Users_signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    signup = select(User).where(User.username == username)
    db_userdata = db.session.execute(signup).scalars().all()

    if db_userdata:
        return {"message" : "user already exist"},HTTP_USER_ERROR

    try:
        new_user = User(username = username, password =generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()
    except Exception as err:
        db.session.rollback()
        return{"message": str(err)},HTTP_SERVER_ERROR
    return{"data":{"id":new_user.id,"username" : new_user.username},"message":"Signup successfully"},HTTP_CREATED
        
@users_bp.post("/login")
def Users_login():
    login_data = request.get_json()
    username = login_data.get('username')
    password = login_data.get('password')

    login_user = select(User).where(User.username == username)
    db_logindata = db.session.execute(login_user).scalar_one_or_none()

    if not db_logindata:
        return {"Error" : "Invalid Credentials"},HTTP_USER_ERROR
    
    if not check_password_hash(db_logindata.password,password):
        return {"Error" : "Invalid Credentials"},HTTP_USER_ERROR
    
    return{"message":"login successfully"}