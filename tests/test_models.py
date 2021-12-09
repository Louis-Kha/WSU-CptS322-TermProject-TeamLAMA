import pytest
import warnings
warnings.filterwarnings("ignore")
import os
basedir = os.path.abspath(os.path.dirname(__file__))

from datetime import datetime, timedelta
import unittest
from app import create_app, db
from app.Model.models import User, Post, Tag
from config import Config
from app.Model.models import Post, Tag, postTags, researchPos, User, application

# to run this test:
# #1 cd into the tests folder through cmd: cd tests
# #2 run in the cmd: pytest test_models.py
# or pytest test_models.py

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    ROOT_PATH = '..//'+ basedir
    
class TestModels(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

## --Correct Above--

    # password hashing
    def test_password_hashing_faculty(self): # password hashing works
        u1 = User(username='john', email='john.yates@wsu.edu', isfaculty=True)
        u2 = User(username='johnfaculty', email='john.yates@wsu.edu', isfaculty=False)
        u1.set_password('covid')
        u2.set_password('19')
        self.assertFalse(u1.get_password('flu'))
        self.assertTrue(u1.get_password('covid'))
        self.assertFalse(u2.get_password('flu'))
        self.assertTrue(u2.get_password('19'))

    # check if faculty
    def test_status_check(self):
        s = User(username='john', email='john.yates@wsu.edu', isfaculty=False)
        f = User(username='john', email='john.yates@wsu.edu', isfaculty=True)
        self.assertFalse(s.get_status(True))
        self.assertTrue(f.get_status(True))

    def test_add_user_adds(self):
        u1 = User(username='john', email='john.yates@wsu.com', isfaculty=True)
        db.session.add(u1)
        db.session.commit()
        assert u1.id==1
        assert u1.username=='john'
        assert u1.isfaculty==True

    def test_research_post_interaction(self):
        p1 = researchPos(title='Research',facultyName='TestProf',faculty_id=1512769)
        db.session.add(p1)
        db.session.commit()
        assert p1.id==1
        assert p1.title=='Research'
        assert p1.faculty_id==1512769

    def test_research_post_tags_interaction(self):
        p1 = researchPos(title='TagResearch',facultyName='TagProf')
        db.session.add(p1)
        db.session.commit()
        assert p1.id==1
        assert p1.title=='TagResearch'

    def test_application_interactions(self):
        a1 = application(student_id='9494949',name='Testudent',status=4)
        db.session.add(a1)
        db.session.commit()
        assert a1.student_id==9494949
        assert a1.name=='Testudent'
        assert a1.status==4

if __name__ == '__main__':
    pytest.main(verbosity=2)