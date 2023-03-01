DROP TABLE IF EXISTS votes;
DROP TABLE IF EXISTS rounds;

CREATE TABLE votes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP DATETIME NOT NULL DEFAULT(STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW')),
    station INTEGER NOT NULL,
    button INTEGER NOT NULL
);

CREATE TABLE rounds (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    start TIMESTAMP DATETIME NOT NULL DEFAULT(STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW')),
    closed TIMESTAMP DATETIME,
    name TEXT NOT NULL
);

--- TODO: create table current_round to track what round we are currently in
--- TODO: create table stations to track stations (maybe associate MAC address to station ID?)
