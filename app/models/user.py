from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.Text, nullable = False, unique = True)
    password = db.Column(db.Text, nullable = False)
    tasks = db.relationship('Task', backref='user', lazy=True)

    def set_password(self, xpassword):
        self.password = generate_password_hash(xpassword)

    def check_password(self, xpassword):
        return check_password_hash(self.password, xpassword)