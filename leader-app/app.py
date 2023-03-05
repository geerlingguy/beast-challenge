import sqlite3
import time
from flask import Flask, json, jsonify, request, make_response, render_template, g

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('database.sqlite')
    conn.row_factory = sqlite3.Row
    return conn


def get_current_round():
    conn = get_db_connection()
    current_round = conn.execute('SELECT * FROM rounds WHERE is_current = 1').fetchone()
    conn.close()
    return current_round


def get_totals_for_round(round_id):
    votes = []
    conn = get_db_connection()
    # Get current round metadata (including start and end time)
    current_round = conn.execute('SELECT * FROM rounds WHERE round_id = ?', (round_id,)).fetchone()
    # If no end time, set end time as 'now'

    # Get all votes that have CREATED between start end end time
    # TODO: Need to select the MOST RECENT vote for each room in current round
    votes = conn.execute('SELECT * FROM votes WHERE round_id = ? ORDER BY created DESC', (2,)).fetchall()
    # TODO: Return the label and tally for each option (0, 1, 2).
    # TODO: only return an element for each result that has a corresponding
    # 'value' in the round (e.g. if only value_0, don't return 1 or 2).
    votes = [
        {'label': current_round['value_0'], 'value': 13},
        {'label': current_round['value_1'], 'value': 42}
    ]

    # Close DB connection and return vote tally.
    conn.close()
    return votes


# Default route - overview.
@app.route('/')
def index():
    conn = get_db_connection()
    rounds = conn.execute('SELECT * FROM rounds').fetchall()
    conn.close()
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

        # If we're accepting votes, save vote and return success.
        if current_round['is_accepting_votes']:
            conn = get_db_connection()
            conn.execute('INSERT INTO votes (room_id, value, round_id) VALUES (?,?,?)', (room_id, value, current_round['round_id']))
            conn.commit()
            conn.close()
            # TODO: Save vote in database.
            response.status = 201
        # Otherwise, I'm sorry, but I'm a Teapot and you can't send me a vote.
        else:
            response.status = 418
        return response


@app.route('/round', methods = ['POST'])
def round():
    if request.method == 'POST':
        response = make_response(jsonify({'Rounds': 'This route has not yet been implemented.'}), 501)
        return response


@app.before_request
def before_request():
    if app.debug:
        g.start = time.time()


@app.after_request
def after_request(response):
    if app.debug:
        diff = (time.time() - g.start) * 1000
        print(diff)
        diff_string = format(diff, '.3f')
        if ((response.response) and
            (200 <= response.status_code < 300) and
            (response.content_type.startswith('text/html'))):
            replacement_text = 'Page rendered in ' + diff_string + ' ms'
            response.set_data(response.get_data().replace(
                b'__EXECUTION_TIME__', replacement_text.encode()))
    return response
