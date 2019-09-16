from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from datetime import datetime

from src import db

from src.components.tickettypes.forms import AddType, DelType, EditType
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

@tickettypes_blueprint.route('/<id>/edit/<typeid>', methods = ['POST', 'GET'])
@login_required
def edittype(id, typeid):
    ref = request.args.get('ref')
    form = EditType()
    event = Event.query.filter_by(id = id, owner_id=current_user.id).first()
    tickettypes = Tickettype.query.filter_by(event_id = id).first()
    print("check event", event.id)
    tickettype = Tickettype.query.filter_by(event_id = id, id = typeid).first()
    print("check type", tickettype)
    if not event:
        flash('you are not allow to edit the Event')
        return redirect(url_for('single_event', id = id))
    elif request.method == 'POST':
        if tickettype:
            if form.validate_on_submit():
                tickettype.name=form.name.data,
                tickettype.price = form.price.data
                tickettype.stockquantity = form.stockquantity.data
                db.session.commit()  
            return redirect(url_for('events.single_event', id = id))
    return render_template('edittype.html', form = form, event = event, tickettype = tickettype, tickettypes = tickettypes)

@tickettypes_blueprint.route('/<id>/editallticket/', methods=['POST','GET'])
@login_required
def editallticket(id):
    form = EditType()
    event = Event.query.filter_by(id = id, owner_id=current_user.id).first()
    tickettypes = Tickettype.query.filter_by(event_id = id).all()
    if not event:
        flash('you are not allow to edit the Event')
        return redirect(url_for('single_event', id = id))
    elif request.method == 'POST':
        if tickettypes:
            if form.validate_on_submit():
                tickettype.name=form.name.data,
                tickettype.price = form.price.data
                tickettype.stockquantity = form.stockquantity.data
                db.session.commit()  
                return redirect(url_for('events.single_event', id = id))
    return render_template('editallticket.html', form = form, event = event, tickettypes = tickettypes)
  

@tickettypes_blueprint.route('/<id>delete/<typeid>', methods=['GET'])
@login_required
def delete(id, typeid):
    event = Event.query.filter_by(id = id, owner_id=current_user.id).first()
    tickettype = Tickettype.query.filter_by(event_id = id, id = typeid).first()
    print("check id event", id, tickettype.event_id, current_user.id, event.owner_id, typeid, tickettype.id)
    if not event:
        flash('you are not allow to edit the Event')
        return redirect(url_for('events.single_event', id = id))
    elif tickettype:
        print("check if", tickettype)
        db.session.delete(tickettype)
        db.session.commit()
        flash("Event successfully deleted!", 'success')
    else:
        flash("You are not authorized to delete this event", "danger")
    return redirect(url_for('events.single_event', id = id))
