CREATE TABLE IF NOT EXISTS athlete_stat_table_2 (
    student_id INTEGER PRIMARY KEY,  -- Unique identifier for the athlete, references master_student(student_id)
    team_id INTEGER,                 -- Identifier for the team the athlete belongs to
    number INTEGER,                  -- Athlete's number (e.g., jersey number)
    passing_yards INTEGER,           -- Statistic for passing yards
    rushing_yards INTEGER,           -- Statistic for rushing yards
    FOREIGN KEY (student_id) REFERENCES master_student(student_id),
    FOREIGN KEY (team_id) REFERENCES Team(ID)
);