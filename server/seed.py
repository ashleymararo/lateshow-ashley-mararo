from server.config import create_app, db
from server.models import Episode, Guest, Appearance

app = create_app()

# Sample data to seed
episodes_data = [
    {"number": 1, "date": "1/11/99"},
    {"number": 2, "date": "1/12/99"},
    {"number": 3, "date": "1/13/99"},
]

guests_data = [
    {"name": "Michael J. Fox", "occupation": "actor"},
    {"name": "Sandra Bernhard", "occupation": "Comedian"},
    {"name": "Tracey Ullman", "occupation": "television actress"},
]

appearances_data = [
    {"episode_number": 1, "guest_name": "Michael J. Fox", "rating": 4},
    {"episode_number": 2, "guest_name": "Tracey Ullman", "rating": 5},
    {"episode_number": 2, "guest_name": "Sandra Bernhard", "rating": 3},
]

def seed_database():
    with app.app_context():
        # Clear existing data
        Appearance.query.delete()
        Episode.query.delete()
        Guest.query.delete()
        db.session.commit()

        # Add episodes
        episodes = []
        for e in episodes_data:
            episode = Episode(number=e["number"], date=e["date"])
            db.session.add(episode)
            episodes.append(episode)
        db.session.commit()

        # Add guests
        guests = []
        for g in guests_data:
            guest = Guest(name=g["name"], occupation=g["occupation"])
            db.session.add(guest)
            guests.append(guest)
        db.session.commit()

        # Add appearances
        for a in appearances_data:
            episode = Episode.query.filter_by(number=a["episode_number"]).first()
            guest = Guest.query.filter_by(name=a["guest_name"]).first()
            appearance = Appearance(
                rating=a["rating"],
                episode=episode,
                guest=guest
            )
            db.session.add(appearance)
        db.session.commit()

        print("Database seeded successfully!")


if __name__ == "__main__":
    seed_database()
