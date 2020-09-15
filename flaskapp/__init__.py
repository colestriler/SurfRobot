from flask import Flask
from flaskapp.config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
# from flask_login import LoginManager
from flask_mail import Mail


#  run python run.py
# CREATE EXTENSIONS OUTSIDE OF FUNCTION BUT INITIALIZE INSIDE FUNCTION WITH THE APPLICATION
db = SQLAlchemy() #represent database structure as classes -> called MODELS
bcrypt = Bcrypt()
# login_manager = LoginManager()
# login_manager.login_view = 'users.login' # telling extension where the login route is located, login is fn name for route
# login_manager.login_message_category = 'info' # blue info alert in bootstrap
mail = Mail() #initializes extension



def create_app(config_class=Config):
    app = Flask(__name__)  # special variable in python that's the name of the module
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    # login_manager.init_app(app)
    mail.init_app(app)

    # REGISTER BLUEPRINTS
    from flaskapp.bots.app import bots
    app.register_blueprint(bots)

    return app



