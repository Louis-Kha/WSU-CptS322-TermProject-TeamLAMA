from __future__ import print_function
import sys
from flask import Blueprint
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_required, login_manager
from config import Config

from app import db
from app.Model.models import Post, Tag, postTags, researchPos, User, application
from app.Controller.forms import PostForm, EmptyForm, SortForm, ResearchForm, ApplicationForm
from app.Model.models import * #Post, Tag, postTags, researchPos, User
from app.Controller.forms import PostForm, EmptyForm, SortForm, ResearchForm, EditForm

bp_routes = Blueprint('routes', __name__)
bp_routes.template_folder = Config.TEMPLATE_FOLDER 

@bp_routes.route('/', methods=['GET']) # loads to the index page
@bp_routes.route('/index', methods=['GET'])
@login_required
def index():
    if current_user.isfaculty:
        return redirect(url_for('routes.facultyindex'))
    else:
        return redirect(url_for('routes.studentindex'))



@bp_routes.route('/postposition', methods=['GET','POST'])
def postposition():
    newPost = ResearchForm()
    if newPost.validate_on_submit():
      newPosted = researchPos(title = newPost.title.data, 
                            researchDesc = newPost.researchDesc.data, 
                            requiredHours = newPost.requiredHours.data, 
                            startEndDate = newPost.startEndDate.data, 
                            requiredQualifications = newPost.requiredQualifications.data, 
                            researchFields = newPost.researchFields.data, 
                            faculty_id = current_user.id, 
                            facultyName = current_user.lastName)
      db.session.add(newPosted)
      db.session.commit()
      flash("New Research Position Has Been Created!")
      return redirect (url_for('routes.index'))
    return render_template('create.html', title="New Research Position", form = newPost)

# created by Al
@bp_routes.route('/studentindex', methods=['GET', 'POST'])
@login_required
def studentindex():
    sform = SortForm()
    posts = researchPos.query.order_by(researchPos.timestamp.desc())
    if request.method == 'POST':
        sform = SortForm(sort = sform.sort.choices)

        if sform.sort.data == 'DataBases':
            posts = researchPos.query.join(researchPostFieldTags, researchPos.researchFields).order_by(researchPostFieldTags.id)
        elif sform.sort.data == 'AI':
            posts = researchPos.query.join(researchPostFieldTags, researchPos.researchFields).order_by(researchPostFieldTags.name)
        elif sform.sort.data == 'System Security':
            posts = researchPos.query.join(researchPostFieldTags, researchPos.researchFields).order_by(researchPostFieldTags.id.desc())
    return render_template('studentindex.html', 
                            title = "Student Index",   
                            posts= posts.all(), 
                            sortform = sform)
    # posts = researchPos.query.order_by(researchPos.timestamp.desc())
    # return render_template('studentindex.html', title="Student Main Page", posts=posts.all())

# created by Al
@bp_routes.route('/facultyindex', methods=['GET'])
@login_required
def facultyindex():
    posts = researchPos.query.order_by(researchPos.timestamp.desc())
    return render_template('facultyindex.html', title="Faculty Main Page", posts=posts.all())

@bp_routes.route('/studentapply2/<researchPos_id>', methods=['GET', 'POST'])
def studentapply2(researchPos_id):
    appBool = 0 #FALSE
    position = researchPos.query.get(researchPos_id)
    applications = application.query.filter_by(researchPos_id = researchPos_id).all()
    for appChecking in applications:
        if current_user.id == appChecking.student_id:
            appBool = 1
    print(applications)
    print(appBool)
    return render_template('studentapp.html', title="Search App Portal", positions=position, applicants = applications, appBool = appBool)

@bp_routes.route('/studentapply/<researchPos_id>', methods=['GET', 'POST'])
def studentapply(researchPos_id):
    position = researchPos.query.get(researchPos_id)
    test = True
    #if current user is logged in as faculty they only see their own posts
    if User.get_status(User, test) == False:
        #something
        flash("Faculty member")
    else:
        flash("Student")
        #something
    posts = researchPos.query.order_by(researchPos.timestamp.desc())
    return render_template('studentapplication.html', title="Search App Portal", posts=posts.all())

#---------------------------------Added By Alex-----------------------------------------------------
@bp_routes.route('/display_profile', methods=['GET'])
#@login_required
def display_profile():
    return render_template('display_profile.html', title="User Profile", user = current_user)

# When the user clicks on a specific user link it will redirect them to the selected profile page
@bp_routes.route('/view_profile/<user_id>', methods=['GET', 'POST'])
#@login_required
def view_profile(user_id):
    viewStudent = User.query.get(user_id) # Gets all of the user's information and sets it to viewStudent class
    return render_template('view_profile.html', 
                        title="{}'s Profile".format(user_id), 
                        user = viewStudent)

@bp_routes.route('/edit_profile', methods=['GET','POST'])
# STILL WIP Waiting on the UserDB
def edit_profile(): # Loads the EditForm Class and lets the user edit/update their information
    eform = EditForm()
    if request.method == 'POST':
        if current_user.isfaculty == 0:
            current_user.username = eform.username.data
            current_user.wsuID = eform.wsuID.data
            current_user.firstName = eform.firstName.data
            current_user.lastName =eform.lastName.data
            current_user.knownLanguages = eform.knownLang.data 
            current_user.email = eform.email.data  
            current_user.address = eform.address.data
            current_user.phoneNumber = eform.phoneNumber.data
            current_user.cumGPA = eform.cumGPA.data
            current_user.techCourseGPA = eform.techCourseGPA.data
            current_user.experienceDesc = eform.experienceDesc.data
            current_user.userResearchFields = eform.rFieldTags.data
            current_user.userMajor = eform.userMajors.data
            current_user.gradDate = eform.gradDate.data
            current_user.userTechnicalCourses = eform.userTechnicalCourses.data
                
        else: #User is faculty
            current_user.username = eform.username.data
            current_user.wsuID = eform.wsuID.data
            current_user.firstName = eform.firstName.data
            current_user.lastName =eform.lastName.data
            current_user.knownLanguages = eform.knownLang.data 
            current_user.email = eform.email.data  
            current_user.address = eform.address.data
            current_user.phoneNumber = eform.phoneNumber.data            


        current_user.set_password(eform.password.data)
        db.session.add(current_user)
        db.session.commit()
        flash("Changes have been saved.")
        return redirect(url_for('routes.display_profile'))

    elif request.method == 'GET': #Populate boxes with user data
        eform.username.data = current_user.username
        eform.wsuID.data = current_user.wsuID
        eform.firstName.data = current_user.firstName
        eform.lastName.data = current_user.lastName
        eform.address.data = current_user.address
        eform.knownLang.data = current_user.knownLanguages
        eform.email.data = current_user.email
        eform.phoneNumber.data = current_user.phoneNumber
        eform.cumGPA.data = current_user.cumGPA
        eform.techCourseGPA.data = current_user.techCourseGPA
        eform.experienceDesc.data = current_user.experienceDesc
        eform.rFieldTags.data = current_user.userResearchFields
        eform.userMajors.data = current_user.userMajor
        eform.gradDate.data = current_user.gradDate
        eform.userTechnicalCourses.data = current_user.userTechnicalCourses

    else:
        pass
    return render_template('edit_profile.html', title='Edit Profile', form=eform, user = current_user)

#---------------------------------------------------------------------------------------------------

@bp_routes.route('/researchApply/<currentResearch_id>', methods=['GET', 'POST'])
def researchApply(currentResearch_id):
    #used in studentapp.html with (current_user) to maintain student id in their research application
    #research_id = researchPos.query.get(currentResearch_id)
    newApply = ApplicationForm()
    if newApply.validate_on_submit():
      newApplied = application(name = newApply.name.data, description = newApply.description.data, reference = newApply.reference.data, student_id = current_user.id, researchPos_id = currentResearch_id)
      db.session.add(newApplied)
      db.session.commit()
      flash("You Have Successfully Applied To A New Position!")
      return redirect (url_for('routes.studentindex'))
    return render_template('researchapply.html', title="Search App Portal", form = newApply)





@bp_routes.route('/viewPosition/<researchPos_id>', methods=['GET', 'POST'])
def viewPosition(researchPos_id):
    position = researchPos.query.get(researchPos_id)
    applications = application.query.filter_by(researchPos_id = researchPos_id).all()
    return render_template('viewposition.html', title="Search App Portal", positions=position, applicants = applications)

@bp_routes.route('/viewapplication/<application_id>', methods=['GET', 'POST'])
def viewApplication(application_id):
    applications = application.query.get(application_id)
    viewStudent = User.query.get(applications.student_id)
    return render_template('viewapplication.html', title="Search App Portal", application=applications, user = viewStudent)