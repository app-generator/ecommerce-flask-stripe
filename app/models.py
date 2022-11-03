from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    username = db.Column(
        db.String(100),
        nullable=False,
        unique=True
    )
    email = db.Column(
        db.String(40),
        unique=True,
        nullable=False
    )
    password = db.Column(
        db.String(200),
        primary_key=False,
        unique=False,
        nullable=True
	)

    def get_id(self):
        return self.username
    

