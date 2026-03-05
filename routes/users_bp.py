from flask import Blueprint, request
from models.user import User
from extensions import db
from sqlalchemy import select

users_bp = Blueprint("users_bp",__name__)

# SCREAMING_SNAKE_CASE
HTTP_NOT_FOUND = 404
HTTP_SERVER_ERROR = 500
HTTP_USER_ERROR = 400



@users_bp.post("/signup")
def Users_signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    signup = select(User).where(User.username == username)
    db_userdata = db.session.execute(signup).scalars().all()

    if db_userdata:
        return {"message" : "user already exist"},HTTP_USER_ERROR

    db_users = User(
        username = username,
        password = password  
    )

    try:
        db.session.add(db_users)
        db.session.commit()
    except Exception as err:
        db.session.rollback()
        return{"message": str(err)},HTTP_SERVER_ERROR
    return{"data":db_users.to_dict(),"message":"login successfully"}
        
