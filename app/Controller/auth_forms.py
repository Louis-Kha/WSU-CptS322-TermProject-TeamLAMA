from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.core import BooleanField
from wtforms.validators import  ValidationError, DataRequired, EqualTo, Length,Email
from wtforms.fields.simple import PasswordField
from app.Model.models import User

class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Email(), Length(min=0, max=64)]) # should be rewritten for email

    wsuID = StringField('Enter your WSU ID', validators=[DataRequired()])
    firstName = StringField('First Name', validators = [DataRequired()])
    lastName = StringField('Last Name', validators = [DataRequired()])
    email = StringField('email', validators=[DataRequired(),Email()]) # will be wsu email
    address = StringField('Address', validators=[DataRequired(), Length(min=10, max=256)])
    phoneNumber = StringField('Phone Number', validators=[DataRequired()])

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

class StudentInfoForm(FlaskForm):
    check = BooleanField()

class FacultyInfoForm(FlaskForm):
    check = BooleanField()
