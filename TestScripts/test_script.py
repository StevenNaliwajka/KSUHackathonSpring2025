from DataBase.Scripts.call_sql_script import call_sql_script

if __name__ == '__main__':
    # Example usage: dynamically provide a student_id parameter
    # Here, we're assuming you want to pass a student id to the SQL script.
    print("Testing Script")

    data = call_sql_script("get_athlete_soccer_data.sql")
    print(data)