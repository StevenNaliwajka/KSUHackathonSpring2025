import os
from os import path


def get_database_path():
    # Global config Pathing. Changes here reflect everywhere.

    # Determines path of config folder
    # Generated on run.
    database_name = "sql_lite_db"
    # Qty of directories to rise
    num_directories = 3

    # Build path.
    current_directory = os.path.abspath(__file__)
    up_levels = ['..'] * num_directories
    parent_directory = os.path.abspath(os.path.join(current_directory, *up_levels))
    database_path = path.join(parent_directory, "DataBase", "Data", database_name)

    return database_path
