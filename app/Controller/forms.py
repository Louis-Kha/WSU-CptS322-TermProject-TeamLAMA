from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.fields.core import BooleanField
from wtforms.fields.simple import TextAreaField
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import  DataRequired, Length, Email, EqualTo
from wtforms_sqlalchemy.fields import QuerySelectMultipleField
from wtforms.widgets import ListWidget, CheckboxInput
from wtforms import validators, PasswordField

from app.Model.models import Post, Tag, User

from app.Model.models import Post

def getAlltags():
    return Tag.query.all()

# this was causing problems, now fixed 
def getTagsbyName(tag):
    return tag.name
    # alltags = Tag.query.all()
    # for t in Tag.query.all():
    #     return t.name
    


class ResearchForm(FlaskForm):
    title = StringField('Research Position Title', validators=[DataRequired()])
    startEndDate = StringField('Start/End Dates (Eg. 11/11/21 - 01/11/22)', validators=[DataRequired()])
    researchDesc = TextAreaField('Position Description', validators=[Length(min = 1, max = 1500, message = "Invalid Length for Post!")])
    researchFields = TextAreaField('Research fields', validators=[Length(min = 1, max = 1500, message = "Invalid Length for Post!")])
    requiredHours = SelectField('Required Hours Per Week',choices = [(40, '40 Hours'), (30, '30 Hours'), (20, '20 Hours'), (10, '10 Hours')])
    requiredQualifications = TextAreaField('Required Qualifications', validators=[Length(min = 1, max = 1500, message = "Invalid Length for Post!")])
    submit = SubmitField('Post')


class PostForm(FlaskForm):
    title = StringField('Research Position Title', validators=[DataRequired()])
    happiness_level = SelectField('Happiness Level',choices = [(3, 'I can\'t stop smiling'), (2, 'Really happy'), (1,'Happy')])
    body = TextAreaField('Body', validators=[DataRequired()])
    tag = QuerySelectMultipleField('Tag', query_factory = getAlltags, get_label=getTagsbyName, allow_blank=False, widget=ListWidget(prefix_label=False), 
       option_widget=CheckboxInput())
    body = TextAreaField('Position Description', validators=[Length(min = 1, max = 1500, message = "Invalid Length for Post!")])
    timecommitment = SelectField('Time Commitment',choices = [(40, '40 Hours'), (30, '30 Hours'), (20, '20 Hours'), (10, '10 Hours')])
    submit = SubmitField('Post')
    # tag = QuerySelectMultipleField('Tag', query_factory="", get_label="", widget=ListWidget(prefix_label=False), 
    #   option_widget=CheckboxInput())

class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')

class SortForm(SelectField):
    sortform = SelectField('Sort options',choices = [(4, 'Date'),(3, 'Title'), (2, '# of likes'), (1,'Happiness level')])
    refresh = SubmitField('Refresh')
    myposts = BooleanField('myposts')

# ------------- Added By Alex --------------------------
#Some obstacles I noticed was maybe creating a separate edit form for the faculty? Still Waiting on the UserModels
# This is just going to be for the student for now, will change later

class EditForm(FlaskForm): #This is the Flask form for the user to edit their profile
    username = StringField('Username', validators=[DataRequired()]) # WSU Email
    email = StringField('Email', validators=[DataRequired(), Email()])

# Things that need to be added still
    # firstname = StringField('First Name', validators=[DataRequired()])
    # lastname = StringField('Last Name', validators=[DataRequired()])
    # address = TextAreaField('Address', [Length(min=0, max=200)])
    # phoneNumber = StringField('Phone Number', [Length(min=0, max=20)])
    # major = StringField('Major', validators=[DataRequired()])
    # cumGPA = StringField('Cumulative GPA', validators=[DataRequired()]) #May want to change this to a float/Double?
    # expectedGradDate = StringField('Expected Graduation Date', validators=[DataRequired()])
    # techCourses = StringField('Technical Courses', validators=[DataRequired()])
    # techGPA = StringField('Technical Courses GPA', validators=[DataRequired()])
    # researchFields = StringField('Interested Research Fields')
    # programmingLanguage = StringField('Programming Languages', validators=[DataRequired()])
    # priorResearchExp = TextAreaField('Prior Research Experience', validators=[DataRequired()])

    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Password Repeated', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit')
#-------------------------------------------------------