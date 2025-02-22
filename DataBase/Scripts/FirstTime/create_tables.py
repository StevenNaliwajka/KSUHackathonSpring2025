from DataBase.Scripts.call_sql_script import call_sql_script


def create_tables(cursor, script_folder):
    call_sql_script(cursor, script_folder, "create_athlete_stat_table_1.sql")
    call_sql_script(cursor, script_folder, "create_athlete_stat_table_2.sql")
    call_sql_script(cursor, script_folder, "create_athletes.sql")
    call_sql_script(cursor, script_folder, "create_master_student.sql")
    call_sql_script(cursor, script_folder, "create_master_visitors.sql")
    call_sql_script(cursor, script_folder, "create_notification_sport_1.sql")
    call_sql_script(cursor, script_folder, "create_notification_sport_2.sql")
    call_sql_script(cursor, script_folder, "create_notification_weather.sql")
    call_sql_script(cursor, script_folder, "create_ongoing_events.sql")
    call_sql_script(cursor, script_folder, "create_team.sql")
    call_sql_script(cursor, script_folder, "create_user.sql")
