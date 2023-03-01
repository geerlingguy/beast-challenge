import sqlite3

connection = sqlite3.connect('database.db')

# Load schema into database.
with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Populate the database with some values.
cur.execute("INSERT INTO votes (station, button) VALUES (?,?)", (1,1,))
cur.execute("INSERT INTO votes (station, button) VALUES (?,?)", (2,1,))
cur.execute("INSERT INTO votes (station, button) VALUES (?,?)", (3,0,))
cur.execute("INSERT INTO rounds (name) VALUES (?)", ('round_1',))

connection.commit()
connection.close()
