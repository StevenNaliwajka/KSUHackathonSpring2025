CREATE TABLE IF NOT EXISTS master_visitors (
    email TEXT PRIMARY KEY,  -- Email as the unique identifier
    name TEXT NOT NULL,      -- Visitor's name
    phone TEXT               -- Visitor's phone number
);