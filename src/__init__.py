from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
login = LoginManager(app)
POSTGRES = {
    'user': os.environ['PSQL_USER'],
    'pw': os.environ['PSQL_PWD'],
    'db': os.environ['PSQL_DB'],
    'host': os.environ['PSQL_HOST'],
    'port': os.environ['PSQL_PORT'],
}

# Often people will also separate these into a separate config.py file
app.config['SECRET_KEY'] = 'mysecretkey'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:\
%(port)s/%(db)s' % POSTGRES
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db, compare_type=True)

from src.components.events.views import events_blueprint
app.register_blueprint(events_blueprint, url_prefix='/events')

from src.components.users.views import users_blueprint
app.register_blueprint(users_blueprint, url_prefix='/users')

from src.components.tickets.views import tickets_blueprint
app.register_blueprint(tickets_blueprint, url_prefix='/tickets')

# from src.components.posts.views import posts_blueprint
# app.register_blueprint(posts_blueprint, url_prefix='/posts')


from src.models.user import User

@login.user_loader
def load_user(id):
    return User.query.get(int(id))  