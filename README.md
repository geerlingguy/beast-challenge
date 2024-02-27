# Beast Challenge

A control system for the buttons and in-room LEDs in MrBeast's [Ages 1 - 100 Fight For $500,000](https://www.youtube.com/watch?v=FM7Z-Xq8Drc) video.

My [behind-the-scenes video about the 1-100 challenge](https://www.youtube.com/watch?v=wsV_C9cMf8A) contains a lot more detail:

<p align="center"><a href="https://www.youtube.com/watch?v=wsV_C9cMf8A"><img alt="Jeff Geerling with a relay board on MrBeast set" src="/resources/jeff-mrbeast-set-relays.jpg" height="auto" width="610"></a></p>

There is also a blog post about the project: [100 SBCs, Python Flask, and two NUCs for MrBeast](https://www.jeffgeerling.com/blog/2023/100-sbcs-python-flask-and-two-nucs-mrbeast).

## Screenshots

![Tally Page Example](/resources/screenshots/tally-example.png)

![Bar Graph Example](/resources/screenshots/bar-graph-example.png)

![Overview UI](/resources/screenshots/overview-example.png)

![Room Votes UI](/resources/screenshots/room-votes-example.png)

![Room Lights UI](/resources/screenshots/room-lights-example.png)

![Test Mode UI](/resources/screenshots/test-mode-example.png)

## Leader app

The Leader app (inside `leader-app/`) runs on a central server that manages state, provides output for a display, and provides controls to manage state (e.g. starting/ending a round, advancing to a new round).

The Leader app is a Flask app built with Python.

To develop it locally, run:

  1. `cd leader-app`
  2. `pipenv shell` (requires `pipenv`, install with `pip3 install pipenv`)
  3. `pip install -r requirements.txt`
  4. Initialize the database: `python3 init_db.py`
  5. Run app: `FLASK_APP=app FLASK_DEBUG=true flask run` (add `--host=0.0.0.0` to make it accessible over the network)

Visit the app at http://127.0.0.1:5000

## Countdown app

The Countdown app (inside `countdown-app/`) runs on a central server that manages state, provides output for a display, and provides controls to manage state (e.g. setting the time interval for a button press, resetting timers).

The Countdown app is a Flask app built with Python.

To develop it locally, run:

  1. `cd countdown-app`
  2. `pipenv shell` (requires `pipenv`, install with `pip3 install pipenv`)
  3. `pip install -r requirements.txt`
  4. Initialize the database: `python3 init_db.py`
  5. Run app: `FLASK_APP=app FLASK_DEBUG=true flask run` (add `--host=0.0.0.0` to make it accessible over the network)

Visit the app at http://127.0.0.1:5000

## Production 'Farmer' Deployment (Leader and Button apps)

The Leader and Button apps will run on the main server NUC, with a hot spare backup server available should the need arise.

The `automation/farmer-control.yml` file contains the Ansible playbook to set up the server, install the app, and run it.

Make sure you have Ansible installed on a machine on the same network: `pip3 install ansible`.

Then make sure the leader and spare's IP addresses are both entered in the `[leader]` section of the `hosts.ini` file. For SSH authentication, the private key is available inside the Notion doc—you should add it to your `ssh` keychain with `ssh-add ~/path/to/private_key`

Then run the Ansible playbook:

```
ansible-playbook farmer-control.yml
```

> For testing, bring up a Docker Ubuntu container with `docker run -d --volume=/sys/fs/cgroup:/sys/fs/cgroup:rw --cgroupns=host --privileged --name farmer geerlingguy/docker-ubuntu2204-ansible:latest /usr/sbin/init`, then set the hostname line for the farmer to:
>
> ```
> farmer ansible_connection=community.general.docker role=leader
> ```
>
> Then run the playbook: `ansible-playbook farmer-control.yml`

### Initializing the Database

To initialize (or reset) the database, run the Ansible playbook:

```
ansible-playbook farmer-reset-database.yml
```

To _manually_ initialize the database (e.g. the first time you run the application in production), log into the server and run:

```
# For leader app
docker exec beast-challenge_leader_1 python3 init_db.py

# For countdown app
docker exec countdown-app_countdown_1 python3 init_db.py
```

### Running the Apps on a Potato

If you want to test things on a Potato running Armbian instead of a NUC running Ubuntu, you can do that too! Just change the `[farmer]` section inside `hosts.ini` to have a line for the Potato where you want the server running.

Run the Ansible `farmer-control.yml` playbook, initialize the database, and away you go!

If you want to plug an HDMI display into the Potato and use Firefox to browse the web UI, you can install the LXDE Desktop (Armbian doesn't come with a desktop environment out of the box):

```
sudo apt install lxdm vanilla-gnome-desktop firefox
```

If you get a popup asking you to select a default display manager, choose `gdm3` then continue. See [this post](https://forum.armbian.com/topic/5298-le-potato-general-topics/page/3/#comment-125790) for more info.

> Note: During testing, some things need tweaking depending on your setup. For example, one Le Potato I was using to demo some button functionality didn't have the relay HAT attached. The default 'Live Colors' configuration resulted in an exception, because the Potato couldn't find the I2C relay HAT to control! So... you might have to do a little Python spelunking if you want to do things out of the norm. In my case, I just had to disable 'Live Colors' in that test round.

## Room app

The Room app (inside `room-app`) runs on every one of the 100x rooms where SBCs are set up to run the room controls.

The app controls the following:

  1. Buttons and Button LEDs (GPIO digital inputs)
  2. RGBW LED light strip control (GPIO digital outputs)

To deploy the app, see the _Automation for Controlling the Potatoes_ section below.

### 52Pi EP-0099 Relay Considerations

The [52Pi EP-0099 Relay](https://amzn.to/49wu65O) is a 4-channel I2C-controlled relay HAT that works with Le Potato. We bought it for two reasons:

  1. It is easy to install (as a HAT)
  2. It was available on short notice

The relays used are [`HK4100F-DC5V-SHG`](https://www.lcsc.com/product-detail/Power-Relays_Ningbo-Keke-New-Era-Appliance-HK4100F-DC5V-SHG_C12072.html), and according to the datasheet, they can only handle 3A at 30V, so they are not rated for the current we'll be drawing.

Because of that, we daisy chained another set of relays rated at 10A at 30V. The relays are controlled via code in the Room app scripts.

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

#### Maintaining the Potato farm

There are a variety of maintenance tasks in the maintenance playbook:

```
# Reboot spuds:
ansible-playbook spud-maintain.yml -e '{"spud_reboot":true}'

# Stop all services on the spuds:
ansible-playbook spud-maintain.yml -e '{"service_stop":true}'

# Start all services on the spuds:
ansible-playbook spud-maintain.yml -e '{"service_start":true}'
```

### Initializing the Farmer

Assuming either Ubuntu Desktop or Ubuntu Server is installed on the Farmer, make sure you have SSH access, and install your SSH key on the `beast-admin` or `admin` account. Then run the Ansible playbook to set it up:

```
ansible-playbook farmer-control.yml
```

You may need to add `-K` the first time the playbook runs, to supply the sudo password (since by default Ubuntu doesn't allow passwordless sudo).

### Switching modes

If you need to switch from the `leader` app to `countdown` (or vice-versa), run the `switch-modes.yml` playbook. For example, if the `leader` app is running, and you would like to switch to `countdown`:

```
ansible-playbook switch-modes.yml -e challenge_mode=countdown
```

## Critical Test Scenarios

  1. Live round is open, accepts multiple votes, make sure multiple votes can be made per room.
  2. Live round is open, doesn't accept multiple votes, make sure only first vote is accepted.
  3. Live round is closed, make sure no votes are accepted.

## License

GPLv2 or later

Any MrBeast trademarks and references are all rights reserved and must be removed if redistributing or re-using this software outside of the MrBeast organization.
