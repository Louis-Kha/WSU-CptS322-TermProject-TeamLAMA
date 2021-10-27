from __future__ import print_function
import sys
from flask import Blueprint
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_required
from config import Config

from app import db
from app.Model.models import Post, Tag, postTags
from app.Controller.forms import PostForm, EmptyForm, SortForm

bp_routes = Blueprint('routes', __name__)
bp_routes.template_folder = Config.TEMPLATE_FOLDER 

@bp_routes.route('/', methods=['GET'])
@bp_routes.route('/index', methods=['GET'])
@login_required
def index():
    eform = EmptyForm()
    sortform = SortForm()
    posts = Post.query.order_by(Post.timestamp.desc())
    return render_template('index.html', title="Smile Portal", posts=posts.all(), eform=eform, sortform = sortform)

# @bp_routes.route('/', methods=['GET'])
#@bp_routes.route('/studentview', methods=['GET'])
#@login_required
#def studentview():
#    return render_template('studentview.html')

# @bp_routes.route('/', methods=['GET'])
#@bp_routes.route('/facultyview', methods=['GET'])
#@login_required
#def studentview():
#    return render_template('facultyview.html')

@bp_routes.route('/createpost/', methods=['GET','POST'])
@login_required
def createpost():
    cform = PostForm()
    if cform.validate_on_submit():
        newPost = Post(title = cform.title.data, happiness_level = cform.happiness_level.data, body = cform.body.data,user_id = current_user.id)
        for t in cform.tag.data:
            newPost.tags.append(t)
        db.session.add(newPost)
        db.session.commit()
        flash('Post is created')
        return redirect(url_for('routes.index'))
    return render_template('create.html', form = cform)

@bp_routes.route('/like/<post_id>', methods=['POST'])
@login_required
def like(post_id):
    if request.method == 'POST':
        thepost = Post.query.filter_by(id = post_id).first()
        thepost.likes = 1 + thepost.likes 
        db.session.add(thepost)
        db.session.commit()
        return redirect(url_for('routes.index'))
    return render_template('index.html', title="Smile Portal", posts=posts.all())


@bp_routes.route('/postposition', methods=['GET','POST'])
def postposition():
    newPost = PostForm()
    if newPost.validate_on_submit():
      newPosted = Post(title = newPost.title.data, happiness_level = newPost.happiness_level.data, timecommitment = newPost.timecommitment.data, body = newPost.body.data)
      db.session.add(newPosted)
      db.session.commit()
      flash("New Research Position Has Been Created!")
      return redirect (url_for('routes.index'))
    return render_template('create.html', title="New Research Position", form = newPost)
