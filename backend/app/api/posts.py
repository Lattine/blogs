from flask import request, jsonify, url_for, g

from app import db
from app.api import bp
from app.api.auth import token_auth
from app.api.errors import error_response, bad_request
from app.models import Post


@bp.route("/posts", methods=["POST"])
@token_auth.login_required
def create_post():
    """添加一片文章"""

    # 以下是验证数据是否缺失
    data = request.get_json()
    if not data:
        return bad_request("You must post JSON data.")
    message = {}
    if "title" not in data or not data.get("title"):
        message["title"] = "Title is required."
    elif len(data.get("title")) > 255:
        message["title"] = "Title must less than 255 characters."
    if "body" not in data or not data.get("body"):
        message["body"] = "Body is required."
    if message:
        return bad_request(message)

    # 以下将数据存入数据库
    post = Post()
    post.from_dict(data)
    post.author = g.current_user  # 通过auth.py中的verify_token传递（同一个request需要先进行认证）
    db.session.add(post)
    db.session.commit()
    response = jsonify(post.to_dict())
    response.status_code = 201
    # HTTP协议要求201响应包含一个值为新资源URL的Location头部
    response.headers["Location"] = url_for("api.get_post", id=post.id)
    return response


@bp.route("/posts", methods=["GET"])
def get_posts():
    """返回文章集合，分页"""
    page = request.args.get("page", 1, type=int)
    per_page = min(request.args.get("per_page", 10, type=int), 100)
    data = Post.to_collection_dict(Post.query.order_by(Post.timestamp.desc()), page, per_page, "api.get_posts")
    return jsonify(data)


@bp.route("/posts/<int:id>", methods=["GET"])
def get_post(id):
    """返回一篇文章"""
    post = Post.query.get_or_404(id)
    post.views += 1
    # db.session.add(post)  # ??
    db.session.commit()
    return jsonify(post.to_dict())


@bp.route("/posts/<int:id>", methods=["PUT"])
@token_auth.login_required
def update_post(id):
    """修改一篇文章"""
    post = Post.query.get_or_404(id)
    if g.current_user != post.author:  #　非同一人
        return error_response(403)

    # 以下是验证数据是否缺失
    data = request.get_json()
    if not data:
        return bad_request("You must post JSON data.")
    message = {}
    if "title" not in data or data.get("title"):
        message["title"] = "Title is required."
    elif len(data.get("title")) > 255:
        message["title"] = "Title must less than 255 characters."
    if "body" not in data or data.get("body"):
        message["body"] = "Body is required."
    if message:
        return bad_request(message)

    # 以下将数据存入数据库
    post.from_dict(data)
    db.session.commit()
    return jsonify(post.to_dict())


@bp.route("/posts/<int:id>", methods=["DELETE"])
@token_auth.login_required
def delete_post(id):
    """删除一篇文章"""
    post = Post.query.get_or_404(id)
    if g.current_user != post.author:
        return error_response(403)
    db.session.delete(post)
    db.session.commit()
    return "", 204
