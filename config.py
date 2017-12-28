# my website's configuration
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or "jhvjha6rUjhvdu73tuyfuyfRU&6rtfyrkd75ytk,jhg,fuyw7f2twa66&$s"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # APP_MAIL_SENDER = 'Benjaminashbaugh.com admin <ashbau.benjam19@svvsd.org>'
    APP_ADMIN = os.environ.get('APP_ADMIN')

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI =\
        'sqlite:///' + os.path.join(basedir, 'db.sqlite')

config = {
    'development' : DevelopmentConfig,
    # other

    'default' : DevelopmentConfig
}
