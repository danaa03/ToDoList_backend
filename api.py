# from flask import Flask, jsonify
# from flask_sqlalchemy import SQLAlchemy
# # from app import Task

# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.db"
# db = SQLAlchemy(app)

# class Task(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     title = db.Column(db.Text, nullable = False)
#     completed = db.Column(db.Boolean, default=False)

# def task_serializer(task):
#     return {
#         'id': task.id,
#         'title': task.title,
#         'completed': task.completed
#     }

# @app.route('/api', methods = ['GET'])
# def index():
#     return jsonify([*map(task_serializer, Task.query.all())])

# if __name__ == '__main__':
#     app.run(debug=True)