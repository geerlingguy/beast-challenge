import sqlite3
import time
import os

database_path = os.environ.get('FLASK_DATABASE_PATH') or 'leader.sqlite'
connection = sqlite3.connect(database_path)

# Load schema into database.
with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Populate the rooms table with some values.
# LAST UPDATED: 2023-08-04 at 2:00 p.m. US Central
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (1,"b8:27:eb:cd:09:30","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (2,"b8:27:eb:cd:09:31","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (3,"b8:27:eb:cd:09:32","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (4,"b8:27:eb:cd:09:33","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (5,"b8:27:eb:cd:09:34","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (6,"b8:27:eb:cd:09:35","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (7,"b8:27:eb:cd:09:36","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (8,"b8:27:eb:cd:09:37","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (9,"b8:27:eb:cd:09:38","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (10,"b8:27:eb:cd:09:39","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (11,"b8:27:eb:cd:09:30","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (12,"b8:27:eb:cd:09:31","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (13,"b8:27:eb:cd:09:32","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (14,"b8:27:eb:cd:09:33","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (15,"b8:27:eb:cd:09:34","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (16,"b8:27:eb:cd:09:35","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (17,"b8:27:eb:cd:09:36","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (18,"b8:27:eb:cd:09:37","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (19,"b8:27:eb:cd:09:38","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (20,"b8:27:eb:cd:09:39","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (21,"b8:27:eb:cd:09:30","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (22,"b8:27:eb:cd:09:31","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (23,"b8:27:eb:cd:09:32","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (24,"b8:27:eb:cd:09:33","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (25,"b8:27:eb:cd:09:34","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (26,"b8:27:eb:cd:09:35","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (27,"b8:27:eb:cd:09:36","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (28,"b8:27:eb:cd:09:37","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (29,"b8:27:eb:cd:09:38","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (30,"b8:27:eb:cd:09:39","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (31,"b8:27:eb:cd:09:30","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (32,"b8:27:eb:cd:09:31","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (33,"b8:27:eb:cd:09:32","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (34,"b8:27:eb:cd:09:33","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (35,"b8:27:eb:cd:09:34","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (36,"b8:27:eb:cd:09:35","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (37,"b8:27:eb:cd:09:36","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (38,"b8:27:eb:cd:09:37","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (39,"b8:27:eb:cd:09:38","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (40,"b8:27:eb:cd:09:39","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (41,"b8:27:eb:cd:09:30","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (42,"b8:27:eb:cd:09:31","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (43,"b8:27:eb:cd:09:32","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (44,"b8:27:eb:cd:09:33","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (45,"b8:27:eb:cd:09:34","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (46,"b8:27:eb:cd:09:35","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (47,"b8:27:eb:cd:09:36","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (48,"b8:27:eb:cd:09:37","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (49,"b8:27:eb:cd:09:38","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (50,"b8:27:eb:cd:09:39","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (51,"b8:27:eb:cd:09:30","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (52,"b8:27:eb:cd:09:31","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (53,"b8:27:eb:cd:09:32","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (54,"b8:27:eb:cd:09:33","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (55,"b8:27:eb:cd:09:34","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (56,"b8:27:eb:cd:09:35","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (57,"b8:27:eb:cd:09:36","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (58,"b8:27:eb:cd:09:37","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (59,"b8:27:eb:cd:09:38","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (60,"b8:27:eb:cd:09:39","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (61,"b8:27:eb:cd:09:30","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (62,"b8:27:eb:cd:09:31","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (63,"b8:27:eb:cd:09:32","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (64,"b8:27:eb:cd:09:33","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (65,"b8:27:eb:cd:09:34","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (66,"b8:27:eb:cd:09:35","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (67,"b8:27:eb:cd:09:36","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (68,"b8:27:eb:cd:09:37","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (69,"b8:27:eb:cd:09:38","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (70,"b8:27:eb:cd:09:39","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (71,"b8:27:eb:cd:09:30","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (72,"b8:27:eb:cd:09:31","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (73,"b8:27:eb:cd:09:32","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (74,"b8:27:eb:cd:09:33","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (75,"b8:27:eb:cd:09:34","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (76,"b8:27:eb:cd:09:35","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (77,"b8:27:eb:cd:09:36","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (78,"b8:27:eb:cd:09:37","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (79,"b8:27:eb:cd:09:38","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (80,"b8:27:eb:cd:09:39","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (81,"b8:27:eb:cd:09:30","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (82,"b8:27:eb:cd:09:31","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (83,"b8:27:eb:cd:09:32","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (84,"b8:27:eb:cd:09:33","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (85,"b8:27:eb:cd:09:34","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (86,"b8:27:eb:cd:09:35","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (87,"b8:27:eb:cd:09:36","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (88,"b8:27:eb:cd:09:37","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (89,"b8:27:eb:cd:09:38","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (90,"b8:27:eb:cd:09:39","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (91,"b8:27:eb:cd:09:30","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (92,"b8:27:eb:cd:09:31","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (93,"b8:27:eb:cd:09:32","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (94,"b8:27:eb:cd:09:33","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (95,"b8:27:eb:cd:09:34","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (96,"b8:27:eb:cd:09:35","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (97,"b8:27:eb:cd:09:36","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (98,"b8:27:eb:cd:09:37","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (99,"b8:27:eb:cd:09:38","off",1))
cur.execute("INSERT INTO rooms (room_id, mac_address, color, live) VALUES (?,?,?,?)", (100,"b8:27:eb:cd:09:39","off",1))

# Populate the rounds table with some values.
time_now = time.strftime("%Y-%m-%d %H:%M:%f", time.gmtime())
cur.execute("INSERT INTO rounds (round_id, start_time, close_time, is_accepting_votes, live, is_allowing_multiple_votes, value_0, value_1, value_2, total_participants) VALUES (?,?,?,?,?,?,?,?,?,?)", (1,"2023-03-01 23:36:37.171","2023-03-01 23:38:23.249",1,0,0,"TEST","MODE","ONLY",100))
cur.execute("INSERT INTO rounds (round_id, start_time, is_accepting_votes, live, is_allowing_multiple_votes, value_0, value_1, value_2, total_participants) VALUES (?,?,?,?,?,?,?,?,?)", (2,time_now,1,1,1,"Chicken","Steak","Oatmeal",100))

# Populate the votes table with some values.
cur.execute("INSERT INTO votes (room_id, value, round_id) VALUES (?,?,?)", (10,1,1))
cur.execute("INSERT INTO votes (room_id, value, round_id) VALUES (?,?,?)", (19,1,1))
cur.execute("INSERT INTO votes (room_id, value, round_id) VALUES (?,?,?)", (30,0,1))
# time.sleep(0.001)
# cur.execute("INSERT INTO votes (room_id, value, round_id) VALUES (?,?,?)", (4,0,1))
# cur.execute("INSERT INTO votes (room_id, value, round_id) VALUES (?,?,?)", (5,1,1))
# cur.execute("INSERT INTO votes (room_id, value, round_id) VALUES (?,?,?)", (6,0,1))
# cur.execute("INSERT INTO votes (room_id, value, round_id) VALUES (?,?,?)", (7,1,1))
# cur.execute("INSERT INTO votes (room_id, value, round_id) VALUES (?,?,?)", (8,1,1))
# cur.execute("INSERT INTO votes (room_id, value, round_id) VALUES (?,?,?)", (9,0,1))
# time.sleep(0.001)
# cur.execute("INSERT INTO votes (room_id, value, round_id) VALUES (?,?,?)", (10,1,1))
# time.sleep(0.001)
# cur.execute("INSERT INTO votes (room_id, value, round_id) VALUES (?,?,?)", (1,0,3))
# time.sleep(0.001)
# cur.execute("INSERT INTO votes (room_id, value, round_id) VALUES (?,?,?)", (2,1,3))
# time.sleep(0.005)
# cur.execute("INSERT INTO votes (room_id, value, round_id) VALUES (?,?,?)", (2,0,3))
# cur.execute("INSERT INTO votes (room_id, value, round_id) VALUES (?,?,?)", (10,1,3))
# cur.execute("INSERT INTO votes (room_id, value, round_id) VALUES (?,?,?)", (49,2,3))
# cur.execute("INSERT INTO votes (room_id, value, round_id) VALUES (?,?,?)", (17,0,3))
# cur.execute("INSERT INTO votes (room_id, value, round_id) VALUES (?,?,?)", (78,2,3))

connection.commit()
connection.close()
