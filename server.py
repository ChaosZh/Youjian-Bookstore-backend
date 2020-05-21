# @Time     : 2020/5/21 14:35
# @Author   : Chao Zheng
# @Email    : chaoszh@foxmail.com

from flask import Flask
from config import Config
from api import register_blueprint

def createApp():
    app = Flask(__name__)
    # 添加config信息
    app.config.from_object(Config())
    # 添加蓝图
    register_blueprint(app)

    return app

if __name__ == "__main__":
    app = createApp()
    app.run(debug=True)