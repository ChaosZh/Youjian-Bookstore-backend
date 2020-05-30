# @Time     : 2020/5/21 15:25
# @Author   : Chao Zheng
# @Email    : chaoszh@foxmail.com

from flask import Blueprint, request
from api.util.response import SuccessResponse, FailureResponse
from database import sql
import json

carts = Blueprint("carts", __name__,  url_prefix='/cart')

@carts.route('/<int:id>', methods = ['GET'])
def cart_get(id):
    carts = sql.get_cart(id)
    books=[]
    for b in carts:
        book = sql.get_book(b.book_id)[0]
        books.append({
            'id': book.id,
            'name': book.name,
            'author': book.author,
            'book_class': book.book_class,
            'price_a': book.price_a,
            'price_b': book.price_b,
            'description': book.description,
            'img': book.img,
            'number': b.number
        })
    return SuccessResponse(data=books)

@carts.route('/add', methods = ['POST'])
def cart_add():
    data = request.json
    sql.add_cart(data['book_id'], data['user_id'], data['number'])
    return SuccessResponse()


@carts.route('/remove', methods = ['POST'])
def cart_remove():
    data = request.json
    print(data)
    sql.remove_cart(data['book_id'], data['user_id'])
    return SuccessResponse()

