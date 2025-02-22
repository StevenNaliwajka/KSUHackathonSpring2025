CREATE TABLE IF NOT EXISTS master_student (
    student_id INTEGER PRIMARY KEY,  -- Unique identifier for each student
    name TEXT NOT NULL,              -- Student's name
    email TEXT NOT NULL,             -- Student's email address
    phone TEXT                       -- Student's phone number (optional)
);