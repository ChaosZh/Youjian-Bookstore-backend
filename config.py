# @Time     : 2020/5/21 15:15
# @Author   : Chao Zheng
# @Email    : chaoszh@foxmail.com
import os
from datetime import timedelta


class Config(object):
    SECRET_KEY = os.urandom(24)
    PERMANENT_SESSION_LIFETIME = timedelta(hours=1)
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@47.101.53.252:3306/web_store'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
