from src import db
from datetime import datetime


class Event(db.Model):

    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    owner_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, default=0)
    address = db.Column(db.String(200), nullable=False)
    time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, name, description, image_url, price, address, time):
        self.name = name
        self.description = description
        self.image_url = image_url
        self.price = price
        self.address = address
        self.time = time

    def __repr__(self):
        return f"{self.id} Event name is {self.name}."
