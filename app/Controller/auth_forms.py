from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.core import BooleanField
from wtforms.validators import  ValidationError, DataRequired, EqualTo, Length,Email
from wtforms.fields.simple import PasswordField
from app.Model.models import User

class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(),Length(min=0, max=64)]) # should be rewritten for email
    email = StringField('email', validators=[DataRequired(),Email()]) # will be wsu email
    password1 = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Password Repeat', validators=[DataRequired(), EqualTo('password1')])
    remember = BooleanField('Remember')
    # wsuID - StringField('Enter your WSU ID', validators=[DataRequired(), type(int)])
    isfaculty = BooleanField('Check if faculty member')
    isnotfaculty = BooleanField('opposite of isfaculty')
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember')
    isfaculty = BooleanField('Check if faculty member')
    isnotfaculty = BooleanField('opposite of isfaculty')
    submit = SubmitField('Sign in')

class StudentInfoForm(FlaskForm):
    check = BooleanField()

class FacultyInfoForm(FlaskForm):
    check = BooleanField()
