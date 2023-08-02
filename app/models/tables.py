from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import random
import string


class User(db.Model, UserMixin):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(86), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    saved_passwords = db.relationship("Password", backref="owner", lazy=True)

    def __init__(self, email, password):
        self.email = email
        self.password = generate_password_hash(password)

    def verify_password(self, pwd):
        """
        Verifies that the hash of the password entered by the user is
        compatible with the database
        """
        return check_password_hash(self.password, pwd)


class Password(db.Model):
    __tablename__ = "password"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(86), nullable=False)
    username = db.Column(db.String(86))
    pwd = db.Column(db.String(120))
    url = db.Column(db.String(120))
    category = db.Column(db.String(20), default="No category")
    id_owner = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def gen_pwd(self, length_pwd, min_numbers, min_special):
        """Generate password"""
        length_pwd -= min_numbers + min_special
        self.pwd = (
            random.choices(string.ascii_letters, k=length_pwd)
            + random.choices(string.digits, k=min_numbers)
            + random.choices("!@#$%^&*", k=min_special)
        )
        random.shuffle(self.pwd)
        self.pwd = "".join(self.pwd)
        return self.pwd
