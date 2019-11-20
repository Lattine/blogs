# -*- coding: utf-8 -*-


# @Time     : 19-11-20
# @Author   : Lattine

# =======================
import datetime
from peewee import *

from backend.config import Config
from backend.dao import User

cfg = Config()

db = MySQLDatabase(cfg.DB_NAME, user=cfg.DB_USER, password=cfg.DB_PASSWD, host=cfg.DB_IP, port=3306)  # 连接数据库


class BaseModel(Model):
    class Meta:
        database = db


class Article(BaseModel):
    author = ForeignKeyField(User, backref="articles")

    title = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField()
