DROP TABLE IF EXISTS votes;
DROP TABLE IF EXISTS rounds;
DROP TABLE IF EXISTS stations;

CREATE TABLE stations (
    station_id INTEGER PRIMARY KEY,
    mac_address TEXT NOT NULL
);

CREATE TABLE rounds (
    round_id INTEGER PRIMARY KEY,
    start_time TIMESTAMP DATETIME,
    close_time TIMESTAMP DATETIME,
    is_open INTEGER NOT NULL DEFAULT(0),
    is_current INTEGER NOT NULL DEFAULT(0),
    value_0 TEXT NOT NULL DEFAULT('No'),
    value_1 TEXT NOT NULL DEFAULT('Yes')
);

CREATE TABLE votes (
    vote_id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP DATETIME NOT NULL DEFAULT(STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW')),
    station_id INTEGER NOT NULL,
    value INTEGER NOT NULL,
    round_id INTEGER NOT NULL,
    FOREIGN KEY (station_id) REFERENCES stations (station_id),
    FOREIGN KEY (round_id) REFERENCES rounds (round_id)
);
