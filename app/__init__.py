from flask import Flask, render_template
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager

mail = Mail()
moment = Moment()
db = SQLAlchemy()
lm = LoginManager()
lm.session_protection = 'strong'
lm.login_view  = 'account.login'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    lm.init_app(app)

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from app.account import account as account_blueprint
    app.register_blueprint(account_blueprint, url_prefix='/account')
    

    return app
