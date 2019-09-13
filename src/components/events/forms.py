from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, TextField, TextAreaField, validators, BooleanField, DateTimeField, IntegerField
from wtforms.validators import DataRequired, Length, InputRequired


class AddForm(FlaskForm):

    name = StringField("Event Name", validators=[DataRequired('Please input your username'),
                                                    Length(min=3, max=100, message='username must have at least 3 chars and max 100 chars')])
    description = StringField("Description", validators=[DataRequired('Please input Decsriptopn')])
    image_url = StringField('Image URL:', validators=[DataRequired('Please input Image Url')])
    price = IntegerField('Price:', validators=[DataRequired('Please input Price')])
    address = StringField('Address:', validators=[DataRequired('Please input your Address')])
    time = StringField('Date:')
    submit = SubmitField('Add Event')


class DelForm(FlaskForm):

    id = IntegerField('Id Number of Event to Remove:')
    submit = SubmitField('Remove Event')
