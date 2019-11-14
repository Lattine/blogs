# -*- coding: utf-8 -*-


# @Time     : 19-11-14
# @Author   : Lattine

# =======================
from sanic import Sanic
from sanic import response

from backend.user.user import usr

app = Sanic("blogs")

app.blueprint(usr)


@app.route("/")
async def index(request):
    return response.json({"host": request.host})


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000)
