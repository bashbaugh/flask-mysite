from datetime import datetime
from flask import render_template, session, redirect, url_for
from flask_login import login_required
from . import main
# from .forms import NameForm
from .. import db
# from ..models import User

@main.route('/')
def index():
    return render_template('index.html') 
    # return "HELLO"

@main.route('/about-me')
def about():
	return render_template('about.html')

@main.route('/member-news')
@login_required
def member_news():
    return "hello"

