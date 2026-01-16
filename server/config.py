import os
from flask import Flask
from flask_migrate import Migrate
from server.models import db

def create_app():
    app = Flask(__name__)

    basedir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(basedir, '..', 'instance', 'app.db')

    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.json.compact = False

    db.init_app(app)
    Migrate(app, db)

    return app
