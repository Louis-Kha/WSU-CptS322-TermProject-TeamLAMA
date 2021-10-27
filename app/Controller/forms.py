from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import  DataRequired, Length


from app.Model.models import Post

class PostForm(FlaskForm):
    title = StringField('Research Position Title', validators=[DataRequired()])
    happiness_level = SelectField('Happiness Level',choices = [(3, 'I can\'t stop smiling'), (2, 'Really happy'), (1,'Happy')])
    body = TextAreaField('Position Description', validators=[Length(min = 1, max = 1500, message = "Invalid Length for Post!")])
    timecommitment = SelectField('Time Commitment',choices = [(40, '40 Hours'), (30, '30 Hours'), (20, '20 Hours'), (10, '10 Hours')])
    submit = SubmitField('Post')
