from src import db
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    address = db.Column(db.String(100), nullable=False)
    phone =  db.Column(db.String(13), nullable=False)
    event = db.relationship('Event',backref='user', cascade="all, delete-orphan", lazy='dynamic')
    order = db.relationship('Order',backref='user', cascade="all, delete-orphan", lazy='dynamic')
    
    
    def set_pass(self, passw):
        self.password = generate_password_hash(passw)

    def check_pass(self, passw):
        return check_password_hash(self.password, passw)

  