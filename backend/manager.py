from app import create_app
from flask_migrate import MigrateCommand
from flask_script import Manager

app = create_app()

manager = Manager(app)  # 初始化管理器
manager.add_command('db', MigrateCommand)  # 添加db命令，并与MigrateCommand绑定

if __name__ == "__main__":
    manager.run()

# python manage.py db init 创建迁移存储库
# python manage.py db migrate 生成迁移脚本
# python manage.py db upgrade 将迁移脚本应用到数据库中
# python manage.py db --help