from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, TextField, TextAreaField, validators, BooleanField, DateTimeField, IntegerField
from wtforms.validators import DataRequired, Length, InputRequired


class AddType(FlaskForm):

    name = StringField("Type Name", validators=[DataRequired('Please input ticket type'),
                                                    Length(min=3, max=100, message='ticket type must have at least 3 chars and max 100 chars')])
    price = IntegerField('Price:', validators=[DataRequired('Please input Price')])
    stockquantity = IntegerField('Stock-Quantity', validators=[DataRequired('Please input Quantity')])
    submit = SubmitField('Add Type')


class EditType(FlaskForm):
    name = StringField("Type Name", validators=[DataRequired('Please input ticket type'),
                                                    Length(min=3, max=100, message='ticket type must have at least 3 chars and max 100 chars')])
    price = IntegerField('Price:', validators=[DataRequired('Please input Price')])
    stockquantity = IntegerField('Stock-Quantity', validators=[DataRequired('Please input Quantity')])
    submit = SubmitField('Edit Type')

class DelType(FlaskForm):

    id = IntegerField('Id Number of Event to Remove:')
    submit = SubmitField('Remove Event')
