from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DateTimeField


class AddForm(FlaskForm):

    name = StringField('Name of Event:')
    description = StringField('Description:')
    image_url = StringField('Image URL:')
    price = IntegerField('Price:')
    address = StringField('Address:')
    time = DateTimeField('Date:')
    submit = SubmitField('Add Event')


class DelForm(FlaskForm):

    id = IntegerField('Id Number of Event to Remove:')
    submit = SubmitField('Remove Event')
