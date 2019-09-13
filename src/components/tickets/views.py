from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from datetime import datetime
import uuid

from src import db

from src.models.ticket import Ticket
from src.models.tickettype import Tickettype

tickets_blueprint = Blueprint('tickets',
                             __name__,
                             template_folder='../../templates/tickets')


@tickets_blueprint.route('/addticket', methods=['POST','GET'])
@login_required
def addticket():
    
    pass

@tickets_blueprint.route('/list', methods = ['POST', 'GET'])
@login_required
def list():
    tickets = Ticket.query.all()
    return render_template('ticketlist.html', tickets = tickets)

