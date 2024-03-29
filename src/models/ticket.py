from src import db
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


class Ticket(db.Model):

    __tablename__ = 'tickets'

    id = db.Column(db.Integer, primary_key=True)
    type_id = db.Column(db.Integer,db.ForeignKey('tickettypes.id'))
    order_id = db.Column(db.Integer,db.ForeignKey('orders.id'))
    UUID = db.Column(db.Integer,nullable = False)
    created = db.Column(db.DateTime, nullable=False)
    redeemed = db.Column(db.String)