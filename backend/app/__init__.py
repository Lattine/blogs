from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from setting import config

db = SQLAlchemy()  # 数据库插件
migrate = Migrate()  # 数据库迁移管理工具插件


def create_app(name="default"):
    app = Flask(__name__)
    app.config.from_object(config[name])

    CORS(app)  # 允许CORS跨域请求
    db.init_app(app)  # 初始化数据库
    migrate.init_app(app, db)  # 初始化数据库管理工具

    # 注册 Blueprint
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix="/api")

    return app


from app import models  #　在尾部导入，防止循环引用
