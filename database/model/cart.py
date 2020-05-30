# @Time     : 2020/5/21 20:44
# @Author   : Chao Zheng
# @Email    : chaoszh@foxmail.com

from database import db

class Cart(db.Model):
    __tablename__='cart'
    book_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, default=1)

    def __init__(self, book_id, user_id, number):
        self.book_id=book_id
        self.user_id=user_id
        self.number=number
        return
