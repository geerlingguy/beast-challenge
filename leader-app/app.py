import sqlite3
from flask import Flask, json, jsonify, render_template

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.sqlite')
    conn.row_factory = sqlite3.Row
    return conn

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
    votes = conn.execute('SELECT * FROM votes').fetchall()
    conn.close()
    return render_template('index.html', votes=votes)

# Test mode page.
@app.route('/test')
def test():
    conn = get_db_connection()
    votes = conn.execute('SELECT * FROM votes ORDER BY created DESC LIMIT 10').fetchall()
    conn.close()
    return render_template('test.html', votes=votes)

# Tally of all votes displayed on a web page.
@app.route('/tally')
def tally():
    conn = get_db_connection()
    current_round = conn.execute('SELECT round_id FROM rounds WHERE is_current = 1').fetchone()
    votes = get_totals_for_round(current_round['round_id'])
    return render_template('tally.html', votes=votes)

# Vote route.
@app.route('/votes',methods = ['GET', 'PUT'])
def votes():
    if request.method == 'GET':
        response = jsonify({'Votes': votes})
        response.status_code = 200
        return response

    # PUT Method to add a vote
    elif request.method == 'PUT':
        response = {}
        payload = request.get_json()
        item = payload["item1"]
        f = False
        for i in votes:
            if i == item:
                f = True
        if not f:
            votes.append(item)
            response = jsonify({'Status': 'Added', 'Item': item})
            response.status_code =201
        else:
            response = jsonify({'Status': 'Already There', 'Item': item})
            response.status_code =400
        return response

@app.route('/rounds', methods = ['GET', 'POST'])
def rounds():
    # GET Method for obtaining the list of rounds
    if request.method == 'GET':
        response = ' '
        if len(rounds) == 0:
            response = jsonify({'Rounds': 'No rounds yet.'} )
            response.status_code = 404
        else :
            response = jsonify({'Rounds': rounds})
            response.status_code = 200
        return response
