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
  5. Run app: `FLASK_APP=app FLASK_DEBUG=true flask run` (add `--host=0.0.0.0` to make it accessible over the network)

Visit the app at http://127.0.0.1:5000

## Room app

The Room app runs on every one of the 100x rooms where SBCs are set up to run the room controls.

The app controls the following:

  1. Buttons and Button LEDs (GPIO digital inputs)
  2. RGBW LED light strip control (GPIO digital outputs)

TODO: Build the app

### 52Pi EP-0099 Relay Considerations

The 52Pi EP-0099 Relay is a 4-channel I2C-controlled relay HAT that works with Le Potato. We bought it for two reasons:

  1. It is easy to install (as a HAT)
  2. It was available on short notice

The relays used are `HK4100F-DC5V-SHG`, and according to the datasheet, 

## Automation for Controlling the Potatoes

The `automation` directory contains Ansible configuration for managing both the main server (`farmer`) and the fleet of 100 room nodes (`potatoes`, sometimes referred to as `spuds`). We have to use something like Ansible because managing 100 nodes by hand would be insane.

Make sure you have Ansible installed on a machine on the same network: `pip3 install ansible`

### Initializing a Le Potato (the 'Spud')

For first-time setup of a new Le Potato (assuming you've already booted it and set up the `admin` user account following Armbian's wizard), do the following:

  1. `cd automation`
  2. `ansible-playbook spud-control.yml -k -K -e '{"run_upgrades": true}'`
  3. Enter the default `admin` password (and then press enter to re-use it for `BECOME`).
  4. Wait for the playbook to complete.

#### Re-running the `spud-control.yml` playbook

For future runs, assuming you have the private key in your agent (`ssh-add [path-to-key]`), you can just run the following:

```
ansible-playbook spud-control.yml
```

The playbook is configured to be idempotent, so we should be able to run it live if we need to quickly patch all 100 rooms!

#### Shutting down the Potato farm

To shut down all active Potatoes, run the command:

```
ansible potatoes -a "shutdown -H now" -b
```

### Initializing the Farmer

TODO.

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
