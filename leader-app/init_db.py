import sqlite3
import time

connection = sqlite3.connect('database.sqlite')

# Load schema into database.
with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Populate the stations table with some values.
cur.execute("INSERT INTO stations (station_id, mac_address) VALUES (?,?)", (1,"b8:27:eb:cd:09:30",))
cur.execute("INSERT INTO stations (station_id, mac_address) VALUES (?,?)", (2,"b8:27:eb:cd:09:31",))
cur.execute("INSERT INTO stations (station_id, mac_address) VALUES (?,?)", (3,"b8:27:eb:cd:09:32",))
cur.execute("INSERT INTO stations (station_id, mac_address) VALUES (?,?)", (4,"b8:27:eb:cd:09:33",))
cur.execute("INSERT INTO stations (station_id, mac_address) VALUES (?,?)", (5,"b8:27:eb:cd:09:34",))
cur.execute("INSERT INTO stations (station_id, mac_address) VALUES (?,?)", (6,"b8:27:eb:cd:09:35",))
cur.execute("INSERT INTO stations (station_id, mac_address) VALUES (?,?)", (7,"b8:27:eb:cd:09:36",))
cur.execute("INSERT INTO stations (station_id, mac_address) VALUES (?,?)", (8,"b8:27:eb:cd:09:37",))
cur.execute("INSERT INTO stations (station_id, mac_address) VALUES (?,?)", (9,"b8:27:eb:cd:09:38",))
cur.execute("INSERT INTO stations (station_id, mac_address) VALUES (?,?)", (10,"b8:27:eb:cd:09:39",))

# Populate the rounds table with some values.
time_now = time.strftime("%Y-%m-%d %H:%M:%f", time.gmtime())
cur.execute("INSERT INTO rounds (round_id, start_time, close_time, is_open, is_current, value_0, value_1) VALUES (?,?,?,?,?,?,?)", (1,"2023-03-01 23:36:37.171","2023-03-01 23:38:23.249",0,0,"No","Yes"))
cur.execute("INSERT INTO rounds (round_id, start_time, is_open, is_current, value_0, value_1) VALUES (?,?,?,?,?,?)", (2,time_now,1,1,"Chicken","Egg"))

# Populate the votes table with some values.
cur.execute("INSERT INTO votes (station_id, value, round_id) VALUES (?,?,?)", (1,1,1,))
time.sleep(0.001)
cur.execute("INSERT INTO votes (station_id, value, round_id) VALUES (?,?,?)", (2,1,1,))
cur.execute("INSERT INTO votes (station_id, value, round_id) VALUES (?,?,?)", (3,0,1,))
time.sleep(0.001)
cur.execute("INSERT INTO votes (station_id, value, round_id) VALUES (?,?,?)", (4,0,1,))
cur.execute("INSERT INTO votes (station_id, value, round_id) VALUES (?,?,?)", (5,1,1,))
cur.execute("INSERT INTO votes (station_id, value, round_id) VALUES (?,?,?)", (6,0,1,))
cur.execute("INSERT INTO votes (station_id, value, round_id) VALUES (?,?,?)", (7,1,1,))
cur.execute("INSERT INTO votes (station_id, value, round_id) VALUES (?,?,?)", (8,1,1,))
cur.execute("INSERT INTO votes (station_id, value, round_id) VALUES (?,?,?)", (9,0,1,))
time.sleep(0.001)
cur.execute("INSERT INTO votes (station_id, value, round_id) VALUES (?,?,?)", (10,1,1,))
time.sleep(0.001)
cur.execute("INSERT INTO votes (station_id, value, round_id) VALUES (?,?,?)", (1,0,2,))
time.sleep(0.001)
cur.execute("INSERT INTO votes (station_id, value, round_id) VALUES (?,?,?)", (2,1,2,))
time.sleep(0.005)
cur.execute("INSERT INTO votes (station_id, value, round_id) VALUES (?,?,?)", (2,0,2,))

connection.commit()
connection.close()
