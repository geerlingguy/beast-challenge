import sqlite3
import time
import os
from datetime import datetime

database_path = os.environ.get('FLASK_DATABASE_PATH') or 'countdown.sqlite'
connection = sqlite3.connect(database_path)

# Load schema into database.
with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Populate the rooms table with some values.
# LAST UPDATED: 2023-03-24 at 8:00 p.m. US Central
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (1,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (2,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (3,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (4,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (5,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (6,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (7,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (8,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (9,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (10,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (11,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (12,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (13,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (14,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (15,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (16,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (17,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (18,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (19,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (20,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (21,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (22,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (23,0,1))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (24,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (25,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (26,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (27,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (28,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (29,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (30,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (31,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (32,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (33,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (34,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (35,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (36,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (37,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (38,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (39,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (40,0,1))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (41,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (42,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (43,0,1))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (44,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (45,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (46,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (47,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (48,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (49,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (50,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (51,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (52,0,1))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (53,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (54,0,1))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (55,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (56,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (57,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (58,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (59,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (60,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (61,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (62,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (63,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (64,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (65,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (66,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (67,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (68,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (69,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (70,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (71,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (72,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (73,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (74,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (75,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (76,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (77,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (78,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (79,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (80,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (81,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (82,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (83,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (84,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (85,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (86,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (87,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (88,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (89,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (90,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (91,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (92,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (93,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (94,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (95,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (96,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (97,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (98,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (99,1,0))
cur.execute("INSERT INTO rooms (room_id, time_expired, live) VALUES (?,?,?)", (100,1,0))

# Populate the state table with values.
time_now = datetime.utcnow().isoformat(' ', 'milliseconds')
cur.execute("INSERT INTO countdown_state (last_change, time_seconds) VALUES (?,?)", (time_now, 3540))

# Populate the presses table with some values.
for room_id in range(1, 101):
    cur.execute("INSERT INTO presses (created, room_id) VALUES (?,?)", (time_now, room_id))

connection.commit()
connection.close()
