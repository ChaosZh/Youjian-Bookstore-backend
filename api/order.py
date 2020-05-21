# @Time     : 2020/5/21 15:25
# @Author   : Chao Zheng
# @Email    : chaoszh@foxmail.com
import sys

from flask import Blueprint

orders = Blueprint("orders", __name__, url_prefix='/order')

@orders.route('/add', methods=['POST'])
def order_add():
    return ('%s'%sys._getframe().f_code.co_name)

@orders.route('/remove', methods=['DELETE'])
def order_delete():
    return ('%s'%sys._getframe().f_code.co_name)
