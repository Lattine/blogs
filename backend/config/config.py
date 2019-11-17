# -*- coding: utf-8 -*-


# @Time     : 19-11-17
# @Author   : Lattine

# =======================

import os


class Config:
    BASE_URL = os.path.abspath(os.path.dirname(os.getcwd()))  # 项目根目录

    # ------- 数据库配置 --------
    DB_NAME = "blogs"
    DB_USER = "root"
    DB_PASSWD = "000000"
    DB_IP = "localhost"
