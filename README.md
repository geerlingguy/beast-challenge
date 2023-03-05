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

## Room app

The Room app runs on every one of the 100x rooms where SBCs are set up to run the room controls.

The app controls the following:

  1. Buttons and Button LEDs (GPIO digital inputs)
  2. RGBW LED light strip control (GPIO digital outputs)

TODO: Build the app

## Automation for Controlling the Rooms

The `automation` directory contains Ansible configuration for managing the fleet of 100 room nodes. We have to use something like Ansible because managing 100 nodes by hand would be insane.

TODO: Build the automation

## Screenshots

![Tally Page Example](/resources/screenshots/tally-example.png)

![Overview UI](/resources/screenshots/overview-example.png)

![Room Votes UI](/resources/screenshots/room-votes-example.png)

![Room Lights UI](/resources/screenshots/room-lights-example.png)

![Test Mode UI](/resources/screenshots/test-mode-example.png)

## Critical Test Scenarios

  1. Active round is open, accepts multiple votes, make sure multiple votes can be made per room.
  2. Active round is open, doesn't accept multiple votes, make sure only first vote is accepted.
  3. Active round is closed, make sure no votes are accepted.
