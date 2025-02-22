CREATE TABLE IF NOT EXISTS ongoing_events (
    event_id INTEGER PRIMARY KEY,  -- Automatically increments the event_id
    venue TEXT NOT NULL,
    interruption_time TEXT,        -- You can use DATETIME if preferred, but TEXT is common in SQLite
    interruption_reason TEXT
);