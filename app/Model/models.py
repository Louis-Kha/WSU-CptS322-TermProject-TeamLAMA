from datetime import datetime
from app import db


postResearch_field = db.Table('postResearch_field',
    db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
    db.Column('Research_Field_id', db.Integer, db.ForeignKey('research_field.id'))
)



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
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