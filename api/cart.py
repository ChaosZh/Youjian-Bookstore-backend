# @Time     : 2020/5/21 15:25
# @Author   : Chao Zheng
# @Email    : chaoszh@foxmail.com

import sys
from flask import Blueprint

carts = Blueprint("carts", __name__,  url_prefix='/cart')

@carts.route('/add', methods = ['POST'])
def cart_add():
    return ('%s'%sys._getframe().f_code.co_name)

@carts.route('/remove', methods = ['POST'])
def cart_remove():
    return ('%s'%sys._getframe().f_code.co_name)


