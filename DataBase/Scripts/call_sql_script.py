import os


def call_sql_script(cursor, script_folder, script_name):
    # Calls SQL SCRIPT
    script_path = os.path.join(script_folder, script_name)

    with open(script_path, 'r') as file:
        sql_script = file.read()

    cursor.executescript(sql_script)
