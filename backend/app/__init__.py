from flask import Flask
from setting import config


def create_app(name="default"):
    app = Flask(__name__)
    app.config.from_object(config[name])

    # 注册 Blueprint
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix="/api")
    return app