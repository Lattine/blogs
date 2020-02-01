from flask import g, jsonify
from app import db
from app.api import bp
from app.api.auth import basic_auth, token_auth


@bp.route("/tokens", methods=["POST"])
@basic_auth.login_required  # 通过 Basic Auth 验证后，才使用用户模型的 get_token() 方法来生成 token
def get_token():
    token = g.current_user.get_token()
    # 数据库提交在生成 token 后发出，以确保 token 及其到期时间被写回到数据库
    db.session.commit()
    return jsonify({"token": token})


@bp.route("/tokens", methods=["DELETE"])
@token_auth.login_required
def revoke_token():
    """撤销Token"""
    g.current_user.revoke_token()
    db.session.commit()
    return "", 204