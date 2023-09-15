import sqlite3
import time
import random
import os
from datetime import datetime
from flask_cors import CORS, cross_origin
from flask_apscheduler import APScheduler
from flask import Flask, json, jsonify, request, flash, redirect, make_response, render_template, g

app = Flask(__name__)
app.config['SECRET_KEY'] = 'TviesCO6smUk7ZlNDm0ojBU7VeyPyGUn'
CORS(app)

# Scheduled task to expire rooms for which time has passed.
def check_room_status():
    with scheduler.app.app_context():
        rooms = get_rooms()
        for room in rooms:
            # Check all rooms that have not yet run out of time.
            if room['live'] and not room['time_expired']:
                latest_press = room_press_latest(room['room_id'])
                remaining_time = remaining_time_for_room(room['room_id'], latest_press['created'])
                # If time is up, expire the room.
                if remaining_time == 0:
                    conn = get_db_connection()
                    conn.execute("UPDATE rooms SET color = ?, time_expired = ? WHERE room_id = ?", ('red', 1, room['room_id']))
                    conn.commit()
                    conn.close()

# Configure the Scheduler to run every second.
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.add_job(func=check_room_status, args=[], trigger='interval', id='room_status', seconds=1)
scheduler.start()

if (__name__ == "__main__"):
    app.run()

# Allow the database path to be overridden
database_path = os.environ.get('FLASK_DATABASE_PATH') or 'countdown.sqlite'

def sqlite_select_as_dict(select_query, type = 'all'):
    try:
        conn = get_db_connection()
        things = conn.execute(select_query).fetchall()
        unpacked = [{k: item[k] for k in item.keys()} for item in things]
        if type == 'one':
            unpacked = unpacked[0]
        return unpacked
    except Exception as e:
        print(f"Failed to execute. Query: {select_query}\n with error:\n{e}")
        return []
    finally:
        conn.close()


def get_db_connection():
    conn = sqlite3.connect(database_path)
    conn.row_factory = sqlite3.Row
    return conn


def get_countdown_state():
    query = "SELECT * FROM countdown_state"
    return sqlite_select_as_dict(query, 'one')


def get_rooms():
    query = 'SELECT * FROM rooms'
    return sqlite_select_as_dict(query, 'all')


def get_room(room_id):
    conn = get_db_connection()
    room = conn.execute('SELECT * FROM rooms WHERE room_id = ?', room_id).fetchone()
    conn.close()
    return room


def valid_room_color_options():
    return ['off', 'white', 'red', 'green', 'blue']


def get_room_presses(room_id, limit = 10):
    conn = get_db_connection()
    conn.row_factory = sqlite3.Row
    presses = conn.execute('SELECT * FROM presses WHERE room_id = ? ORDER BY created DESC LIMIT ?', (room_id, limit)).fetchall()
    unpacked = [{k: item[k] for k in item.keys()} for item in presses]
    conn.close()
    return unpacked


def room_press_count(room_id):
    conn = get_db_connection()
    count = conn.execute('SELECT COUNT(*) FROM presses WHERE room_id = ?', (room_id,)).fetchone()
    conn.close()
    return count[0]


def room_press_latest(room_id):
    conn = get_db_connection()
    vote = conn.execute('SELECT * FROM presses WHERE room_id = ? ORDER BY created DESC', (room_id,)).fetchone()
    conn.close()
    return vote


def format_seconds_to_mmss(seconds):
    minutes = seconds // 60
    seconds %= 60
    return "%i:%02i" % (minutes, seconds)


def remaining_time_for_room(room_id, press_time):
    # If the room's time is expired, return 0 immediately.
    room = get_room((room_id,))
    if room['time_expired']:
        return 0

    current_time = getattr(g, '_current_time', None)
    if current_time is None:
        g._current_time = datetime.utcnow()
        current_time = g._current_time

    # Get current round's time_seconds / 'time per press'.
    countdown_state = get_countdown_state()
    time_per_press = countdown_state['time_seconds']

    # Get delta of seconds between current time and last button press.
    press_datetime = datetime.fromisoformat(press_time)
    time_difference = current_time - press_datetime
    time_difference_s = int(round(time_difference.total_seconds()))

    # Set remaining time based on the current time_seconds value.
    if time_difference_s > time_per_press:
        remaining_time = 0
    else:
        remaining_time = time_per_press - time_difference_s

    return remaining_time


def save_press(room_id):
    conn = get_db_connection()
    conn.execute('INSERT INTO presses (room_id) VALUES (?)', (room_id,))
    conn.commit()
    conn.close()


def update_color_for_room(color, room_id):
    conn = get_db_connection()
    conn.execute("UPDATE rooms SET color = ? WHERE room_id = ?", (color, room_id))
    conn.commit()
    conn.close()


# Default route - overview.
@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        conn = get_db_connection()

        time_now = datetime.utcnow().isoformat(' ', 'milliseconds')
        time_seconds = int(request.form['time_seconds'])

        # Update the countdown_state table.
        time_now = datetime.utcnow().isoformat(' ', 'milliseconds')
        conn.execute('UPDATE countdown_state SET last_change = ?, time_seconds = ? WHERE id = 1', (time_now, time_seconds))

        # Save a press for each live room (only if it hasn't had time expired)
        # so their counters are reset to the new time_seconds.
        rooms = get_rooms()
        for room in rooms:
            if not room['time_expired']:
                conn.execute("INSERT INTO presses (created, room_id) VALUES (?,?)", (time_now, room['room_id']))

        conn.commit()
        conn.close()

    countdown_state = get_countdown_state()

    # Render the page.
    return render_template('index.html', countdown_state=countdown_state, page='index')


# Test mode page.
@app.route('/test')
def test():
    conn = get_db_connection()
    presses = conn.execute('SELECT * FROM presses ORDER BY created DESC LIMIT 25').fetchall()
    conn.close()
    return render_template('test.html', presses=presses, page='test')


# Live current state data.
@app.route('/live/countdown-state')
@cross_origin()
def live_countdown_state():
    countdown_state = get_countdown_state()
    return jsonify(countdown_state)


# Room timer status displayed on a web page.
@app.route('/room-timers', methods = ['GET', 'POST'])
def room_timers():
    rooms = get_rooms()

    if request.method == 'POST':
        if request.form.get('reset_all_timers'):
            # Reset all rooms in the rooms table if they are 'live'.
            for room in rooms:
                if room['live']:
                    # Reset the room's status in the rooms table.
                    conn = get_db_connection()
                    conn.execute("UPDATE rooms SET color = ?, time_expired = ? WHERE room_id = ?", ('off', 0, room['room_id']))
                    conn.commit()
                    conn.close()

                    # Save a vote with the current time for this room.
                    save_press(room['room_id'])

    countdown_state = get_countdown_state()

    # Build list of rooms and press data.
    rooms_with_press_data = []
    for room in rooms:
        if room['live']:
            # Add a count of total presses submitted this round.
            room['presses'] = room_press_count(room['room_id'])

            # Add the most recent press.
            latest_press = room_press_latest(room['room_id'])
            room['most_recent_press'] = latest_press

            # Format the remaining time as MM:SS
            remaining_time = remaining_time_for_room(room['room_id'], latest_press['created'])
            if remaining_time > 0:
                room['time_remaining_seconds'] = remaining_time
                room['time_remaining'] = format_seconds_to_mmss(remaining_time)

        if 'time_remaining' not in room.keys():
            room['time_remaining'] = '0:00'

        # Add the data to our list of rooms.
        rooms_with_press_data.append(room)

    return render_template('room_timers.html', rooms=rooms_with_press_data, countdown_state=countdown_state, page='room-timers')


# Room timer API endpoint.
@app.route('/live/room-timers', methods = ['GET'])
@cross_origin()
def live_room_timers():
    response = make_response()

    room_timer_data = []
    status_code = 200
    rooms = get_rooms()
    for room in rooms:
        room_data = {'room_id': room['room_id']}
        room_data['press_count'] = room_press_count(room['room_id'])
        if room['live']:
            latest_press = room_press_latest(room['room_id'])
            remaining_time = remaining_time_for_room(room['room_id'], latest_press['created'])
            if remaining_time > 0:
                room_data['time_remaining_seconds'] = remaining_time
                room_data['time_remaining'] = format_seconds_to_mmss(remaining_time)
            else:
                room_data['time_remaining_seconds'] = 0
                room_data['time_remaining'] = '0:00'
        else:
            room_data['time_remaining_seconds'] = 0
            room_data['time_remaining'] = '0:00'
        room_timer_data.append(room_data)

    return room_timer_data, status_code


# Room timer status displayed on a web page.
@app.route('/room-presses/<int:room_id>', methods = ['GET', 'POST'])
def room_presses(room_id):
    if request.method == 'POST':
        if request.form.get('reset_timer'):
            # Reset the room's status in the rooms table.
            conn = get_db_connection()
            conn.execute("UPDATE rooms SET color = ?, time_expired = ?, live = ? WHERE room_id = ?", ('off', 0, 1, room_id))
            conn.commit()
            conn.close()

            # Save a vote with the current time for this room.
            save_press(room_id)

    countdown_state = get_countdown_state()

    # Get room press data.
    room = {'room_id': room_id}
    room['presses'] = get_room_presses(room_id)
    room['presses_total'] = room_press_count(room_id)
    room['latest_press'] = room_press_latest(room_id)

    return render_template('room_presses.html', room=room, countdown_state=countdown_state, page='room-presses')


# Room information API endpoint.
@app.route('/room', methods = ['GET'])
def room():
    response = make_response()
    room_id = request.args.get('room_id')
    status_code = 400

    if room_id:
        room_data = get_room((room_id,))
        status_code = 200

    return dict(room_data), status_code


# Room status displayed on a web page.
@app.route('/room-control', methods = ['GET', 'POST'])
def room_control():
    if request.method == 'POST':
        color = request.form.get('color_select')

        # Make sure the color is valid.
        if color not in valid_room_color_options():
            flash('Color "' + color + '" is not a valid color option.')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE rooms SET color = ?', (color,))
            conn.commit()
            conn.close()

    rooms = get_rooms()
    return render_template('room_control.html', rooms=rooms, page='room-control')


# Room edit page
@app.route('/edit-room/<int:room_id>', methods = ['GET', 'POST'])
def edit_room(room_id):
    if request.method == 'POST':
        color = request.form.get('color_select')
        # Ensure every binary option has something set, 0 or 1.
        binary_vars = ['live']
        binary_values = {}
        for var in binary_vars:
            if request.form.get(var):
                binary_values[var] = 1
            else:
                binary_values[var] = 0

        # Make sure the color is valid.
        if color not in valid_room_color_options():
            flash('Color "' + color + '" is not a valid color option.')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE rooms SET color = ?, live = ? WHERE room_id = ?', (color, binary_values['live'], room_id))
            conn.commit()
            conn.close()
            return redirect("/room-control", code=302)

    room = get_room((room_id,))
    return render_template('edit_room.html', room=room, page='edit-room')


# Vote route.
@app.route('/vote', methods = ['POST'])
def vote():
    # POST Method to add a vote
    if request.method == 'POST':
        response = make_response()
        data = request.get_json()
        room_id = data['room_id']

        # live_colors will never be enabled for countdown challenge.
        response_data = {'live_colors': 0}

        # Get the room's info.
        room = get_room((room_id,))

        # Save a vote if the room's time has not yet expired.
        if not room['time_expired']:
            save_press(room_id)
            response.data = json.dumps(response_data)
            response.status = 201  # Created
        else:
            response.status = 418  # I'm a Teapot
        return response


@app.template_filter('pluralize')
def pluralize(number, singular = '', plural = 's'):
    if number == 1:
        return singular
    else:
        return plural


@app.context_processor
def inject_debug():
    return dict(debug=app.debug)


@app.before_request
def before_request():
    if app.debug:
        g.start = time.time()


@app.after_request
def after_request(response):
    if app.debug:
        diff_string = format((time.time() - g.start) * 1000, '.3f')
        if ((response.response) and
            (200 <= response.status_code < 300) and
            (response.content_type.startswith('text/html'))):
            replacement_text = 'Page rendered in ' + diff_string + ' ms'
            response.set_data(response.get_data().replace(
                b'__EXECUTION_TIME__', replacement_text.encode()))
    return response
