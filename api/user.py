# @Time     : 2020/5/21 15:25
# @Author   : Chao Zheng
# @Email    : chaoszh@foxmail.com

import sys
from flask import Blueprint, request
from flask import session
from api.util.response import SuccessResponse, FailureResponse
from database import sql

users = Blueprint(name = 'users', import_name = __name__,  url_prefix='/user')

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
    res={
        'id': user.id,
        'name': user.name
    }
    # print(type(session))
    # session.__setitem__('key','value')
    # session.__getitem__('key')
    return SuccessResponse(data=res)

@users.route('/logout', methods=['POST'])
def user_logout():
    if session.get('user_id'):
        session.pop('user_id')
        return SuccessResponse()
    else:
        return FailureResponse(data="用户未登录。")

