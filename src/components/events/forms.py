from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, TextField, TextAreaField, validators, BooleanField, DateTimeField, IntegerField
from wtforms.validators import DataRequired, Length, InputRequired
from datetime import datetime


class AddForm(FlaskForm):

    name = StringField("Event Name", validators=[DataRequired('Please input your username'),
                                                    Length(min=3, max=100, message='username must have at least 3 chars and max 100 chars')])
    description = StringField("Description", validators=[DataRequired('Please input Decsriptopn')])
    image_url = StringField('Image URL:', validators=[DataRequired('Please input Image Url')])
    address = StringField('Address:', validators=[DataRequired('Please input your Address')])
    datetimestart = StringField('Date-Time-Start:',validators=[DataRequired("Please input Date-Start")])
    datetimeend = StringField('Date-Time-End:')
    submit = SubmitField('Add Event')
    
    def validate_datetimestart(self, field):
        if datetime.strptime(field.data,"%m/%d/%Y %H:%M") <= datetime.now():
            raise ValidationError("Please check Date Start, it must be in the future !!!")
        
    def validate_datetimeend(self, field):
        if not field.data:
            field.data == None
        elif datetime.strptime(field.data,"%m/%d/%Y %H:%M") <= datetime.strptime(self.datetimestart.data,"%m/%d/%Y %H:%M"):
            raise ValidationError("Please check Date End, it must be in the future !!!")
            
        
    
class DelForm(FlaskForm):

    id = IntegerField('Id Number of Event to Remove:')
    submit = SubmitField('Remove Event')
