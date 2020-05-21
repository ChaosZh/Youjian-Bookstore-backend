# @Time     : 2020/5/21 15:25
# @Author   : Chao Zheng
# @Email    : chaoszh@foxmail.com

from flask import Blueprint, request
from api.util.response import SuccessResponse, FailureResponse
from database import sql

carts = Blueprint("carts", __name__,  url_prefix='/cart')

@carts.route('/add', methods = ['POST'])
def cart_add():
    data = request.json
    sql.add_cart(data['book_id'], data['user_id'], data['number'])
    return SuccessResponse()


@carts.route('/remove', methods = ['POST'])
def cart_remove():
    data = request.json
    sql.remove_cart(data['book_id'], data['user_id'])
    return SuccessResponse()


