# LateShow Phase 4 Project

## Description

This is a Flask backend app for managing episodes, guests, and appearances of a talk show.

## Features

* Stores Episodes, Guests, and their Appearances
* Seed script to populate sample data
* Uses SQLite database (`instance/app.db`)

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone <your-repo-url>
   cd lateshow-ashley-mararo
   ```

2. Create virtual environment and install dependencies:

   ```bash
   pipenv install
   pipenv shell
   ```

3. Initialize database and migrations:

   ```bash
   flask db init     # only if migrations folder isn't there
   flask db migrate
   flask db upgrade
   ```

4. Seed database:

   ```bash
   python -m server.seed
   ```

5. Run the app:

   ```bash
   export FLASK_APP=server.config
   flask run
   ```

## Testing

Use flask shell to query models:

```python
from server.models import Episode, Guest, Appearance
Episode.query.all()
Guest.query.all()
Appearance.query.all()
```

Or hit API endpoints (if routes exist).

## Author

Ashley Mararo
