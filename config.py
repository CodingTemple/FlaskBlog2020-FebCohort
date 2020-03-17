import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Windows Documents\projects\blog2020\config.py
# Mac&Linux Documents/projects/blog2020/config.py

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess this'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False