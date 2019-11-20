# -*- coding: utf-8 -*-


# @Time     : 19-11-20
# @Author   : Lattine

# =======================
import datetime
from sanic import Blueprint
from sanic import response
from backend.dao import Article, User

article = Blueprint("article", url_prefix="/article")


@article.route("/<id:int>", methods=["GET"])
async def get(request, id):
    return response.json({"id": id})


@article.route("/save", methods=["POST"])
async def save(request):
    id = request.json.get("id", None)
    user_id = request.json.get("author", None)
    if user_id is None:
        return response.json({"msg": "your don't has access right!"})
    user = User.get_by_id(user_id)
    props = {
        "title": request.json.get("title", ""),
        "content": request.json.get("content", ""),
        "author": user
    }
    if id is None:
        em = Article(**props)
        em.save()
        return response.json({"msg": "created", "id": em.id})
    else:
        em = Article.get_by_id(id)
        em.title = props['title']
        em.content = props['content']
        em.updated_at = datetime.datetime.now()
        em.save()
        return response.json({"msg": "created"})
