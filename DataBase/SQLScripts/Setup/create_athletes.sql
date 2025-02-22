CREATE TABLE IF NOT EXISTS athletes (
    student_id INTEGER PRIMARY KEY,  -- Unique identifier for the athlete, referencing a student
    team_id INTEGER,                 -- Identifier for the team the athlete belongs to
    bio TEXT,                        -- Biography or additional details about the athlete
    year INTEGER,                    -- Typically the year of participation or academic year
    FOREIGN KEY (student_id) REFERENCES master_student(student_id),
    FOREIGN KEY (team_id) REFERENCES Team(ID)
);