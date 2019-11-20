# -*- coding: utf-8 -*-


# @Time     : 19-11-14
# @Author   : Lattine

# =======================
from sanic import Sanic, response
from sanic_cors import CORS
from sanic_jwt import Initialize, protected, exceptions
from backend.members import article


# ----------- Common Methods for JWT --------------
async def authenticate(request, *args, **kwargs):
    # username = request.json.get("username", None)
    # password = request.json.get("password", None)
    # if not username or not password:
    #     raise exceptions.AuthenticationFailed()
    # user = Users.select().where(username == username, password == password).get()
    # if not user:
    #     raise exceptions.AuthenticationFailed()
    # return {"id": user.id, "username": user.username}
    return {"id": 0, "username": "test"}


# --------------- Main process --------------
app = Sanic("blogs")
app.blueprint(article)
CORS(app)  # 解决跨域
Initialize(app, authenticate=authenticate)


@app.route("/", methods=["OPTIONS", "GET"])
async def index(request):
    return response.json({"host": request.host})


@app.route("/sc", methods=["OPTIONS", "GET"])
@protected()
async def sc(request):
    return response.json({"host": request.host, "msg": "secret!"})


if __name__ == '__main__':
    # app.run(host="127.0.0.1", port=8000)
    app.run(host="0.0.0.0", port=8000, auto_reload=True)
