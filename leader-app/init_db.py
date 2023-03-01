import sqlite3
import time

connection = sqlite3.connect('database.sqlite')

# Load schema into database.
with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Populate the rounds table with some values.
cur.execute("INSERT INTO rounds (name) VALUES (?)", ('round_1',))

# Populate the votes table with some values.
cur.execute("INSERT INTO votes (station, button) VALUES (?,?)", (1,1,))
time.sleep(0.001)
cur.execute("INSERT INTO votes (station, button) VALUES (?,?)", (2,1,))
cur.execute("INSERT INTO votes (station, button) VALUES (?,?)", (3,0,))
time.sleep(0.001)
cur.execute("INSERT INTO votes (station, button) VALUES (?,?)", (4,0,))
cur.execute("INSERT INTO votes (station, button) VALUES (?,?)", (5,1,))
cur.execute("INSERT INTO votes (station, button) VALUES (?,?)", (6,0,))
cur.execute("INSERT INTO votes (station, button) VALUES (?,?)", (7,1,))
cur.execute("INSERT INTO votes (station, button) VALUES (?,?)", (8,1,))
cur.execute("INSERT INTO votes (station, button) VALUES (?,?)", (9,0,))
time.sleep(0.001)
cur.execute("INSERT INTO votes (station, button) VALUES (?,?)", (10,1,))
time.sleep(0.001)
cur.execute("INSERT INTO votes (station, button) VALUES (?,?)", (1,0,))
time.sleep(0.001)
cur.execute("INSERT INTO votes (station, button) VALUES (?,?)", (2,1,))
time.sleep(0.005)
cur.execute("INSERT INTO votes (station, button) VALUES (?,?)", (2,0,))

# TODO: Populate the current_round table with the current round.
# TODO: Populate the stations table with MAC addresses and station IDs for all the Potatoes.

connection.commit()
connection.close()
