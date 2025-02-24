from flask import Flask
from app.extensions import db
from flask_cors import CORS
from app.routes.task_routes import task_bp
from app.routes.user_routes import user_bp
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object("app.config.Config")
    db.init_app(app)
    jwt = JWTManager(app)

    app.register_blueprint(task_bp, url_prefix='/tasks')
    app.register_blueprint(user_bp, url_prefix='/users')

    with app.app_context():
        db.create_all()

    return app