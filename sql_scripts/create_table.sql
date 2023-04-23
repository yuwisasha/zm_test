CREATE TABLE IF NOT EXISTS cookie_profile (
    id INTEGER PRIMARY KEY NOT NULL,
    creation_time DATETIME NOT NULL,
    cookie TEXT,
    last_run_time DATETIME,
    run_count INTEGER DEFAULT 0
);