# -*- coding: utf-8 -*-


# @Time     : 19-11-14
# @Author   : Lattine

# =======================
from sanic import Sanic, response
from sanic_jwt import Initialize, protected, exceptions
from backend.dao import Users


# ----------- Common Methods for JWT --------------
async def authenticate(request, *args, **kwargs):
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if not username or not password:
        raise exceptions.AuthenticationFailed()
    user = Users.select().where(username == username, password == password)
    if not user:
        raise exceptions.AuthenticationFailed()
    return user


# --------------- Main process --------------
app = Sanic("blogs")
Initialize(app, authenticate=authenticate)


@app.route("/")
async def index(request):
    return response.json({"host": request.host})


@app.route("/sc")
@protected()
async def sc(request):
    return response.json({"host": request.host, "msg": "secret!"})


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000)
