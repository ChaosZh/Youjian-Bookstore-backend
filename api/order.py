# @Time     : 2020/5/21 15:25
# @Author   : Chao Zheng
# @Email    : chaoszh@foxmail.com

from flask import Blueprint, request
from api.util.response import SuccessResponse, FailureResponse
from database import sql
import json

orders = Blueprint("orders", __name__, url_prefix='/order')

@orders.route('/add', methods=['POST'])
def order_add():
    data = request.json
    sql.add_order(data['user_id'], json.dumps(data['books']))
    return SuccessResponse()
    

@orders.route('/remove', methods=['DELETE'])
def order_delete():
    data = request.json
    sql.remove_order(data['id'])
    return SuccessResponse()

@orders.route('/<int:user_id>', methods=['GET'])
def order_get(user_id):
    orders = sql.get_orders(user_id)
    res=[]
    for o in orders:
        bs=json.loads(json.loads(o.book_json))
        books=[]
        total_val = 0
        for b in bs:
            book = sql.get_book(b['book_id'])[0]
            book = {
                'id': book.id,
                'name': book.name,
                'author': book.author,
                'book_class': book.book_class,
                'price_a': book.price_a,
                'price_b': book.price_b,
                'description': book.description,
                'img': book.img,
                'number': b['number']
            }
            total_val+=(int)(book['number'])*(float)(book['price_b'])
            books.append(book)
        r = {
            'order_id': o.id,
            'books': books,
            'sum': total_val
        }
        res.append(r)
    return SuccessResponse(data=res)