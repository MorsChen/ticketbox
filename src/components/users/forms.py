from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, TextField, TextAreaField, validators, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length, InputRequired
from src.models.user import User

class Register(FlaskForm):
    username = StringField("User Name", validators=[DataRequired('Please input your username'),
                                                    Length(min=3, max=20, message='username must have at least 3 chars and max 20 chars')])
    email = StringField("Email Address", validators=[
                        DataRequired(),  Email("Please input an appropriate email address")])
    password = PasswordField("Password", validators=[
                             DataRequired(), EqualTo('confirm')])
    confirm = StringField("Confirm", validators=[DataRequired()])
    submit = SubmitField("Register")

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Your name has been register !!!")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Your email has been register !!!")


class Login(FlaskForm):
    email = StringField("Email Address", validators=[
                        DataRequired(), Email("Please input an appropriate email address")])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")
