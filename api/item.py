# @Time     : 2020/5/21 15:25
# @Author   : Chao Zheng
# @Email    : chaoszh@foxmail.com

from flask import Blueprint
from api.util.response import SuccessResponse, FailureResponse
from database import sql

items = Blueprint(name = 'items', import_name = __name__,  url_prefix='/item')

@items.route('/<int:id>', methods=['GET'])
def get_item(id):
    book = sql.get_book(id)[0]
    res = {
        'id': book.id,
        'name': book.name,
        'author': book.author,
        'book_class': book.book_class,
        'price_a': book.price_a,
        'price_b': book.price_b,
        'description': book.description,
        'img': book.img
    }
    return SuccessResponse(data=res)

@items.route('/class/<string:book_class>', methods=['GET'])
def get_items(book_class):
    books = sql.get_books(book_class)
    res = []
    for book in books:
        r = {
            'id': book.id,
            'name': book.name,
            'author': book.author,
            'book_class': book.book_class,
            'price_a': book.price_a,
            'price_b': book.price_b,
            'description': book.description,
            'img': book.img
        }
        res.append(r)
    return SuccessResponse(data=res)