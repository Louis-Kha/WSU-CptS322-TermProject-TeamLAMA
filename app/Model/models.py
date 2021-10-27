from datetime import datetime
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, generate_password_hash, check_password_hash
 
postTags = db.Table('PostTag',
    db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique = True)
    email = db.Column(db.String(120), unique = True)
    password_hash = db.Column(db.String(128))
    post = db.relationship('Post', backref = 'writer', lazy = 'dynamic')
    isfaculty = db.Column(db.Boolean)

    def __repr__(self):
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

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

#class Posttag(db.Model):
#    postid = db.Column(db.Integer, db.ForeignKey('post.id'), primary_key = True)
#    tagid =  db.Column(db.Integer, db.ForeignKey('tag.id'), primary_key = True)
from app import db
from enum import unique
from datetime import datetime
from werkzeug.security import generate_password_hash, generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
from sqlalchemy import Date

class Student(UserMixin, db.Model):
    permissions = db.Column(db.Boolean, default = 0)
    username = db.Column(db.String(64)) # I may want to add unique=True, I'm not sure if I want to assume they're going to use their WSU email
    passwordHash = db.Column(db.String(64), unique = True, index = True)
    # ------------------------------------- Contact information -------------------------------------
    firstName = db.Column(db.String(128), default = "Butchy") 
    lastName = db.Column(db.String(128), default = "Boi")
    wsuId = db.Column(db.Integer)
    address = db.Column(db.String(256))
    email = db.Column(db.String(120), unique = True, index = True) # The requirements document didn't specify if this had to be their WSU email
    phoneNumber = db.Column(db.String(32)) # Made it len of 32 because theres no way someone has a phone number that long
    #------------------------------------------------------------------------------------------------
    major = db.Column( db.String(64))                                       # One to many relationship
    cumGPA = db.Column(db.Integer)
    expectedGraduationDate = db.Column(db.String(64)) # May want to change this to an actual date type

    # -----------------------Technical Courses-------------------------------------------
    #                    (One to many relationship)
    technicalCourses = db.Column( db.String(64))                            
    technicalCourseGPA = db.Column(db.Float)                                
    # -----------------------------------------------------------------------------------
    researchFields = db.Column( db.String(64))                              # One to many relationship
    programLang = db.Coumn(db.String(64))                                   # One to many relationship
    experienceDescription = db.Column(db.String(500)) # Research Experience Description

    def __repr__(self):
        return 'Student Name: {} {} - WSU ID: {} - Email: {} - permissions: {} '.format(self.firstName, self.lastName, self.wsuId,self.email, self.permissions)

    #To Do: Create password Functions
    
class Major(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))
    
    def __repr__(self):
        return '{}'.format(self.name)

class Faculty(UserMixin, db.Model):
    permissions = db.Column(db.Boolean, default = 1) 
    username = db.Column(db.String(64)) 
    # --- Contact information ---
    firstName = db.Column(db.String(128)) 
    lastName = db.Column(db.String(128))
    address = db.Column(db.String(256))
    email = db.Column(db.String(120), unique = True, index = True) # The requirements document didn't specify if this had to be their WSU email
    phoneNumber = db.Column(db.String(32)) # Made it len of 32 because theres no way someone has a phone number that long
    #----------------------------
    def __repr__(self):
        return 'Faculty Name: {} {} - Email: {} - permissions: {} '.format(self.firstName, self.lastName, self.email, self.permissions)
    

class researchPos(db.Model):
    title  = db.Column(db.String(64))
    researchDesc = db.Column(db.String(500))
    startDate = db.Column(db.Date)
    endDate = db.Column(db.Date)
    requiredHours = db.Column(db.Integer)
    researchFields = db.Column(db.String(64))
    requiredQualifications = db.Column(db.String(250))






postResearch_field = db.Table('postResearch_field',
    db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
    db.Column('Research_Field_id', db.Integer, db.ForeignKey('research_field.id'))
)



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
    happiness_level = db.Column(db.Integer, default = 3)
    body = db.Column(db.String(1500))
    timecommitment = db.Column(db.Integer, default = 3)
    likes = db.Column(db.Integer, default = 0)
    research_fields = db.relationship(
        'Research_field',
        secondary = postResearch_field,
        primaryjoin=(postResearch_field.c.post_id == id),
        backref=db.backref('postResearch_field, lazy=dynamic'),
        lazy='dynamic'
    )
    def get_researchfield(self):
        return self.research_fields


class Research_field(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    def __repr__(Research_field):
        return '<Research_field id: {} - Research_field name: {}>'.format(Research_field.id, Research_field.name)
