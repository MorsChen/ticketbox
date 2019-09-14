from src import db

class Tickettype(db.Model):

    __tablename__ = 'tickettypes'

    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer,db.ForeignKey('events.id'))
    name = db.Column(db.String(100))
    price = db.Column(db.Integer, default = 0)
    stockquanity = db.Column(db.Integer, default = 0)
    restquantity = db.Column(db.Integer)
    ticket = db.relationship('Ticket', backref='tickettypes', cascade="all, delete-orphan", lazy='dynamic')
    
    def setrestquantity(self, quantity):
        self.restquantity =  self.stockquanity - quantity