from __future__ import print_function
import sys
from flask import Blueprint
from flask import render_template, flash, redirect, url_for, request
from config import Config

from app import db
from app.Model.models import Post
from app.Controller.forms import PostForm

bp_routes = Blueprint('routes', __name__)
bp_routes.template_folder = Config.TEMPLATE_FOLDER #'..\\View\\templates'


@bp_routes.route('/', methods=['GET'])
@bp_routes.route('/index', methods=['GET'])
def index():
    posts = Post.query.order_by(Post.timestamp.desc())
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
