from flask import redirect, render_template
from . import main

@main.route('/login')
def loginredirect():
    return redirect('/account/login')
