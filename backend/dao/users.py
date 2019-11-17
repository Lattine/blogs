# -*- coding: utf-8 -*-


# @Time     : 19-11-17
# @Author   : Lattine

# =======================

from peewee import *
from backend.config import Config

cfg = Config()

db = MySQLDatabase(cfg.DB_NAME, user=cfg.DB_USER, password=cfg.DB_PASSWD, host=cfg.DB_IP, port=3306)  # 连接数据库


class BaseModel(Model):
    class Meta:
        database = db


class Users(BaseModel):
    username = CharField(max_length=50)
    password = CharField()


if __name__ == '__main__':
    try:
        db.create_tables([Users])
        print("Tables is created.")
    except Exception as e:
        print(e)
