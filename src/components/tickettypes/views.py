from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from datetime import datetime

from src import db

from src.components.tickettypes.forms import AddType, DelType
from src.models.tickettype import Tickettype

tickettypes_blueprint = Blueprint('tickettypes',
                             __name__,
                             template_folder='../../templates/tickettypes')

@ticketypes_blueprint.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = AddType()
    if request.method == 'POST':
        if form.validate_on_submit():
            if form.datetimeend.data:
                newtype =Tickettype(name=form.name.data,
                                description = form.description.data,
                                image_url = form.image_url.data,
                                address = form.address.data,
                                datetimestart = datetime.strptime(form.datetimestart.data,"%m/%d/%Y %H:%M"),
                                created = datetime.now(),
                                datetimeend = datetime.strptime(form.datetimeend.data, "%m/%d/%Y %H:%M"))
            else:
                newtype =Tickettype(name=form.name.data,
                                description = form.description.data,
                                image_url = form.image_url.data,
                                address = form.address.data,
                                datetimestart = datetime.strptime(form.datetimestart.data,"%m/%d/%Y %H:%M"),
                                created = datetime.now()
                                )
            current_user.event.append(newtype)
            db.session.add(newtype)
            db.session.commit()
            db.session.commit()
        else:
            for field_name, errors in form.errors.items():
                flash(errors)
                return redirect(url_for('add'))
        return redirect(url_for('home'))
    return render_template('add.html', form=form)

@ticketypes_blueprint.route('/list')
def list():
    # Grab a list of events from database.
    types = Tickettype.query.all()
    return render_template('list.html', types = types)

@ticketypes_blueprint.route('/singleevent/<id>', methods = ['POST', 'GET'])
@login_required
def single_event(id):
    type = Tickettype.query.filter_by(id = id).first()
    print("check single", id)
    if type:
        event.views += 1
        db.session.commit()
    return render_template('single_event.html', tpye = type )



@ticketypes_blueprint.route('/delete/<id>', methods=['GET'])
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
