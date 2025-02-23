CREATE TABLE IF NOT EXISTS notification_sport_1 (
    email TEXT PRIMARY KEY,
    email_notif INTEGER NOT NULL,  -- 0 (false) or 1 (true)
    phone_notif INTEGER NOT NULL   -- 0 (false) or 1 (true)
);