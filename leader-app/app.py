import sqlite3
from flask import Flask, json, jsonify, render_template

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# TODO REWRITE THIS FOR RETRIEVING DATA FROM SQLite.
votes = [{'Item': 'Rice', 'Price': 10},{'Item': 'Chicken','Price': 20},{'Item':'Fish', 'Price': 20}]
rounds = []

# Default route.
@app.route('/')
def index():
    conn = get_db_connection()
    votes = conn.execute('SELECT * FROM votes').fetchall()
    conn.close()
    return render_template('index.html', votes=votes)

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

    # POST Method to add a round
    elif request.method == 'POST':
        response = {}
        payload = request.get_json()
        id1 = int(payload['id'])
        if id1 == len(votes):
            response = jsonify({'Status': 'Not in rounds'})
            response.status_code = 404
        elif votes[id1] in rounds:
            for i in rounds:
                if i['Item'] == votes[id1]['Item']:
                    i['Quantity'] += 1
            response = jsonify({'Status': 'Updated quantity', 'Item': votes[id1]})
            response.status_code = 200
        return response
