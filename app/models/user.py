from app.extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.Text, nullable = False)
    password = db.Column(db.Text, nullable = False)
    tasks = db.relationship('Task', backref='user', lazy=True)
