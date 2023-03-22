DROP TABLE IF EXISTS rooms;
DROP TABLE IF EXISTS countdown_state;
DROP TABLE IF EXISTS presses;

CREATE TABLE rooms (
    room_id INTEGER PRIMARY KEY,
    color TEXT NOT NULL DEFAULT('off'),
    time_expired INTEGER DEFAULT(0),
    live INTEGER DEFAULT(1)
);

CREATE TABLE countdown_state (
    id INTEGER PRIMARY KEY,
    last_change TIMESTAMP DATETIME NOT NULL DEFAULT(STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW')),
    time_seconds INTEGER NOT NULL DEFAULT(300)
);

CREATE TABLE presses (
    press_id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP DATETIME NOT NULL DEFAULT(STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW')),
    room_id INTEGER NOT NULL,
    FOREIGN KEY (room_id) REFERENCES rooms (room_id)
);
