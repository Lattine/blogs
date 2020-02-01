import os


def load_env(path):
    try:
        with open(path, encoding="utf-8") as fr:
            for line in fr:
                ems = line.strip().split("=")
                os.environ[ems[0].strip()] = ems[1].strip()
    except Exception as e:
        print(f"Exception with {e}")


# --->> 全局配置
BASE_URL = os.path.abspath(os.getcwd())  # 项目根目录
load_env(os.path.join(BASE_URL, ".env"))


# --->> APP配置
class Config:
    SECRET_KEY = os.environ.get("SECREET_KEY") or "1234567890"
    JSON_AS_ASCII = False  # 支持中文

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI") or "sqlite:///" + os.path.join(BASE_URL, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {"default": Config}