
from src import db
from datetime import datetime


class Order(db.Model):

    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    total_bill = db.Column(db.Integer,nullable=False)
    total_items = db.Column(db.Integer,nullable=False)
    date_add = db.Column(db.String)
    ticket = db.relationship('Ticket', backref='orders', cascade="all, delete-orphan", lazy='dynamic')