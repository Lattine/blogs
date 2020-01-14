from flask import Blueprint

bp = Blueprint("api", __name__)

from app.api import ping  # 写在Blueprint之后，是避免循环引用
