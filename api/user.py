# @Time     : 2020/5/21 15:25
# @Author   : Chao Zheng
# @Email    : chaoszh@foxmail.com

import sys
from flask import Blueprint, request, current_app
from api.util.response import SuccessResponse, FailureResponse
from database import sql

users = Blueprint(name = 'users', import_name = __name__,  url_prefix='/user')

@users.route('/test', methods=['GET'])
def test():
    return SuccessResponse(data={"data":"haha"})

@users.route('/register', methods=['POST'])
def user_register():
    name=request.json['name']
    passwd=request.json['passwd']
    sql.add_user(name, passwd)
    return SuccessResponse()

@users.route('/login', methods=['POST'])
def user_login():
    name=request.json['name']
    passwd=request.json['passwd']
    user=sql.get_user(name=name, passwd=passwd)
    if user==None:
        return FailureResponse(data="用户不存在或密码错误")
    res={
        'id': user.id,
        'name': user.name
    }
    return SuccessResponse(data=res)

@users.route('/logout', methods=['POST'])
def user_logout():
    return SuccessResponse(data=None)

