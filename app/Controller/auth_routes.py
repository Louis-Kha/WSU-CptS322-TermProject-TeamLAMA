from __future__ import print_function
import sys
from flask import Blueprint
from flask import render_template, flash, redirect, url_for
from flask_sqlalchemy import sqlalchemy
from flask_login import login_user, login_required, current_user, logout_user 
from config import Config
from app.Controller.auth_forms import RegistrationForm, LoginForm
from app.Model.models import User

from app import db

bp_auth = Blueprint('auth', __name__)
bp_auth.template_folder = Config.TEMPLATE_FOLDER 

# lets try to make this one a student login
@bp_auth.route('/login', methods=['GET', 'POST'])
def login():
    lform = LoginForm()
    if current_user.is_authenticated: 
        return redirect(url_for('routes.index'))
    if lform.validate_on_submit():
        user = User.query.filter_by(username = lform.username.data).first()
        if (user is None) or (user.get_password(lform.password.data) == False) or (user.get_status(lform.isfaculty.data) == False):
            flash('Invalid Username or Password')
            return redirect(url_for('auth.login'))
        login_user(user, remember = lform.remember.data)
        return redirect(url_for('routes.index'))
    return render_template('login.html', title = 'Student Sign in', form = lform)

@bp_auth.route('/FacultyLogin', methods=['GET', 'POST'])
def FacultyLogin():
    lform = LoginForm()
    if current_user.is_authenticated: 
        return redirect(url_for('routes.index'))
    if lform.validate_on_submit():
        user = User.query.filter_by(username = lform.username.data).first()
        if (user is None) or (user.get_password(lform.password.data) == False) or (user.get_status(lform.isfaculty.data) == True):
            flash('Invalid Username or Password')
            return redirect(url_for('auth.FacultyLogin'))
        login_user(user, remember = lform.remember.data)
        return redirect(url_for('routes.index'))
    return render_template('Facultylogin.html', title = 'Faculty Sign in', form = lform)

@bp_auth.route('/logout', methods = ['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('routes.index'))

# student register
@bp_auth.route('/register', methods=['GET', 'POST'])
def register():
    rform = RegistrationForm()
    if rform.validate_on_submit():
        user = User(username = rform.username.data, email = rform.email.data, isfaculty = False)
        user.set_password(rform.password1.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash('You are now a registered user {}!'.format(user.username))
        return redirect(url_for('auth.login'))
    return render_template('register.html', form = rform)

@bp_auth.route('/Facultyregister', methods=['GET', 'POST'])
def Facultyregister():
    rform = RegistrationForm()
    if rform.validate_on_submit():
        user = User(username = rform.username.data, email = rform.email.data, isfaculty = True)
        user.set_password(rform.password1.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash('You are now a registered user {}!'.format(user.username))
        return redirect(url_for('auth.FacultyLogin'))
    return render_template('Facultyregister.html', form = rform)
