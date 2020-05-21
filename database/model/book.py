# @Time     : 2020/5/21 20:44
# @Author   : Chao Zheng
# @Email    : chaoszh@foxmail.com

from database import db

class Book(db.Model):
    __tablename__='book'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    author = db.Column(db.String(15))
    book_class = db.Column(db.String(20))
    price_a = db.Column(db.Float)
    price_b = db.Column(db.Float)
    description = db.Column(db.String(300))
    img = db.Column(db.String(200))
