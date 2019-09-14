from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from datetime import datetime
import uuid

from src import db

from src.components.events.forms import AddForm, DelForm
from src.models.event import Event

events_blueprint = Blueprint('events',
                             __name__,
                             template_folder='../../templates/events')

@events_blueprint.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = AddForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            if form.datetimeend.data:
                    newevent =Event(name=form.name.data,
                                    description = form.description.data,
                                    image_url = form.image_url.data,
                                    address = form.address.data,
                                    datetimestart = datetime.strptime(form.datetimestart.data,"%m/%d/%Y %H:%M"),
                                    created = datetime.now(),
                                    datetimeend = datetime.strptime(form.datetimeend.data, "%m/%d/%Y %H:%M"))
            else:
                newevent = Event(name=form.name.data,
                                description = form.description.data,
                                image_url = form.image_url.data,
                                address = form.address.data,
                                datetimestart = datetime.strptime(form.datetimestart.data,"%m/%d/%Y %H:%M"),
                                created = datetime.now()
                                )
            current_user.event.append(newevent)
            db.session.add(newevent)
            db.session.commit()
            db.session.commit()
        else:
            for field_name, errors in form.errors.items():
                flash(errors)
                return redirect(url_for('add'))
        return redirect(url_for('home'))
    return render_template('add.html', form=form)

@events_blueprint.route('/list')
def list():
    # Grab a list of events from database.
    events = Event.query.all()
    return render_template('list.html', events = events)

@events_blueprint.route('/singleevent/<id>', methods = ['POST', 'GET'])
@login_required
def single_event(id):
    event = Event.query.filter_by(id = id).first()
    print("check single", id)
    if event:
        event.views += 1
        db.session.commit()
    return render_template('single_event.html', event = event )



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
