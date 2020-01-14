import os

# --->> 全局配置
BASE_URL = os.path.abspath(os.getcwd())  # 项目根目录


# --->> APP配置
class Config:
    SECRET_KEY = os.environ.get("SECREET_KEY") or "1234567890"
    JSON_AS_ASCII = False  # 支持中文


config = {"default": Config}