"""
This file contains the functional tests for the routes.
These tests use GETs and POSTs to different URLs to check for the proper behavior.
Resources:
    https://flask.palletsprojects.com/en/1.1.x/testing/ 
    https://www.patricksoftwareblog.com/testing-a-flask-application-using-pytest/ 
"""
import pytest
from app import create_app, db
from app.Model.models import User, Post, Tag
from config import Config

# to run this test:
# #1 cd into the tests folder through cmd: cd tests
# #2 run in the cmd: pytest test_routes.py

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SECRET_KEY = 'bad-bad-key'
    WTF_CSRF_ENABLED = False
    DEBUG = True
    TESTING = True

@pytest.fixture(scope='module')
def test_client():
    # create the flask application ; configure the app for tests
    flask_app = create_app(config_class=TestConfig)
    db.init_app(flask_app)
    testing_client = flask_app.test_client()
    ctx = flask_app.app_context()
    ctx.push()
    yield testing_client 
    ctx.pop()

@pytest.fixture
def init_database():
    db.create_all()   
    user1 = User(username='sakire')
    user1.set_password('1234')
    db.session.add(user1)
    db.session.commit()
    yield  
    db.drop_all()

## --configuration setup above--
def test_sregister_page(test_client): # passes
    response = test_client.get('/register')
    assert response.status_code == 200
    assert b"Register" in response.data

def test_fregister_page(test_client): # passes
    response = test_client.get('/Facultyregister')
    assert response.status_code == 200
    assert b"Register" in response.data

def test_slogin(test_client):
    response = test_client.get('/login')
    assert response.status_code == 200
    assert b"Student Sign In" in response.data

def test_flogin(test_client):
    response = test_client.get('/FacultyLogin')
    assert response.status_code == 200
    assert b"Faculty Sign In" in response.data

def test_sindex(test_client):
    response = test_client.get('/studentindex')
    assert response.status_code == 302

def test_findex(test_client):
    response = test_client.get('/facultyindex')
    assert response.status_code == 302

def test_slogin_action(request,test_client,init_database):
    response = test_client.post('/login', 
                          data=dict(username='sakire', password='1234'),
                          follow_redirects = True)
    assert response.status_code == 200
    assert b"Student Sign in - ResearchApp" in response.data

def test_flogin_action(request,test_client,init_database):
    response = test_client.post('/FacultyLogin', 
                          data=dict(username='sakire', password='1234'),
                          follow_redirects = True)
    assert response.status_code == 200
    assert b"Faculty Main Page - ResearchApp" in response.data

def logout(test_client):
    return test_client.get('/logout', follow_redirects=True)

def new_user(uname, uemail,passwd):
    user = User(username=uname, email=uemail)
    user.set_password(passwd)
    return user