from datetime import datetime

from sqlalchemy.orm import backref
from app import db, login
from flask_login import UserMixin, LoginManager
from werkzeug.security import generate_password_hash, generate_password_hash, check_password_hash

# import app
 
# Al commits
## changing login.html, register.html, models.py, auth_routes.py, auth_forms.py

postTags = db.Table('postTags',
    db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
)
# ----------------------Alex
userLanguages = db.Table('userLanguages',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('progLang_id', db.Integer, db.ForeignKey('prog_lang.id'))
)

interestedFields = db.Table('interestedFields',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('researchFieldTags_id', db.Integer, db.ForeignKey('research_field_tags.id'))
)

researchPosFieldTable = db.Table('researchPosFieldTable', # for research positions
    db.Column('researchPosition_id', db.Integer, db.ForeignKey('researchPosition.id')),
    db.Column('researchPostFieldTags_id', db.Integer, db.ForeignKey('research_post_field_tags.id')),
)

majorTable = db.Table('majorTable',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('majorT_id', db.Integer, db.ForeignKey('majorT.id'))
)

technicalCoursesTable = db.Table('technicalCoursesTable',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('technicalCourses_id', db.Integer, db.ForeignKey('technical_courses.id'))
)
#---------------------------


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique = True)
    wsuID = db.Column(db.Integer)

    # Contact Information
    firstName = db.Column(db.String(128)) 
    lastName = db.Column(db.String(128))    
    email = db.Column(db.String(120), unique = True)
    address = db.Column(db.String(256))
    phoneNumber = db.Column(db.String(32))
    startDate = db.Column(db.DateTime)

    password_hash = db.Column(db.String(128))
    post = db.relationship('Post', backref = 'writer', lazy = 'dynamic')
    # remember = db.Column(db.Boolean)
    gradDate = db.Column(db.DateTime)
    isfaculty = db.Column(db.Boolean)
    isnotfaculty = db.Column(db.Boolean)

    cumGPA = db.Column(db.Float)
    techCourseGPA = db.Column(db.Float)
    experienceDesc = db.Column(db.String(1048))

    knownLanguages = db.relationship('progLang', # Class Name
                                    secondary = userLanguages, # Table 
                                    primaryjoin = (userLanguages.c.user_id == id),
                                    backref = db.backref('userLanguages', lazy = 'dynamic'),
                                    lazy = 'dynamic')

    userResearchFields = db.relationship('researchFieldTags', # Class Name
                                    secondary = interestedFields, # Table 
                                    primaryjoin = (interestedFields.c.user_id == id),
                                    backref = db.backref('interestedFields', lazy = 'dynamic'),
                                    lazy = 'dynamic')

    userMajor = db.relationship('majorT', # Class Name
                                    secondary = majorTable, # Table 
                                    primaryjoin = (majorTable.c.user_id == id),
                                    backref = db.backref('majorTable', lazy = 'dynamic'),
                                    lazy = 'dynamic')

    userTechnicalCourses = db.relationship('technicalCourses', # Class Name
                                    secondary = technicalCoursesTable, # Table 
                                    primaryjoin = (technicalCoursesTable.c.user_id == id),
                                    backref = db.backref('technicalCoursesTable', lazy = 'dynamic'),
                                    lazy = 'dynamic')

    #----------
    def get_courses(self): #Returns all of the user technical courses
        allCourses = technicalCourses().query.all()
        return allCourses

    def get_majors(self): # Returns all of the user's majors
        allMajors = majorT().query.all()
        return allMajors

    def get_lang(self): # returns all of the user's known languages
        allLang = progLang().query.all()
        return allLang

    def get_field(self): # returns the user's interested research fields
        allFields = researchFieldTags().query.all()
        return allFields  
    
    def __repr__(self): # returns the user's WSU email
        return ' {} - {} '.format(self.username, self.id)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password) 
    
    def get_password(self, password):
        return check_password_hash(self.password_hash, password)

    # checks whether the faculty or not
    def get_status(self, statusinput):
        return self.isfaculty == statusinput

    def status_out(self):
        return self.isfaculty

    def get_user_posts(self):
        allUserPosts = User.query.all()
        return allUserPosts
    
    # def get_remember(self):
    #     return self.remember 

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

#class Posttag(db.Model):
#    postid = db.Column(db.Integer, db.ForeignKey('post.id'), primary_key = True)
#    tagid =  db.Column(db.Integer, db.ForeignKey('tag.id'), primary_key = True)

class Post(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    body = db.Column(db.String(1500))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    likes = db.Column(db.Integer, default = 0)
    happiness_level = db.Column(db.Integer, default = 3) 
    tags = db.relationship('Tag', 
                            secondary = postTags,
                            primaryjoin=(postTags.c.post_id == id),
                            backref=db.backref('postTags', lazy='dynamic'),
                            lazy='dynamic')

    
    def get_tags(self):
        return self.tags


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    def __repr__(self):
        return '<Id: {} Name: {}>'.format(self.id,self.name)



class researchPos(db.Model):
    __tablename__ = 'researchPosition'
    id = db.Column(db.Integer, primary_key=True)
    faculty_id = db.Column(db.Integer, default = 0)
    facultyName = db.Column(db.String(100))
    title  = db.Column(db.String(150))
    researchDesc = db.Column(db.String(1500))
    startDate = db.Column(db.DateTime)
    endDate = db.Column(db.DateTime)
    requiredHours = db.Column(db.Integer, default = 0)

    researchFields = db.relationship('researchPostFieldTags',
                                    secondary = researchPosFieldTable,
                                    primaryjoin = (researchPosFieldTable.c.researchPosition_id == id),
                                    backref = db.backref('researchPosFieldTable', lazy = 'dynamic'),
                                    lazy = 'dynamic')

    requiredQualifications = db.Column(db.String(500))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Id: {} Name: {}>'.format(self.id,self.title)
    
    def get_posFields(self):
        allFields = researchPostFieldTags().query.all()
        return allFields


class application(db.Model):
    __tablename__ = 'applicants'
    student_id = db.Column(db.Integer, default = 0)
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Integer, default = 0) #0 = pending, 1 = interview, 2 = hired, 3 = rejected
    name = db.Column(db.String(100))
    description = db.Column(db.String(2000))
    reference = db.Column(db.String(200))
    researchPos_id = db.Column(db.Integer, db.ForeignKey('researchPosition.id')) 
    researchPosition = db.relationship("researchPos")
    def __repr__(self): # Prints the Programming Languages in the database
        return '{}, '.format(self.name)

#------------ Added by Alex -------------------
class progLang(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(69))

    def __repr__(self): # Prints the Programming Languages in the database
        return '{} '.format(self.name)

class researchFieldTags(db.Model): #Research Fields for studends and faculty to add to their profile
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(69))

    def __repr__(self): 
        return '{} '.format(self.name)

class researchPostFieldTags(db.Model): # This is for the researchPosition Posts
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(69))

    def __repr__(self): 
        return '{} '.format(self.name)

class majorT(db.Model): #Majors for students
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(69))

    def __repr__(self): 
        return '{} '.format(self.name)

class technicalCourses(db.Model): #Technical Courses Students took
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(69))

    def __repr__(self): 
        return '{} '.format(self.name)
#----------------------------------------------