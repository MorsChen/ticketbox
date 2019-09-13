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
            newevent = Event(name=form.name.data,
                            description = form.description.data,
                            image_url = form.image_url.data,
                            price = form.price.data,
                            address = form.address.data,
                            time = form.time.data,
                            created = datetime.now())
            current_user.event.append(newevent)
            db.session.add(newevent)
            db.session.commit()
            print('check',uuid.uuid4())
        return redirect(url_for('events.add'))
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
    if event:
        event.views += 1
        db.session.commit()
    return render_template('single_event.html', event = event )



@events_blueprint.route('/delete', methods=['GET', 'POST'])
def delete():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        pup = Event.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('events.list'))
    return render_template('delete.html', form=form)
