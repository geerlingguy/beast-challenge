DROP TABLE IF EXISTS rooms;
DROP TABLE IF EXISTS rounds;
DROP TABLE IF EXISTS presses;

CREATE TABLE rooms (
    room_id INTEGER PRIMARY KEY,
    mac_address TEXT NOT NULL,
    color TEXT NOT NULL DEFAULT('white'),
    live INTEGER DEFAULT(1),
    led_0 INTEGER DEFAULT(0),
    led_1 INTEGER DEFAULT(0),
    led_2 INTEGER DEFAULT(0)
);

CREATE TABLE rounds (
    round_id INTEGER PRIMARY KEY,
    start_time TIMESTAMP DATETIME,
    close_time TIMESTAMP DATETIME,
    is_live INTEGER NOT NULL DEFAULT(0),
    time_seconds INTEGER NOT NULL DEFAULT(300)
);

CREATE TABLE presses (
    press_id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP DATETIME NOT NULL DEFAULT(STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW')),
    room_id INTEGER NOT NULL,
    round_id INTEGER NOT NULL,
    FOREIGN KEY (room_id) REFERENCES rooms (room_id),
    FOREIGN KEY (round_id) REFERENCES rounds (round_id)
);
