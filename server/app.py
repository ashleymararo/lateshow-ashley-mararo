from server.config import create_app, db
from server.models import Episode, Guest, Appearance

app = create_app()

if __name__ == "__main__":
    app.run(port=5555, debug=True)
