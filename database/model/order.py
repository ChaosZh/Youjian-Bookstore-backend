# @Time     : 2020/5/21 20:44
# @Author   : Chao Zheng
# @Email    : chaoszh@foxmail.com

from database import db

class Order(db.Model):
    __tablename__='order'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    book_json = db.Column(db.String(200))

    def __init__(self, id, user_id, book_json):
        self.id = id
        self.user_id = user_id
        self.book_json = book_json
        return