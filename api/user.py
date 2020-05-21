# @Time     : 2020/5/21 15:25
# @Author   : Chao Zheng
# @Email    : chaoszh@foxmail.com

import sys

from flask import Blueprint

users = Blueprint(name = 'users', import_name = __name__,  url_prefix='/user')

@users.route('/register', methods=['POST'])
def user_register():
    return ('%s'%sys._getframe().f_code.co_name)

@users.route('/login', methods=['POST'])
def user_login():
    return ('%s'%sys._getframe().f_code.co_name)

@users.route('/logout', methods=['POST'])
def user_logout():
    return ('%s'%sys._getframe().f_code.co_name)

