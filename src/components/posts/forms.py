from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DateTimeField
from wtforms.validators import DataRequired, Email, EqualTo, Length, InputRequired


class NewPost(FlaskForm):

    title = StringField("Blog Title", validators=[DataRequired('Please input blog title'),
                                                  Length(min=3, max=255, message='title must have at least 3 chars and max 255 chars')])
    body = StringField("Blog Body", validators=[DataRequired('Please input blog body'),
                                                Length(min=3, max=1000, message='username must have at least 3 chars and max 1000 chars')])
    submit = SubmitField('Post')