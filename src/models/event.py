from src import db
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


class Event(db.Model):

    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    owner_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String, nullable=False)
    tickettypes = db.relationship('Tickettype',backref='events', cascade="all, delete-orphan", lazy='dynamic')
    address = db.Column(db.String(200), nullable=False)
    datetimestart = db.Column(db.DateTime, nullable=False)
    datetimeend = db.Column(db.DateTime)
    views = db.Column(db.Integer, default = 0)
    created = db.Column(db.DateTime, nullable=False)
    updated = db.Column(db.DateTime)
    