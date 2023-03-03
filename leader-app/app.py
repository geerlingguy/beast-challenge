import sqlite3
from flask import Flask, json, jsonify, render_template

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.sqlite')
    conn.row_factory = sqlite3.Row
    return conn

def get_totals_for_round(round = ''):
    # TODO: Get round metadata (including start and end time)
    # If no end time, set end time as 'now'
    # Get all votes that have CREATED between start end end time
    # Tally up count of 1 and count of 0
    # Return those to tallies
    totals = [{'yes': 92, 'no': 10}]

# Default route.
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
    current_round = conn.execute('SELECT * FROM rounds WHERE is_current = 1').fetchone()
    # TODO: Need to select the MOST RECENT vote for each room in current round
    votes = conn.execute('SELECT * FROM votes WHERE round_id = ? ORDER BY created DESC', (2,)).fetchall()
    # TODO: Sum how many voted 0 and how many voted 1
    conn.close()
    # TODO: This is for demo only.
    votes = [
        {'label': current_round['value_0'], 'value': 13},
        {'label': current_round['value_1'], 'value': 42}
    ]
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
