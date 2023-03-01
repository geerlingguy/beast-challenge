# Beast Game

A game control system for Mr. Beast.

Relevant resources:

  - [Notion Doc](https://www.notion.so/networkchuck/Mr-Beast-Raspberry-Pi-Project-24b504815a63434fbceb8776cfc94d49?pvs=4)

## Leader app

The Leader app (inside `leader-app/`) runs on a central server that manages game state, provides output for a display, and provides controls to manage game state (e.g. starting/ending a round, advancing to a new round).

The Leader app is a Flask app built with Python.

To develop it locally, run:

  1. `cd leader-app`
  2. `pipenv shell` (requires `pipenv`, install with `pip3 install pipenv`)
  3. `pip install -r requirements.txt`
  4. Initialize the database: `python3 init_db.py`
  5. Run app: `FLASK_APP=app FLASK_DEBUG=true flask run`

Visit the app at http://127.0.0.1:5000
