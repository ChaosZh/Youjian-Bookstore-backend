# @Time     : 2020/5/21 20:41
# @Author   : Chao Zheng
# @Email    : chaoszh@foxmail.com

from database import db

class User(db.Model):
    __tablename__='user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    passwd = db.Column(db.String(50), nullable=False)

    def __init__(self, name, passwd):
        self.name=name
        self.passwd=passwd
        return