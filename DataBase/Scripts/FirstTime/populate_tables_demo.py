from DataBase.Scripts.call_sql_script import call_sql_script


def populate_tables_demo(cursor, script_folder):
    call_sql_script(cursor, script_folder, "demo_athlete_stat_table_1.sql")
    call_sql_script(cursor, script_folder, "demo_athlete_stat_table_2.sql")
    call_sql_script(cursor, script_folder, "demo_athletes.sql")
    call_sql_script(cursor, script_folder, "demo_master_student.sql")
    call_sql_script(cursor, script_folder, "demo_master_visitors.sql")
    call_sql_script(cursor, script_folder, "demo_notification_sport_1.sql")
    call_sql_script(cursor, script_folder, "demo_notification_sport_2.sql")
    call_sql_script(cursor, script_folder, "demo_notification_weather.sql")
    call_sql_script(cursor, script_folder, "demo_ongoing_events.sql")
    call_sql_script(cursor, script_folder, "demo_team.sql")
    call_sql_script(cursor, script_folder, "demo_admin_users.sql")
