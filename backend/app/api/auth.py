from flask import g
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from app.models import User
from app.api.errors import error_response

basic_auth = HTTPBasicAuth()  # 通过 Basic Auth 验证后，才使用用户模型的 get_token() 方法来生成 token
token_auth = HTTPTokenAuth()  # 通过 Basic Auth 拿到 token 后，之后的请求只要附带这个 token 就能够访问其它 API


@basic_auth.verify_password
def verify_password(username, password):
    """验证用户名和密码"""
    user = User.query.filter_by(username=username).first()
    if user is None:
        return False
    g.current_user = user
    return user.check_password(password)


@token_auth.verify_token
def verify_token(token):
    """用于检查用户请求是否有token、是否在有效期"""
    g.current_user = User.check_token(token) if token else None
    return g.current_user is not None


@basic_auth.error_handler
def basic_auth_error():
    """用于认证失败时的错误相应"""
    return error_response(401)


@token_auth.error_handler
def token_auth_error():
    """用于在token auth认证失败的错误相应"""
    return error_response(401)