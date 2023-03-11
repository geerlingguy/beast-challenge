import sqlite3
import time
import random
from datetime import datetime
from flask import Flask, json, jsonify, request, flash, redirect, make_response, render_template, g

app = Flask(__name__)
app.config['SECRET_KEY'] = 'TvierCO6smUk7ZlNDm0ojBU7VeyPyGUn'


def sqlite_select_as_dict(select_query, type = 'all'):
    try:
        conn = sqlite3.connect('database.sqlite')
        conn.row_factory = sqlite3.Row
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
    conn = sqlite3.connect('database.sqlite')
    conn.row_factory = sqlite3.Row
    return conn


def get_live_round():
    query = "SELECT * FROM rounds WHERE is_live = 1 ORDER BY start_time DESC"
    return sqlite_select_as_dict(query, 'one')


def get_rooms():
    query = 'SELECT * FROM rooms'
    return sqlite_select_as_dict(query, 'all')


def get_room(room_id):
    conn = get_db_connection()
    room = conn.execute('SELECT * FROM rooms WHERE room_id = ?', room_id).fetchone()
    conn.close()
    return room


def get_round(round_id):
    conn = get_db_connection()
    round_data = conn.execute('SELECT * FROM rounds WHERE round_id = ?', round_id).fetchone()
    conn.close()
    return round_data


def get_rounds():
    return sqlite_select_as_dict('SELECT * FROM rounds')


def valid_room_color_options():
    return ['off', 'white', 'red', 'green', 'blue']


def room_submitted_press_for_round(room_id, round_id):
    conn = get_db_connection()
    press = conn.execute('SELECT * FROM presses WHERE room_id = ? AND round_id = ?', (room_id, round_id)).fetchone()
    conn.close()
    return press


def room_press_count_for_round(room_id, round_id):
    conn = get_db_connection()
    count = conn.execute('SELECT COUNT(*) FROM presses WHERE room_id = ? AND round_id = ?', (room_id, round_id)).fetchone()
    conn.close()
    return count[0]


def room_press_latest_for_round(room_id, round_id):
    conn = get_db_connection()
    press = conn.execute('SELECT * FROM presses WHERE room_id = ? AND round_id = ? ORDER BY created DESC', (room_id, round_id)).fetchone()
    conn.close()
    return press


def remaining_time_for_room(room_id, press_time):
    current_time = getattr(g, '_current_time', None)
    if current_time is None:
        g._current_time = datetime.now().isoformat(' ', 'milliseconds')
        current_time = g._current_time
    print(room_id)
    print(current_time)

    # Get current round's time_seconds 'time per press'.
    current_round = get_live_round()
    time_per_press = current_round['time_seconds']

    # TODO - Get delta of seconds between current time and last button press.

    # TODO - Check if delta is greater than current round's time_seconds
    #   - If so, maybe make sure room is turned 'off' in the database automatically?
    #   - return 0

    # TODO - Else get the number of seconds left... TODO MY BRAIN HURTS RIGHT
    # NOW SO LET'S JUST GIVE IT A RANDOM NUMBER.
    return str(random.randint(1,4)) + ':' + str(random.randint(10,58))


def save_press(room_id, round_id):
    conn = get_db_connection()
    conn.execute('INSERT INTO presses (room_id, round_id) VALUES (?,?)', (room_id, round_id))
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
    # To future readers of this code: please realize it was written after 1 a.m.
    # over a long weekend which involved writing code between settling frequent
    # disputes between the young ones in my family. I am tired, this code is not
    # amazing, and that's all there is to it. If it works reliably, it ships!
    if request.method == 'POST':
        # Save data for all the rounds - build a dict.
        round_data = {}
        for key, value in request.form.items():
            round_id = key[0]
            actual_key = key[2:]
            if round_id not in round_data:
                round_data[round_id] = {'round_id': round_id}
            round_data[round_id][actual_key] = value

        conn = get_db_connection()

        # Write each round to the database.
        # NOTE: Security is not a priority. If someone hacked the form, they
        # could likely achieve SQL injection. Hello little Bobby Tables!
        for key, value in round_data.items():
            value_keys = value.keys()
            # Force all binary options to have a value, set to 0 or 1.
            if 'is_live' not in value_keys:
                value['is_live'] = 0
            else:
                value['is_live'] = 1

            # Check if round is opening up. If so, store a vote for each room.
            if value['is_live']:
                round_data = get_round(value['round_id'])
                if not round_data['is_live']:
                    print('TODO - This should result in writing a new vote with a global request time to each room that is not _off_')

            # Rearrange things for database insertion or update.
            row_round_id = value.pop('round_id')
            db_keys = '=?, '.join(value.keys()) + '=?'
            if (row_round_id != 'n'):
                value['round_id'] = row_round_id
            else:
                db_keys = ','.join(value.keys())
            db_values = tuple(value.values())

            # Create new round if not empty.
            if row_round_id == 'n':
                if value['time_seconds']:
                    conn = get_db_connection()
                    conn.execute("INSERT INTO rounds (" + db_keys + ') VALUES (?,?)', db_values)
                    conn.commit()
                    conn.close()
            # Update existing round.
            else:
                conn = get_db_connection()
                conn.execute("UPDATE rounds SET " + db_keys + " WHERE round_id=?", db_values)
                conn.commit()
                conn.close()

    rounds = get_rounds()
    print(rounds)

    # Create empty row for last round.
    last_row = dict(rounds[-1])
    for key, value in last_row.items():
        if key == 'round_id':
            last_row[key] = 'n'
        elif type(last_row[key]) is int:
            last_row[key] = 0
        elif type(last_row[key]) is str:
            last_row[key] = ''
    rounds.append(last_row)

    # Render the page.
    return render_template('index.html', rounds=rounds, page='index')


# Test mode page.
@app.route('/test')
def test():
    conn = get_db_connection()
    presses = conn.execute('SELECT * FROM presses ORDER BY created DESC LIMIT 25').fetchall()
    conn.close()
    return render_template('test.html', presses=presses, page='test')


# Live current round data for React.
@app.route('/live/round')
def live_round():
    live_round = get_live_round()
    # TODO - See https://github.com/geerlingguy/beast-game/issues/21
    live_round['total_participants'] = 100
    return jsonify(live_round)


# Room press status displayed on a web page.
@app.route('/room-timers')
def room_timers():
    # TODO: Current round is hardcoded here. Might want to allow looking at
    # press data for other rounds (for reference). Maybe a query string param?
    live_round = get_live_round()

    # Build list of rooms and press data.
    rooms_with_press_data = []
    rooms = get_rooms()
    for room in rooms:
        # Add a count of total presses submitted this round.
        room['presses_this_round'] = room_press_count_for_round(room['room_id'], live_round['round_id'])

        # Add the most recent press.
        latest_press = room_press_latest_for_round(room['room_id'], live_round['round_id'])
        room['most_recent_press'] = latest_press

        # TODO DELETE NEXT 4 LINES
        if not latest_press:
            lpc = '2023-03-11 00:56:38.829'
        else:
            lpc = latest_press['created']
        room['time_remaining'] = remaining_time_for_room(room['room_id'], lpc)

        # Add the data to our list of rooms.
        rooms_with_press_data.append(room)
    return render_template('room_timers.html', rooms=rooms_with_press_data, round=live_round, page='room-timers')


# Room information API endpoint.
@app.route('/room', methods = ['GET'])
def room():
    response = make_response()
    room_id = request.args.get('room_id')
    status_code = 400

    if room_id:
        room_data = get_room(room_id)
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


# Press route.
@app.route('/press', methods = ['POST'])
def press():
    # POST Method to add a press
    if request.method == 'POST':
        response = make_response()
        data = request.get_json()
        room_id = data['room_id']

        # Get current round information.
        live_round = get_live_round()

        save_press(room_id, live_round['round_id'])
        response.status = 201  # Created

        return response


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
