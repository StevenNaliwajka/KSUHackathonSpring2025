import os


def get_sql_scripts_folder():
    # Global config Pathing. Changes here reflect everywhere.

    # Determines path of config folder
    # Generated on run.
    script_folder = "SQLScripts"
    # Qty of directories to rise
    num_directories = 3

    # Build path.
    current_directory = os.path.abspath(__file__)
    up_levels = ['..'] * num_directories
    parent_directory = os.path.abspath(os.path.join(current_directory, *up_levels))
    database_path = os.path.join(parent_directory, "DataBase", script_folder)

    return database_path
