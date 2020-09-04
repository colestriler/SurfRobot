from flask import Flask
from flaskapp.config import Config




def create_app(config_class=Config):
    app = Flask(__name__)  # special variable in python that's the name of the module
    app.config.from_object(Config)

    # REGISTER BLUEPRINTS
    from flaskapp.main.routes import main
    from flaskapp.bots.app import bots
    app.register_blueprint(main)
    app.register_blueprint(bots)

    return app



