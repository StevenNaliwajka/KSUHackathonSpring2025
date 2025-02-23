SELECT
    a.student_id,
    a.assists,
    t.first_name,
    t.last_name,
    t.player_headshot_url

FROM
    AVG_STAT_VOLLEYBALL AS a
LEFT JOIN
    ATHLETES AS t
    ON a.student_id = t.student_id
WHERE
    a.student_id = %s;