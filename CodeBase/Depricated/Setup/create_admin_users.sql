CREATE TABLE IF NOT EXISTS admin_users (
    id INTEGER PRIMARY KEY,  -- Automatically increments the id
    username TEXT NOT NULL,
    password TEXT NOT NULL
);