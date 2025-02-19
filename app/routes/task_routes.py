from flask import Blueprint, jsonify, request
from app.models.task import Task
from app.extensions import db

task_bp = Blueprint("tasks", __name__)

@task_bp.route("/", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{"id": task.id, "title": task.title, "completed": task.completed} for task in tasks])

@task_bp.route("/add-task", methods=["POST"])
def add_task():
    data = request.json
    new_task = Task(title=data["title"])
    db.session.add(new_task)
    db.session.commit()
    
    return jsonify({"message": "Task added successfully!", "task": {"id": new_task.id, "title": new_task.title, "completed": new_task.completed}})

@task_bp.route("/api", methods = ['GET'])
def hello():
    return jsonify({"message": "HI!"})