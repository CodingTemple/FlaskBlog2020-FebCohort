from blog2020 import app, db

# Import for Werkzeug Security
from werkzeug.security import generate_password_hash, check_password_hash

# import for Date Time Module
from datetime import datetime

# Import for login_manager
from blog2020 import login
from flask_login import UserMixin

# Expose the current user_manager user_login function as a decorator
@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(150),nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    post = db.relationship('Post', backref='author', lazy = True)

    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = self.set_password(password)

    def __repr__(self):
        return f'{self.username} has been created with {self.email}'

    def set_password(self,password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash


class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200))
    content = db.Column(db.String(300))
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self,title,content,user_id):
        self.title = title
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return f'The Title of the post is {self.title} and the user is {self.user_id}'