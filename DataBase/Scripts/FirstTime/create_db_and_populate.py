import os
import sqlite3
from CodeBase.StandardFilePathing.get_sql_scripts_folder import get_sql_scripts_folder
from DataBase.Scripts.FirstTime.create_tables import create_tables
from DataBase.Scripts.FirstTime.populate_tables_demo import populate_tables_demo


def create_db_and_populate(database_path):
    if os.path.exists(database_path):
        print("Database already exists, skipping creation.")
        return  # Skip the rest if the database exists

    # Make directory if not existing.
    parent_directory = os.path.abspath(os.path.join(database_path, '..'))
    os.makedirs(parent_directory, exist_ok=True)
    print(parent_directory)

    # Create and initialize the database
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    # Create tables
    script_folder = get_sql_scripts_folder()
    setup_script_folder = os.path.join(script_folder, "Setup")
    create_tables(cursor, setup_script_folder)
    # POPULATES DEMO DATA
    demo_script_folder = os.path.join(setup_script_folder, "Demo")
    populate_tables_demo(cursor, demo_script_folder)

    conn.commit()
    conn.close()

    print("Database created and initialized.")
