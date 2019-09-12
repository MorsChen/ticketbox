from src import db
from datetime import datetime


class Post(db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    body = db.Column(db.String, nullable=False)
    author = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created = db.Column(db.DateTime, nullable=False)
    updated = db.Column(db.DateTime)
    comments = db.relationship('Comments', backref='posts', cascade="all, delete-orphan", lazy='dynamic')
    views = db.Column(db.Integer, default = 0)
    flags = db.relationship('Flag', backref='posts',cascade="all, delete-orphan", lazy='dynamic')