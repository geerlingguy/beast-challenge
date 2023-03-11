import sqlite3
import time

connection = sqlite3.connect('database.sqlite')

# Load schema into database.
with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Populate the rooms table with some values.
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (1,"b8:27:eb:cd:09:30","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (2,"b8:27:eb:cd:09:31","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (3,"b8:27:eb:cd:09:32","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (4,"b8:27:eb:cd:09:33","red"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (5,"b8:27:eb:cd:09:34","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (6,"b8:27:eb:cd:09:35","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (7,"b8:27:eb:cd:09:36","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (8,"b8:27:eb:cd:09:37","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (9,"b8:27:eb:cd:09:38","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (10,"b8:27:eb:cd:09:39","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (11,"b8:27:eb:cd:09:30","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (12,"b8:27:eb:cd:09:31","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (13,"b8:27:eb:cd:09:32","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (14,"b8:27:eb:cd:09:33","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (15,"b8:27:eb:cd:09:34","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (16,"b8:27:eb:cd:09:35","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (17,"b8:27:eb:cd:09:36","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (18,"b8:27:eb:cd:09:37","red"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (19,"b8:27:eb:cd:09:38","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (20,"b8:27:eb:cd:09:39","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (21,"b8:27:eb:cd:09:30","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (22,"b8:27:eb:cd:09:31","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (23,"b8:27:eb:cd:09:32","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (24,"b8:27:eb:cd:09:33","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (25,"b8:27:eb:cd:09:34","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (26,"b8:27:eb:cd:09:35","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (27,"b8:27:eb:cd:09:36","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (28,"b8:27:eb:cd:09:37","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (29,"b8:27:eb:cd:09:38","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (30,"b8:27:eb:cd:09:39","red"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (31,"b8:27:eb:cd:09:30","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (32,"b8:27:eb:cd:09:31","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (33,"b8:27:eb:cd:09:32","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (34,"b8:27:eb:cd:09:33","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (35,"b8:27:eb:cd:09:34","red"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (36,"b8:27:eb:cd:09:35","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (37,"b8:27:eb:cd:09:36","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (38,"b8:27:eb:cd:09:37","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (39,"b8:27:eb:cd:09:38","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (40,"b8:27:eb:cd:09:39","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (41,"b8:27:eb:cd:09:30","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (42,"b8:27:eb:cd:09:31","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (43,"b8:27:eb:cd:09:32","off"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (44,"b8:27:eb:cd:09:33","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (45,"b8:27:eb:cd:09:34","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (46,"b8:27:eb:cd:09:35","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (47,"b8:27:eb:cd:09:36","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (48,"b8:27:eb:cd:09:37","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (49,"b8:27:eb:cd:09:38","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (50,"b8:27:eb:cd:09:39","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (51,"b8:27:eb:cd:09:30","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (52,"b8:27:eb:cd:09:31","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (53,"b8:27:eb:cd:09:32","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (54,"b8:27:eb:cd:09:33","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (55,"b8:27:eb:cd:09:34","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (56,"b8:27:eb:cd:09:35","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (57,"b8:27:eb:cd:09:36","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (58,"b8:27:eb:cd:09:37","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (59,"b8:27:eb:cd:09:38","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (60,"b8:27:eb:cd:09:39","red"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (61,"b8:27:eb:cd:09:30","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (62,"b8:27:eb:cd:09:31","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (63,"b8:27:eb:cd:09:32","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (64,"b8:27:eb:cd:09:33","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (65,"b8:27:eb:cd:09:34","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (66,"b8:27:eb:cd:09:35","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (67,"b8:27:eb:cd:09:36","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (68,"b8:27:eb:cd:09:37","off"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (69,"b8:27:eb:cd:09:38","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (70,"b8:27:eb:cd:09:39","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (71,"b8:27:eb:cd:09:30","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (72,"b8:27:eb:cd:09:31","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (73,"b8:27:eb:cd:09:32","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (74,"b8:27:eb:cd:09:33","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (75,"b8:27:eb:cd:09:34","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (76,"b8:27:eb:cd:09:35","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (77,"b8:27:eb:cd:09:36","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (78,"b8:27:eb:cd:09:37","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (79,"b8:27:eb:cd:09:38","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (80,"b8:27:eb:cd:09:39","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (81,"b8:27:eb:cd:09:30","off"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (82,"b8:27:eb:cd:09:31","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (83,"b8:27:eb:cd:09:32","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (84,"b8:27:eb:cd:09:33","off"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (85,"b8:27:eb:cd:09:34","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (86,"b8:27:eb:cd:09:35","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (87,"b8:27:eb:cd:09:36","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (88,"b8:27:eb:cd:09:37","red"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (89,"b8:27:eb:cd:09:38","red"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (90,"b8:27:eb:cd:09:39","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (91,"b8:27:eb:cd:09:30","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (92,"b8:27:eb:cd:09:31","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (93,"b8:27:eb:cd:09:32","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (94,"b8:27:eb:cd:09:33","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (95,"b8:27:eb:cd:09:34","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (96,"b8:27:eb:cd:09:35","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (97,"b8:27:eb:cd:09:36","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (98,"b8:27:eb:cd:09:37","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (99,"b8:27:eb:cd:09:38","white"))
cur.execute("INSERT INTO rooms (room_id, mac_address, color) VALUES (?,?,?)", (100,"b8:27:eb:cd:09:39","white"))

# Populate the rounds table with some values.
time_now = time.strftime("%Y-%m-%d %H:%M:%f", time.gmtime())
cur.execute("INSERT INTO rounds (round_id, start_time, close_time, is_live, time_seconds) VALUES (?,?,?,?,?)", (1,"2023-03-01 23:36:37.171","2023-03-01 23:38:23.249",0,300))
cur.execute("INSERT INTO rounds (round_id, start_time, close_time, is_live, time_seconds) VALUES (?,?,?,?,?)", (2,"2023-03-01 23:39:23.249","2023-03-01 23:42:23.249",1,240))

# Populate the presses table with some values.
cur.execute("INSERT INTO presses (room_id, round_id) VALUES (?,?)", (1,1))
time.sleep(0.001)
cur.execute("INSERT INTO presses (room_id, round_id) VALUES (?,?)", (2,1))
cur.execute("INSERT INTO presses (room_id, round_id) VALUES (?,?)", (3,1))
time.sleep(0.001)
cur.execute("INSERT INTO presses (room_id, round_id) VALUES (?,?)", (4,1))
cur.execute("INSERT INTO presses (room_id, round_id) VALUES (?,?)", (5,1))
cur.execute("INSERT INTO presses (room_id, round_id) VALUES (?,?)", (6,1))
cur.execute("INSERT INTO presses (room_id, round_id) VALUES (?,?)", (7,1))
cur.execute("INSERT INTO presses (room_id, round_id) VALUES (?,?)", (8,1))
cur.execute("INSERT INTO presses (room_id, round_id) VALUES (?,?)", (9,1))
time.sleep(0.001)
cur.execute("INSERT INTO presses (room_id, round_id) VALUES (?,?)", (9,2))
time.sleep(0.001)
cur.execute("INSERT INTO presses (room_id, round_id) VALUES (?,?)", (10,2))
time.sleep(0.001)
cur.execute("INSERT INTO presses (room_id, round_id) VALUES (?,?)", (1,2))
time.sleep(0.001)
cur.execute("INSERT INTO presses (room_id, round_id) VALUES (?,?)", (2,2))
time.sleep(0.005)
cur.execute("INSERT INTO presses (room_id, round_id) VALUES (?,?)", (2,2))
cur.execute("INSERT INTO presses (room_id, round_id) VALUES (?,?)", (28,2))
time.sleep(0.010)
cur.execute("INSERT INTO presses (room_id, round_id) VALUES (?,?)", (50,2))
cur.execute("INSERT INTO presses (room_id, round_id) VALUES (?,?)", (46,2))

connection.commit()
connection.close()
