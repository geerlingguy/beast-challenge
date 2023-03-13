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

## The Button app

TODO: Same as above, but add `-p 5005` and access at http://127.0.0.1:5005

## Production 'Farmer' Deployment (Leader and Button apps)

The Leader and Button apps will run on the main server NUC, with a hot spare backup server available should the need arise.

The `automation/farmer-control.yml` file contains the Ansible playbook to set up the server, install the app, and run it.

Make sure you have Ansible installed on a machine on the same network: `pip3 install ansible`.

Then make sure the leader and spare's IP addresses are both entered in the `[leader]` section of the `hosts.ini` file. For SSH authentication, the private key is available inside the Notion doc—you should add it to your `ssh` keychain with `ssh-add ~/path/to/private_key`

Then run the Ansible playbook:

```
ansible-playbook farmer-control.yml
```

You can control which app is active by overriding it with the extra var `running_app`. For example, if `leader-app` is currently running, switch to `the-button` with:

```
ansible-playbook farmer-control.yml -e "running_app=the-button" --tags app
```

> For testing, bring up a Docker Ubuntu container with `docker run -d --volume=/sys/fs/cgroup:/sys/fs/cgroup:rw --cgroupns=host --privileged --name farmer geerlingguy/docker-ubuntu2204-ansible:latest /usr/sbin/init`, then set the hostname line for the farmer to:
>
> ```
> farmer ansible_connection=community.general.docker role=leader
> ```
>
> Then run the playbook: `ansible-playbook farmer-control.yml`

## Room app

The Room app (inside `room-app`) runs on every one of the 100x rooms where SBCs are set up to run the room controls.

The app controls the following:

  1. Buttons and Button LEDs (GPIO digital inputs)
  2. RGBW LED light strip control (GPIO digital outputs)

To deploy the app, see the _Automation for Controlling the Potatoes_ section below.

### 52Pi EP-0099 Relay Considerations

The 52Pi EP-0099 Relay is a 4-channel I2C-controlled relay HAT that works with Le Potato. We bought it for two reasons:

  1. It is easy to install (as a HAT)
  2. It was available on short notice

The relays used are `HK4100F-DC5V-SHG`, and according to the datasheet, they can only handle 3A at 30V, so they are not rated for the current we'll be drawing.

Because of that, we will daisy chain another set of relays that are rated at 10A at 30V. For wiring diagrams, refer to the Notion doc. The relays are controlled via code in the Room app scripts.

There is also a convenient `light.py` script which allows for setting a room color directly on the device, e.g. `./light.py white`. Note that you may need to temporarily stop the lighting control script: `sudo systemctl stop light-control`.

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

Assuming either Ubuntu Desktop or Ubuntu Server is installed on the Farmer, make sure you have SSH access, and install your SSH key on the `beast-admin` or `admin` account. Then run the Ansible playbook to set it up:

```
ansible-playbook farmer-control.yml
```

You may need to add `-K` the first time the playbook runs, to supply the sudo password (since by default Ubuntu doesn't allow passwordless sudo).

## Screenshots

![Tally Page Example](/resources/screenshots/tally-example.png)

![Bar Graph Example](/resources/screenshots/bar-graph-example.png)

![Overview UI](/resources/screenshots/overview-example.png)

![Room Votes UI](/resources/screenshots/room-votes-example.png)

![Room Lights UI](/resources/screenshots/room-lights-example.png)

![Test Mode UI](/resources/screenshots/test-mode-example.png)

## Critical Test Scenarios

  1. Live round is open, accepts multiple votes, make sure multiple votes can be made per room.
  2. Live round is open, doesn't accept multiple votes, make sure only first vote is accepted.
  3. Live round is closed, make sure no votes are accepted.
