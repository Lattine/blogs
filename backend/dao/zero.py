# -*- coding: utf-8 -*-


# @Time     : 19-11-20
# @Author   : Lattine

# =======================
from peewee import *
from backend.config import Config
from backend.dao import User, Article

if __name__ == '__main__':

    cfg = Config()
    db = MySQLDatabase(cfg.DB_NAME, user=cfg.DB_USER, password=cfg.DB_PASSWD, host=cfg.DB_IP, port=3306)  # 连接数据库
    try:
        db.create_tables([User, Article])
        print("Tables is created.")
    except Exception as e:
        print(e)
