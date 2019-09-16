from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from datetime import datetime

from src import db

from src.components.events.forms import AddForm, DelForm
from src.components.tickettypes.forms import AddType, DelType
from src.models.event import Event
from src.models.tickettype import Tickettype


events_blueprint = Blueprint('events',
                             __name__,
                             template_folder='../../templates/events')

@events_blueprint.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = AddForm()
    formtype = AddType()
    if request.method == 'POST':
        if form.validate_on_submit():
            newevent =Event(name=form.name.data,
                            description = form.description.data,
                            image_url = form.image_url.data,
                            address = form.address.data,
                            datetimestart = datetime.strptime(form.datetimestart.data,"%m/%d/%Y %H:%M"),
                            created = datetime.now(), 
                            datetimeend = None if not form.datetimeend.data else datetime.strptime(form.datetimeend.data, "%m/%d/%Y %H:%M")
                            )
            current_user.event.append(newevent)
            db.session.add(newevent)
            db.session.commit()
            return redirect(url_for('tickettypes.addtype',id = newevent.id))
        else:
            for field_name, errors in form.errors.items():
                flash(errors)
    return render_template('add.html', form=form)

@events_blueprint.route('/list')
def list():
    # Grab a list of events from database.
    events = Event.query.all()
    tickettypes = Tickettype.query.all()
    return render_template('list.html', events = events, tickettypes = tickettypes)

@events_blueprint.route('/singleevent/<id>', methods = ['POST', 'GET'])
@login_required
def single_event(id):
    event = Event.query.filter_by(id = id).first()
    tickettypes = Tickettype.query.filter_by(event_id = id).all()
    print("check single", id)
    print('check tickettypes', tickettypes)
    if event:
        event.views += 1
        db.session.commit()
    return render_template('single_event.html', event = event, tickettypes = tickettypes )


@events_blueprint.route('/editevent/<id>', methods=['POST', 'GET'])
@login_required
def editevent(id):
    ref = request.args.get('ref')
    form = AddForm()
    event = Event.query.filter_by(id = id, owner_id=current_user.id).first()
    if not event:
        flash('you are not allow to edit the Event')
        return redirect(url_for('single_event', id = id))
    elif request.method == 'POST':
        event.name = form.name.data
        event.description = form.description.data
        event.image_url = form.image_url.data
        event.address = form.address.data
        event.datetimestart = datetime.strptime(form.datetimestart.data,"%m/%d/%Y %H:%M") > datetime.now()
        event.updated = datetime.now()
        event.datetimeend = None if not form.datetimeend.data else datetime.strptime(form.datetimeend.data, "%m/%d/%Y %H:%M") > event.datetimestart
        db.session.commit()  
        return redirect(url_for('events.single_event', id = id))
    return render_template('editevent.html', form = form, event = event)



@events_blueprint.route('/delete/<id>', methods=['GET'])
@login_required
def delete(id):
    print('check', id)
    event = Event.query.filter_by(id=id).first()
    if Event.query.filter_by(id=id, owner_id=current_user.id).first():
            db.session.delete(event)
            db.session.commit()
            flash("Event successfully deleted!", 'success')
    else:
        flash("You are not authorized to delete this event", "danger")
    return redirect(url_for('events.list'))
