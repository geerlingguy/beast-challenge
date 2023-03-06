import sqlite3
import time
import random
from flask import Flask, json, jsonify, request, flash, make_response, render_template, g

app = Flask(__name__)
app.config['SECRET_KEY'] = 'TvierCO6smUk7ZlNDm0ojBU7VeyPyGUn'


def get_db_connection():
    conn = sqlite3.connect('database.sqlite')
    conn.row_factory = sqlite3.Row
    return conn


def get_current_round():
    conn = get_db_connection()
    current_round = conn.execute('SELECT * FROM rounds WHERE is_current = 1 ORDER BY start_time DESC').fetchone()
    conn.close()
    return current_round


def get_rooms():
    conn = get_db_connection()
    rooms = conn.execute('SELECT * FROM rooms').fetchall()
    conn.close()
    return rooms


def get_rounds():
    conn = get_db_connection()
    rounds = conn.execute('SELECT * FROM rounds').fetchall()
    conn.close()
    return rounds


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
    current_round = conn.execute('SELECT * FROM rounds WHERE round_id = ?', (round_id,)).fetchone()

    # Build list of up to three vote options.
    vote_tallies = []
    for i in range(3):
        if current_round['value_' + str(i)]:
            vote_tallies.append({'label': current_round['value_' + str(i)],'total': 0})

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

    # Close DB connection and return vote tally.
    conn.close()
    return vote_tallies


# Default route - overview.
@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Build dict of submitted round data.
        round_data = {}
        for key, value in request.form.items():
            round_id = key[0]
            actual_key = key[2:]
            if round_id in round_data:
                round_data[round_id][actual_key] = value
            else:
                round_data[round_id] = {'round_id': round_id}

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
            if 'is_current' not in value_keys:
                value['is_current'] = 0
            else:
                value['is_current'] = 1
            if 'is_allowing_multiple_votes' not in value_keys:
                value['is_allowing_multiple_votes'] = 0
            else:
                value['is_allowing_multiple_votes'] = 1

            # Rearrange things for database insertion or update.
            row_round_id = value.pop('round_id')
            db_keys = '=?, '.join(value.keys()) + '=?'
            value['round_id'] = row_round_id
            db_values = tuple(value.values())

            # Create new round.
            if value['round_id'] == 'new':
                print('TODO new round about to be created')
            else:
                print('Updating existing round')
                conn = get_db_connection()
                conn.execute("UPDATE rounds SET " + db_keys + " WHERE round_id=?", db_values)
                conn.commit()
                conn.close()

    rounds = get_rounds()
    return render_template('index.html', rounds=rounds, page='index')


# Test mode page.
@app.route('/test')
def test():
    conn = get_db_connection()
    votes = conn.execute('SELECT * FROM votes ORDER BY created DESC LIMIT 10').fetchall()
    conn.close()
    return render_template('test.html', votes=votes, page='test')


# Tally of all votes displayed on a web page.
@app.route('/tally')
def tally():
    current_round = get_current_round()
    votes = get_totals_for_round(current_round['round_id'])
    return render_template('tally.html', votes=votes, page='tally')


# Room vote status displayed on a web page.
@app.route('/room-votes')
def room_votes():
    # TODO: Current round is hardcoded here. Might want to allow looking at
    # vote data for other rounds (for reference). Maybe a query string param?
    current_round = get_current_round()

    # Build list of rooms and vote data.
    rooms_with_vote_data = []
    rooms = get_rooms()
    for room in rooms:
        room_copy = dict(zip(room.keys(), room))

        # Add a count of total votes submitted this round.
        room_copy['votes_this_round'] = room_vote_count_for_round(room['room_id'], current_round['round_id'])

        # Add the most recent vote.
        latest_vote = room_vote_latest_for_round(room['room_id'], current_round['round_id'])
        vote_label = ''
        if latest_vote is not None:
            match latest_vote['value']:
                case 0:
                    vote_label = current_round['value_0']
                case 1:
                    vote_label = current_round['value_1']
                case 2:
                    vote_label = current_round['value_2']
        room_copy['most_recent_vote'] = vote_label

        # Add the data to our list of rooms.
        rooms_with_vote_data.append(room_copy)
    return render_template('room_votes.html', rooms=rooms_with_vote_data, round=current_round, page='room-votes')


# Room light status displayed on a web page.
@app.route('/room-lights', methods = ['GET', 'POST'])
def room_lights():
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
    return render_template('room_lights.html', rooms=rooms, page='room-lights')


# Vote route.
@app.route('/vote', methods = ['POST'])
def vote():
    # POST Method to add a vote
    if request.method == 'POST':
        response = make_response()
        payload = request.get_json()
        room_id = payload['room_id']
        value = payload['value']

        # Get current round information.
        current_round = get_current_round()

        # TODO Don't store votes for a button that doesn't have a corresponding
        # option (e.g. if vote value is `2` and round only has value_0/value_1).
        # (This is not critical... mostly saves us storing the non-useful data.)

        # If we're accepting votes, save vote and return success.
        if current_round['is_accepting_votes']:
            # If the current round allows multiple votes, save the vote.
            if current_round['is_allowing_multiple_votes']:
                save_vote(room_id, value, current_round['round_id'])
                response.status = 201  # Created
            else:
                # A vote was already submitted for this room; deny the vote.
                if room_submitted_vote_for_round(room_id, current_round['round_id']):
                    response.status = 423  # Locked
                # No vote submitted yet; save the vote.
                else:
                    save_vote(room_id, value, current_round['round_id'])
                    response.status = 201  # Created
        # Not accepting votes right now; deny the vote.
        else:
            response.status = 418  # I'm a Teapot
        return response


@app.route('/round', methods = ['POST'])
def round():
    if request.method == 'POST':
        response = make_response(jsonify({'Rounds': 'This route has not yet been implemented.'}), 501)
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
