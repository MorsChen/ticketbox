from flask import Blueprint, render_template, redirect, url_for
from src import db
from src.components.events.forms import AddForm, DelForm
from src.models.event import Event

events_blueprint = Blueprint('events',
                             __name__,
                             template_folder='../../templates/events')

@events_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        image_url = form.image_url.data
        price = form.price.data
        address = form.address.data
        time = form.time.data
        # Add new Event to database
        new_pup = Event(name, description, image_url, price, address, time)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('events.list'))

    return render_template('add.html', form=form)


@events_blueprint.route('/list')
def list():
    # Grab a list of events from database.
    events = Event.query.all()
    return render_template('list.html', events=events)


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
