import os
import sys

from CodeBase.StandardFilePathing.get_project_root import get_project_root
from DataBase.Scripts.call_sql_script import call_sql_script

if __name__ == '__main__':
    # Example usage: dynamically provide a student_id parameter
    # Here, we're assuming you want to pass a student id to the SQL script.
    print("Testing Script")
    proj_root = get_project_root()

    sys.path.append(os.path.abspath(proj_root))

    data = call_sql_script("get_athlete_soccer_data.sql", 100)
    print(data)
    data_2 = call_sql_script("get_athlete_vollyball.sql", 200)
    print(data_2)