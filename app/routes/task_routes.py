from flask import Blueprint, jsonify, request
from app.models.task import Task
from app.extensions import db
from app.models.user import User
from flask_jwt_extended import jwt_required, get_jwt_identity

task_bp = Blueprint("tasks", __name__)

@task_bp.route("/", methods=["GET"])
@jwt_required()
def get_tasks():
    current_user = get_jwt_identity()
    tasks = db.session.query(Task).filter(Task.user_id == current_user).all()
    return jsonify([{"id": task.id, "title": task.title, "completed": task.completed, "user_id": task.user_id} for task in tasks])

@task_bp.route("/add-task", methods=["POST"])
@jwt_required()
def add_task():
    current_user = get_jwt_identity()
    data = request.json
    user_id = current_user
    title = data.get("title")

    if not title:
        return jsonify({"message": "Task Title is required"}), 400
    
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    new_task = Task(title=title, user_id=user_id)
    db.session.add(new_task)
    db.session.commit()

    return jsonify({"message": "Task added successfully!", "task": {"id": new_task.id, "title": new_task.title, "user_id": new_task.user_id}})

@task_bp.route("/delete-task", methods=["POST"])
@jwt_required()
def delete_task():
    current_user = get_jwt_identity()
    data = request.json
    user_id = current_user
    title = data.get("title")

    if not title:
        return jsonify({"message": "Task Title is required"}), 400
    
    if not user_id:
        return jsonify({"message": "User is required"}), 400
    

    record_to_delete = db.session.query(Task).filter_by(title=title).first()
    if not record_to_delete:
        return jsonify({"message": "Task not found"}), 404
    db.session.delete(record_to_delete)
    db.session.commit()

    return jsonify({"message": "Task deleted successfully!"})