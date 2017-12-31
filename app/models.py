from werkzeug.security import generate_password_hash, check_password_hash
from . import db

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(32), unique=True, index=True, nullable=False)


