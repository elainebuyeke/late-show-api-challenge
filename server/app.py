from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from .config import Config
from .models import db
from .controllers.auth_controller import auth_bp
from .controllers.guest_controller import guest_bp
from .controllers.episode_controller import episode_bp
from .controllers.appearance_controller import appearance_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)
    JWTManager(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(guest_bp)
    app.register_blueprint(episode_bp)
    app.register_blueprint(appearance_bp)

    @app.route('/')
    def index():
        return {'message': 'Late Show API is running!'}

    return app 