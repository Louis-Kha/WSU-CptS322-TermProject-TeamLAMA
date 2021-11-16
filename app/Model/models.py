from datetime import datetime
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

    password_hash = db.Column(db.String(128))
    post = db.relationship('Post', backref = 'writer', lazy = 'dynamic')
    # remember = db.Column(db.Boolean)
    isfaculty = db.Column(db.Boolean)
    isnotfaculty = db.Column(db.Boolean)

    #------------- Added by Alex 
    knownLanguages = db.relationship('progLang', # Class Name
                                    secondary = userLanguages, # Table 
                                    primaryjoin = (userLanguages.c.user_id == id),
                                    backref = db.backref('userLanguages', lazy = 'dynamic'),
                                    lazy = 'dynamic')
    def get_lang(self):
        allLang = progLang().query.all()
        return allLang
    #----------------------------------
    
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
    title  = db.Column(db.String(150))
    researchDesc = db.Column(db.String(1500))
    startEndDate = db.Column(db.String(150))
    requiredHours = db.Column(db.Integer, default = 0)
    researchFields = db.Column(db.String(150))
    requiredQualifications = db.Column(db.String(500))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)


class application(db.Model):
    __tablename__ = 'applicants'
    student_id = db.Column(db.Integer, default = 0)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(2000))
    reference = db.Column(db.String(200))
    researchPos_id = db.Column(db.Integer, db.ForeignKey('researchPosition.id'))
    researchPosition = db.relationship("researchPos")

#------------ Added by Alex -------------------
class progLang(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(69))

    def __repr__(self): # Prints the Programming Languages in the database
        return '{}, '.format(self.name)
#----------------------------------------------