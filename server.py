# @Time     : 2020/5/21 14:35
# @Author   : Chao Zheng
# @Email    : chaoszh@foxmail.com

from flask import Flask
from config import Config
from api import register_blueprint
from database import connect_to_mysql

def createApp():
    app = Flask(__name__)
    app.secret_key = "1234"
    # 添加config信息
    app.config.from_object(Config())
    # 连接数据库
    connect_to_mysql(app)
    # 添加蓝图
    register_blueprint(app)
    return app

if __name__ == "__main__":
    app = createApp()
    app.run(debug=True)