from flask import Blueprint, jsonify, request
from app.models.user import User
# from app.extensions import db

user_bp = Blueprint("users", __name__)

@user_bp.route("/", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([{"id": user.id, "email": user.email, "password": user.password} for user in users])

@user_bp.route("/add-user", methods=["POST"])
def add_task():
    data = request.json
    new_user = User(email=data["email"], password=data["password"])
    # db.session.add(new_task)
    # db.session.commit()
    
    return jsonify({"message": "User added successfully!", "task": {"id": new_user.id, "email": new_user.email}})
