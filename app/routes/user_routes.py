from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.models.user import User
from app.extensions import db
from sqlalchemy.exc import IntegrityError

user_bp = Blueprint("users", __name__)

@user_bp.route("/", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([{"id": user.id, "email": user.email, "password": user.password} for user in users])

@user_bp.route("/add-user", methods=["POST"])
def add_user():
    data = request.json
    if not data.get("email") or not data.get("password"):
        return jsonify({"message": "Email and password are required"}), 400

    existing_user = User.query.filter_by(email=data["email"]).first()
    if existing_user:
        return jsonify({"message": "Error: Email already exists!"}), 400

    try:
        new_user = User(email=data["email"])
        new_user.set_password(data["password"])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User added successfully!", "user": {"id": new_user.id, "email": new_user.email}})
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "An error occurred", "error": str(e)}), 500

@user_bp.route("/login", methods = ['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data["email"]).first()
    if not user:
        return jsonify({"message": "User not found"}), 404
    if not user.check_password(data["password"]):
        return jsonify({"message": "Invalid password"}), 400
    
    access_token = create_access_token(identity = str(user.id))
    return jsonify({"message": "Login successful!", "access_token": access_token})

@user_bp.route("/protected", methods = ['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as = current_user), 200