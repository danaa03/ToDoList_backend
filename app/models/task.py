from app.extensions import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.Text, nullable = False)
    completed = db.Column(db.Boolean, default=False)