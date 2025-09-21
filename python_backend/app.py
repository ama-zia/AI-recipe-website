import os


from flask import Flask, jsonify, redirect, url_for
from flask_cors import CORS
from flask_login import LoginManager
from python_backend.models import db, User
from python_backend.auth.auth import auth_bp
from python_backend.api.api import api_bp
from python_backend.routes.main import main_bp

def create_app(test_config=None):
    app = Flask(__name__)
    CORS(app)
    
    app.config['SECRET_KEY'] = 'your-very-secure-secret-key-that-is-long-and-random'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in
        app.config.update(test_config)

    with app.app_context():
        db.init_app(app)
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth_bp.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(main_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    try:
        app.run(debug=True)
    except KeyboardInterrupt:
        print("\n🚦 Server stopped by user.")
