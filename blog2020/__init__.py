from flask import Flask

from config import Config

# Imports for Flask DB and Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Import for Flask Login
from flask_login import LoginManager

app = Flask(__name__)

app.config.from_object(Config)

# Wrap Our Flask App inside of SQLAlchemy
db = SQLAlchemy(app)
migrate = Migrate(app,db)

# Login Flow Config
login = LoginManager(app)
login.login_view = 'login' # This specifies what page to load for non-authenticated users


from blog2020 import routes,models