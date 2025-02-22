CREATE TABLE IF NOT EXISTS user_picks (
    email INTEGER PRIMARY KEY,  -- Automatically increments the ID
    event_id INTEGER NOT NULL,
    pick_1 INTEGER CHECK(is_active IN (0, 1))
    pick_2 INTEGER CHECK(is_active IN (0, 1))
    pick_3 INTEGER CHECK(is_active IN (0, 1))
    pick_4 INTEGER CHECK(is_active IN (0, 1))
    pick_5 INTEGER CHECK(is_active IN (0, 1))
    pick_total INTEGER
);