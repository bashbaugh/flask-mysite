from flask import render_template
from . import account

@account.route('/login')
def login():
    return "login page"
