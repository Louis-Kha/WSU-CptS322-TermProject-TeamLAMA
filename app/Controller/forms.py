from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.fields.core import BooleanField
from wtforms.fields.simple import TextAreaField
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import  DataRequired, Length, Email, EqualTo
from wtforms_sqlalchemy.fields import QuerySelectMultipleField
from wtforms.widgets import ListWidget, CheckboxInput
from wtforms import validators, PasswordField
from wtforms.fields.html5 import DateField

from app.Model.models import *

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

    researchFields = QuerySelectMultipleField('Research Fields', 
                                query_factory = researchPos().get_posFields, 
                                get_label = researchPostFieldTags.__repr__, 
                                widget = ListWidget(prefix_label = False), 
                                option_widget = CheckboxInput())

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
   # myposts = BooleanField('myposts')


class ApplicationForm(FlaskForm):
    name = StringField('Student Name', validators=[DataRequired()])
    description = TextAreaField('Brief Description', validators=[Length(min = 1, max = 2000, message = "Invalid Length for Post!")])
    reference = TextAreaField('Faculty References', validators=[Length(min = 1, max = 200, message = "Invalid Length for Post!")])
    submit = SubmitField('Post')

# ------------- Added By Alex --------------------------

class EditForm(FlaskForm): #This is the Flask form for the user to edit their profile
    username = StringField('Username', validators=[DataRequired()]) # WSU Email
    email = StringField('Email', validators=[DataRequired(), Email()])

# Things that need to be added still
    # techCourses = StringField('Technical Courses', validators=[DataRequired()])
    wsuID = StringField('Enter your WSU ID', validators=[DataRequired()])
    firstName = StringField('First Name', validators = [DataRequired()])
    lastName = StringField('Last Name', validators = [DataRequired()])
    email = StringField('email', validators=[DataRequired(),Email()]) # will be wsu email
    address = StringField('Address', validators=[DataRequired(), Length(min=10, max=256)])
    phoneNumber = StringField('Phone Number', validators=[DataRequired()])
    gradDate = DateField('Expected Graduation', format='%Y-%m-%d', validators=[DataRequired()])

    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Password Repeated', validators=[DataRequired(), EqualTo('password')])
    knownLang = QuerySelectMultipleField('Programming Languages', 
                                query_factory = User().get_lang, 
                                get_label = progLang.__repr__, 
                                widget = ListWidget(prefix_label = False), 
                                option_widget = CheckboxInput())
    cumGPA = StringField('Cumulative GPA:')
    techCourseGPA = StringField('Technical Courses GPA:')
    userTechnicalCourses = QuerySelectMultipleField('Technical Courses', 
                                query_factory = User().get_courses, 
                                get_label = technicalCourses.__repr__, 
                                widget = ListWidget(prefix_label = False), 
                                option_widget = CheckboxInput())

    experienceDesc = TextAreaField('Experience Description', validators=[Length(min=0, max = 1048)])
    rFieldTags = QuerySelectMultipleField('Research Fields', 
                                query_factory = User().get_field, 
                                get_label = researchFieldTags.__repr__, 
                                widget = ListWidget(prefix_label = False), 
                                option_widget = CheckboxInput())
    userMajors = QuerySelectMultipleField('Majors', 
                                query_factory = User().get_majors, 
                                get_label = majorT.__repr__, 
                                widget = ListWidget(prefix_label = False), 
                                option_widget = CheckboxInput())

    submit = SubmitField('Submit')
#-------------------------------------------------------