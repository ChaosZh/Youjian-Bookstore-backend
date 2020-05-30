# @Time     : 2020/5/21 18:23
# @Author   : Chao Zheng
# @Email    : chaoszh@foxmail.com

from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

def connect_to_mysql(app):
    db.init_app(app)
    app.app_context().push()