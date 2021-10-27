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