CREATE TABLE IF NOT EXISTS notification_weather (
    phone TEXT NOT NULL,
    event_id INTEGER PRIMARY KEY,
    FOREIGN KEY(event_id) REFERENCES ongoing_events(event_id)
);