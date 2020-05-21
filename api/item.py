# @Time     : 2020/5/21 15:25
# @Author   : Chao Zheng
# @Email    : chaoszh@foxmail.com

from flask import Blueprint

items = Blueprint(name = 'items', import_name = __name__,  url_prefix='/item')

@items.route('', methods=['GET'])
def item_get_all():
    return "get all items"

@items.route('/<int:id>', methods=['GET'])
def item_get(id):
    return ('get id'+str(id))