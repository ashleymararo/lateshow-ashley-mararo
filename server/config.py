import os
from flask import Flask, jsonify
from flask_migrate import Migrate
from server.models import db, Episode, Guest, Appearance

def create_app():
    app = Flask(__name__)

    basedir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(basedir, '..', 'instance', 'app.db')
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.json.compact = False

    db.init_app(app)
    Migrate(app, db)

    @app.route("/")
    def home():
        return "LateShow API is running!"

    @app.route("/episodes")
    def get_episodes():
        episodes = Episode.query.all()
        return jsonify([{"id": e.id, "number": e.number, "date": e.date} for e in episodes])

    @app.route("/guests")
    def get_guests():
        guests = Guest.query.all()
        return jsonify([{"id": g.id, "name": g.name, "occupation": g.occupation} for g in guests])

    @app.route("/appearances")
    def get_appearances():
        appearances = Appearance.query.all()
        return jsonify([{
            "id": a.id,
            "episode_number": a.episode.number,
            "guest_name": a.guest.name,
            "rating": a.rating
        } for a in appearances])

    return app
