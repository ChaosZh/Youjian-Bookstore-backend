from database.model.user import User
from database.model.book import Book
from database.model.cart import Cart
from database.model.order import Order
from database import db
import json

def add_user(name, passwd):
    user = User(name, passwd)
    db.session.add(user)
    db.session.commit()
    return

def get_user(name, passwd):
    user = User.query.filter_by(name=name, passwd=passwd).first()
    return user

def get_book(id):
    book = Book.query.filter_by(id=id).all()
    return book

def get_books(book_class):
    books = Book.query.filter_by(book_class=book_class).all()
    return books

def add_cart(book_id, user_id, number):
    cart = Cart(book_id, user_id, number)
    db.session.add(cart)
    db.commit()
    return

def remove_cart(book_id, user_id):
    cart = Cart.query.filter_by(book_id=book_id, user_id=user_id).first()
    db.session.remove(cart)
    db.commit()
    return

def get_order(id):
    order = Order.query.filter_by(id=id).first()
    return order

def get_orders(user_id):
    orders = Order.query.filter_by(user_id=user_id).all()
    return orders

def add_order(id, user_id, books):
    book_json = json.dumps(books)
    order = Order(id, user_id, book_json)
    db.session.add(order)
    db.commit()
    return

def remove_order(id):
    order = Order.query.filter_by(id=id).first()
    db.session.remove(order)
    db.commit()
    return
