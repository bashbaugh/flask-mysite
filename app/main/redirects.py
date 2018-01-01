from flask import redirect, render_template, url_for
from . import main

@main.route('/login')
def loginr():
    return redirect(url_for('account.login'))

@main.route('/logout')
def logoutr():
    return redirect(url_for('account.logout'))
