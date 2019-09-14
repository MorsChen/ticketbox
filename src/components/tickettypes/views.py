from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from datetime import datetime

from src import db

from src.components.tickettypes.forms import AddType, DelType
from src.models.event import Event
from src.models.tickettype import Tickettype

tickettypes_blueprint = Blueprint('tickettypes',
                             __name__,
                             template_folder='../../templates/tickettypes')

@tickettypes_blueprint.route('/add/<id>', methods=['GET', 'POST'])
@login_required
def addtype(id):
    form = AddType()
    newevent = Event.query.filter_by(id=id).first()
    if request.method == 'POST':
        if newevent:
            if form.validate_on_submit():
                newtype =Tickettype(name=form.name.data,
                                price = form.price.data,
                                stockquantity = form.stockquantity.data,
                                )
                newevent.tickettypes.append(newtype)
                db.session.add(newtype)
                db.session.commit()
                print ("check1")
        else:
            for field_name, errors in form.errors.items():
                flash(errors)
                print ("check error")
                return redirect(url_for('addtype'))
    return render_template('addtype.html', form=form)

@tickettypes_blueprint.route('/list')
def list():
    # Grab a list of events from database.
    types = Tickettype.query.all()
    return render_template('list.html', types = types)

@tickettypes_blueprint.route('/delete/<id>', methods=['GET'])
@login_required
def delete(id):
    print('check', id)
    type = Tickettype.query.filter_by(id=id).first()
    if Tickettype.query.filter_by(id=id, owner_id=current_user.id).first():
            db.session.delete(type)
            db.session.commit()
            flash("Event successfully deleted!", 'success')
    else:
        flash("You are not authorized to delete this event", "danger")
    return redirect(url_for('events.list'))
