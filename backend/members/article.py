# -*- coding: utf-8 -*-


# @Time     : 19-11-20
# @Author   : Lattine

# =======================
from sanic import Blueprint
from sanic import response
from backend.dao import Article

article = Blueprint("article", url_prefix="/article")


@article.route("/<id:int>", methods=["OPTIONS", "GET"])
async def get(request, id):
    return response.json({"id": id})


@article.route("/save", methods=["OPTIONS", "POST"])
async def save(request):
    print(request.json)
    return response.json({"msg": "saved"})
