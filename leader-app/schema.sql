DROP TABLE IF EXISTS rooms;
DROP TABLE IF EXISTS rounds;
DROP TABLE IF EXISTS votes;

CREATE TABLE rooms (
    room_id INTEGER PRIMARY KEY,
    mac_address TEXT NOT NULL,
    color TEXT NOT NULL DEFAULT('white')
);

CREATE TABLE rounds (
    round_id INTEGER PRIMARY KEY,
    start_time TIMESTAMP DATETIME,
    close_time TIMESTAMP DATETIME,
    is_accepting_votes INTEGER NOT NULL DEFAULT(0),
    is_current INTEGER NOT NULL DEFAULT(0),
    is_allowing_multiple_votes INTEGER NOT NULL DEFAULT(1),
    value_0 TEXT DEFAULT('No'),
    value_1 TEXT DEFAULT('Yes'),
    value_2 TEXT
);

CREATE TABLE votes (
    vote_id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP DATETIME NOT NULL DEFAULT(STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW')),
    room_id INTEGER NOT NULL,
    value INTEGER NOT NULL,
    round_id INTEGER NOT NULL,
    FOREIGN KEY (room_id) REFERENCES rooms (room_id),
    FOREIGN KEY (round_id) REFERENCES rounds (round_id)
);
