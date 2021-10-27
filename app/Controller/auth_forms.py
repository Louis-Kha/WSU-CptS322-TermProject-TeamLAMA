from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.core import BooleanField
from wtforms.validators import  ValidationError, DataRequired, EqualTo, Length,Email
from wtforms.fields.simple import PasswordField
from app.Model.models import User

class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(),Length(min=0, max=64)])
    email = StringField('email', validators=[DataRequired(),Email()])
    password1 = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Password Repeat', validators=[DataRequired(), EqualTo('password1')])
    isfaculty = BooleanField('Check if faculty member')
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember')
    isfaculty = BooleanField('Check if faculty member')
    submit = SubmitField('Sign in')