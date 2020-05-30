# @Time     : 2020/5/21 14:35
# @Author   : Chao Zheng
# @Email    : chaoszh@foxmail.com

from flask import Flask
from flask_cors import CORS
from config import Config
from api import register_blueprint
from database import connect_to_mysql
from auth import register_auth

def createApp(app):
    # 跨域
    CORS(app)
    # 添加config信息
    app.config.from_object(Config())
    # 连接数据库
    connect_to_mysql(app)
    # 添加蓝图
    register_blueprint(app)
    register_auth(app)
    return app


app = Flask(__name__)
app = createApp(app)
app.run(debug=True)