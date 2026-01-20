from flask import Flask


def create_app():
    app = Flask(__name__)

    from .routes import calc_bp

    app.register_blueprint(calc_bp)

    return app
