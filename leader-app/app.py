import sqlite3
import time
import random
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
    query = "SELECT * FROM rounds WHERE live = 1 ORDER BY start_time DESC"
    return sqlite_select_as_dict(query, 'one')


def get_rooms():
    query = 'SELECT * FROM rooms'
    return sqlite_select_as_dict(query, 'all')


def get_room(room_id):
    conn = get_db_connection()
    room = conn.execute('SELECT * FROM rooms WHERE room_id = ?', room_id).fetchone()
    conn.close()
    return room


def get_rounds():
    return sqlite_select_as_dict('SELECT * FROM rounds')


def valid_room_color_options():
    return ['off', 'white', 'red', 'green', 'blue']


def room_submitted_vote_for_round(room_id, round_id):
    conn = get_db_connection()
    vote = conn.execute('SELECT * FROM votes WHERE room_id = ? AND round_id = ?', (room_id, round_id)).fetchone()
    conn.close()
    return vote


def room_vote_count_for_round(room_id, round_id):
    conn = get_db_connection()
    count = conn.execute('SELECT COUNT(*) FROM votes WHERE room_id = ? AND round_id = ?', (room_id, round_id)).fetchone()
    conn.close()
    return count[0]


def room_votes_for_round(room_id, round_id):
    conn = get_db_connection()
    conn.row_factory = sqlite3.Row
    votes = conn.execute('SELECT * FROM votes WHERE room_id = ? AND round_id = ? ORDER BY created DESC', (room_id, round_id)).fetchall()
    unpacked = [{k: item[k] for k in item.keys()} for item in votes]
    conn.close()
    return unpacked


def room_vote_latest_for_round(room_id, round_id):
    conn = get_db_connection()
    vote = conn.execute('SELECT * FROM votes WHERE room_id = ? AND round_id = ? ORDER BY created DESC', (room_id, round_id)).fetchone()
    conn.close()
    return vote


def save_vote(room_id, value, round_id):
    conn = get_db_connection()
    conn.execute('INSERT INTO votes (room_id, value, round_id) VALUES (?,?,?)', (room_id, value, round_id))
    conn.commit()
    conn.close()


def get_totals_for_round(round_id):
    votes = []
    conn = get_db_connection()
    # Get current round metadata.
    live_round = conn.execute('SELECT * FROM rounds WHERE round_id = ?', (round_id,)).fetchone()

    # Build list of up to three vote options.
    vote_tallies = []
    for i in range(3):
        if live_round['value_' + str(i)]:
            vote_tallies.append({'label': live_round['value_' + str(i)],'total': 0})

    # Get all votes for the current round.
    # TODO: The rest of the tabulation logic here is probably like O(3) or
    # something insane. With 33,000 votes in a given round, this takes over
    # 200ms to render. So, not wonderful when there are tens of thousands of
    # votes in a given round. It would be nice to use a DISTINCT and do all the
    # logic via SQL but with SQLite I was having problems getting SELECT
    # DISTINCT working with an ORDER BY so I decited iterate through ALL the
    # votes in a round to tally them up.
    vote_data = conn.execute('SELECT * FROM votes WHERE round_id = ? ORDER BY created DESC', (round_id,)).fetchall()
    latest_votes = []

    # Filter this list only include the first vote for each room.
    for vote in vote_data:
        if not any(vote['room_id'] in d for d in latest_votes):
            latest_votes.append({vote['room_id']: vote['value']})

    # Total the count of each tally.
    for index, option in enumerate(vote_tallies):
        for vote in latest_votes:
            # If the current option matches the vote, add one to the tally.
            if index == next(iter(vote.values())):
                vote_tallies[index]['total'] += 1

    # Add a percentage value to the result.
    for tally in vote_tallies:
        percentage_exact = ((tally['total'] / live_round['total_participants']) * 100)
        tally['percentage'] = round(percentage_exact)

    # Close DB connection and return vote tally.
    conn.close()
    return vote_tallies


def update_color_for_room(color, room_id):
    conn = get_db_connection()
    conn.execute("UPDATE rooms SET color = ? WHERE room_id = ?", (color, room_id))
    conn.commit()
    conn.close()


def set_room_colors_according_to_last_vote(colors={}):
    live_round = get_live_round()
    rooms = get_rooms()
    # Loop through all the rooms.
    for room in rooms:
        # Get the latest vote for the room to set the color.
        latest_vote = room_vote_latest_for_round(room['room_id'], live_round['round_id'])
        if latest_vote:
            key = latest_vote['value']
            vote_color = colors[key]
            # Write the new color to the database.
            update_color_for_room(vote_color, room['room_id'])


# Default route - overview.
@app.route('/', methods = ['GET', 'POST'])
def index():
    # To future readers of this code: please realize it was written after 1 a.m.
    # over a long weekend which involved writing code between settling frequent
    # disputes between the young ones in my family. I am tired, this code is not
    # amazing, and that's all there is to it. If it works reliably, it ships!
    if request.method == 'POST':
        # Process the colors selected for options in the current round.
        if 'room_color_form' in request.form:
            colors = {}
            for key, value in request.form.items():
                # Discard the first result.
                if key == 'room_color_form':
                    continue
                # Grab the last character from the key.
                colors[int(key[-1])] = value
            set_room_colors_according_to_last_vote(colors)


        # Save data for all the rounds.
        else:
            # Build dict of submitted round data.
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
                if 'is_accepting_votes' not in value_keys:
                    value['is_accepting_votes'] = 0
                else:
                    value['is_accepting_votes'] = 1
                if 'live' not in value_keys:
                    value['live'] = 0
                else:
                    value['live'] = 1
                if 'is_allowing_multiple_votes' not in value_keys:
                    value['is_allowing_multiple_votes'] = 0
                else:
                    value['is_allowing_multiple_votes'] = 1

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
                    if value['value_0']:
                        conn = get_db_connection()
                        conn.execute("INSERT INTO rounds (" + db_keys + ') VALUES (?,?,?,?,?,?,?)', db_values)
                        conn.commit()
                        conn.close()
                # Update existing round.
                else:
                    conn = get_db_connection()
                    conn.execute("UPDATE rounds SET " + db_keys + " WHERE round_id=?", db_values)
                    conn.commit()
                    conn.close()

    rounds = get_rounds()

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

    # Also set up options for color selections.
    live_round = get_live_round()
    color_options = []
    for key, value in live_round.items():
        if key.startswith('value_') and value:
            color_options.append(value)

    # Render the page.
    return render_template('index.html', rounds=rounds, color_options=color_options, page='index')


# Test mode page.
@app.route('/test')
def test():
    conn = get_db_connection()
    votes = conn.execute('SELECT * FROM votes ORDER BY created DESC LIMIT 25').fetchall()
    conn.close()
    return render_template('test.html', votes=votes, page='test')


# Live vote data for React.
@app.route('/live/tally')
def live_tally():
    live_round = get_live_round()
    votes = get_totals_for_round(live_round['round_id'])
    return jsonify(votes)


# Live current round data for React.
@app.route('/live/round')
def live_round():
    live_round = get_live_round()
    return jsonify(live_round)


# Live current round data for React.
@app.route('/live/round/participants')
def live_round_participants():
    live_round = get_live_round()
    return jsonify({'total_participants': live_round['total_participants']})


# Tally of all votes displayed on a web page.
@app.route('/tally')
def tally():
    live_round = get_live_round()
    votes = get_totals_for_round(live_round['round_id'])
    return render_template('tally.html', votes=votes, page='tally')


# Room vote status displayed on a web page.
@app.route('/room-votes')
def room_votes():
    # TODO: Current round is hardcoded here. Might want to allow looking at
    # vote data for other rounds (for reference). Maybe a query string param?
    live_round = get_live_round()

    # Build list of rooms and vote data.
    rooms_with_vote_data = []
    rooms = get_rooms()
    for room in rooms:

        # Add a count of total votes submitted this round.
        room['votes_this_round'] = room_vote_count_for_round(room['room_id'], live_round['round_id'])

        # Add the most recent vote.
        latest_vote = room_vote_latest_for_round(room['room_id'], live_round['round_id'])
        vote_label = ''
        if latest_vote is not None:
            match latest_vote['value']:
                case 0:
                    vote_label = live_round['value_0']
                case 1:
                    vote_label = live_round['value_1']
                case 2:
                    vote_label = live_round['value_2']
        room['most_recent_vote'] = vote_label

        # Add the data to our list of rooms.
        rooms_with_vote_data.append(room)
    return render_template('room_votes.html', rooms=rooms_with_vote_data, round=live_round, page='room-votes')


# Room vote status and history for the current round displayed on a web page.
@app.route('/room-vote/<int:room_id>')
def room_vote(room_id):
    # TODO: Current round is hardcoded here. Might want to allow looking at
    # vote data for other rounds (for reference). Maybe a query string param?
    live_round = get_live_round()

    # Get current room data.
    room = get_room((room_id,))
    room_data = {}
    room_data['room_id'] = room_id

    # Get all votes for this room submitted this round.
    votes = room_votes_for_round((room_id), live_round['round_id'])

    total = 0
    for vote in votes:
        # Store the latest vote data separately.
        if total == 0:
            room_data['latest_vote'] = vote
        total += 1
        # Add label for each vote value.
        match vote['value']:
            case 0:
                vote['label'] = live_round['value_0']
            case 1:
                vote['label'] = live_round['value_1']
            case 2:
                vote['label'] = live_round['value_2']
    room_data['votes_this_round'] = total

    return render_template('room_vote.html', room=room_data, votes=votes, round=live_round, page='room-vote')


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
        binary_vars = ['live', 'led_0', 'led_1', 'led_2']
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
            conn.execute('UPDATE rooms SET color = ?, live = ?, led_0 = ?, led_1 = ?, led_2 = ? WHERE room_id = ?', (color, binary_values['live'], binary_values['led_0'], binary_values['led_1'], binary_values['led_2'], room_id))
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
        value = data['value']

        # Get current round information.
        live_round = get_live_round()

        # TODO Don't store votes for a button that doesn't have a corresponding
        # option (e.g. if vote value is `2` and round only has value_0/value_1).
        # (This is not critical... mostly saves us storing the non-useful data.)

        # If we're accepting votes, save vote and return success.
        if live_round['is_accepting_votes']:
            # If the current round allows multiple votes, save the vote.
            if live_round['is_allowing_multiple_votes']:
                save_vote(room_id, value, live_round['round_id'])
                response.status = 201  # Created
            else:
                # A vote was already submitted for this room; deny the vote.
                if room_submitted_vote_for_round(room_id, live_round['round_id']):
                    response.status = 423  # Locked
                # No vote submitted yet; save the vote.
                else:
                    save_vote(room_id, value, live_round['round_id'])
                    response.status = 201  # Created
        # Not accepting votes right now; deny the vote.
        else:
            response.status = 418  # I'm a Teapot
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
