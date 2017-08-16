from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_compress import Compress
from config import config


compress = Compress()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    #config[config_name].init_app(app)
    compress.init_app(app)
    db.init_app(app)
    db.app = app

    from web.users import users as users_blueprint
    app.register_blueprint(users_blueprint, url_prefix='/v1')
    return app
