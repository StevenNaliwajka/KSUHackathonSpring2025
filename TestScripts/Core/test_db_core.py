import os
import sys

from DataBase.Scripts.call_sql_script import call_sql_script

def test_db_core():
    # Example usage: dynamically provide a student_id parameter
    # Here, we're assuming you want to pass a student id to the SQL script.
    print("Testing Script")


    data = call_sql_script("get_athlete_soccer_data.sql", 100)
    print(data)
    data_2 = call_sql_script("get_athlete_vollyball.sql", 200)
    print(data_2)