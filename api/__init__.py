# @Time     : 2020/5/21 15:15
# @Author   : Chao Zheng
# @Email    : chaoszh@foxmail.com

from api.user import users
from api.item import items
from api.cart import carts
from api.order import orders

def register_blueprint(app):
    app.register_blueprint(users)
    app.register_blueprint(items)
    app.register_blueprint(carts)
    app.register_blueprint(orders)
    return app