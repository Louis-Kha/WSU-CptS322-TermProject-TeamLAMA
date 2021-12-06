from __future__ import print_function
import sys
from datetime import timedelta
from flask import Blueprint
from flask import render_template, flash, redirect, url_for, session
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
    # session.permanent = False
    lform = LoginForm()
    if (current_user.is_authenticated): 
        return redirect(url_for('routes.studentindex')) # changed here
    if lform.validate_on_submit():
        user = User.query.filter_by(username = lform.username.data).first()
        if (user is None) or (user.get_password(lform.password.data) == False) or (user.get_status(lform.isfaculty.data) == False):
            flash('Invalid Username or Password')
            return redirect(url_for('auth.login'))
        login_user(user, remember = True)
        # login_user(user, remember = False)
        return redirect(url_for('routes.studentindex')) # changed here
    return render_template('login.html', title = 'Student Sign in', form = lform)

@bp_auth.route('/FacultyLogin', methods=['GET', 'POST'])
def FacultyLogin():
    lform = LoginForm()
    if current_user.is_authenticated: 
        return redirect(url_for('routes.facultyindex')) # changed here
    if lform.validate_on_submit():
        user = User.query.filter_by(username = lform.username.data).first()
        if (user is None) or (user.get_password(lform.password.data) == False) or (user.get_status(lform.isfaculty.data) == True):
            flash('Invalid Username or Password')
            return redirect(url_for('auth.FacultyLogin'))
        login_user(user, remember = True)
        return redirect(url_for('routes.facultyindex')) # changed here
    return render_template('Facultylogin.html', title = 'Faculty Sign in', form = lform)

@bp_auth.route('/logout', methods = ['GET'])
@login_required
def logout():
    tmp = ""
    if current_user.isfaculty:
        tmp = 'auth.FacultyLogin'
        # return redirect(url_for('routes.facultyindex'))
    else:
        tmp = 'auth.login'
        # return redirect(url_for('routes.studentindex'))
    logout_user()
    # session.clear()
    return redirect(url_for(tmp))

# student register
@bp_auth.route('/register', methods=['GET', 'POST'])
def register():
    rform = RegistrationForm()
    if rform.validate_on_submit():
        user = User(username = rform.username.data, 
                    wsuID = rform.wsuID.data,
                    firstName = rform.firstName.data, 
                    lastName = rform.lastName.data,
                    email = rform.email.data, 
                    address = rform.address.data,
                    phoneNumber = rform.phoneNumber.data,
                    isfaculty = False,
                    isnotfaculty = True)
        user.set_password(rform.password1.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash('You are now a registered user {}!'.format(user.username))
        return redirect(url_for('auth.login'))
    return render_template('register.html', form = rform)

# Faculty Register
@bp_auth.route('/Facultyregister', methods=['GET', 'POST'])
def Facultyregister():
    rform = RegistrationForm()
    if rform.validate_on_submit():
        user = User(username = rform.username.data, 
                    wsuID = rform.wsuID.data,
                    firstName = rform.firstName.data, 
                    lastName = rform.lastName.data,
                    email = rform.email.data, 
                    address = rform.address.data,
                    phoneNumber = rform.phoneNumber.data,
                    isfaculty = True,
                    isnotfaculty = False)
        user.set_password(rform.password1.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash('You are now a registered user {}!'.format(user.username))
        return redirect(url_for('auth.FacultyLogin'))
    return render_template('Facultyregister.html', form = rform)
