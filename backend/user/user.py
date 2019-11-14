# -*- coding: utf-8 -*-


# @Time     : 19-11-14
# @Author   : Lattine

# =======================
from sanic import response
from sanic import Blueprint

usr = Blueprint("user", url_prefix="user")


@usr.route("/login")
async def login(request):
    return response.json({"msg": "success"})
