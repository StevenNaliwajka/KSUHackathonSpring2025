import os
import sys  # Added import for sys

from CodeBase.StandardFilePathing.get_sql_scripts_folder import get_sql_scripts_folder
from CodeBase.get_db_conn_str import get_db_conn_str

def call_sql_script(script_name, params=None):
    script_folder = get_sql_scripts_folder()
    script_path = os.path.join(script_folder, script_name)
    # print(pyodbc.drivers())
    connection = get_db_conn_str()
    # Connect to the database
    # connection = pymssql.connect(conn_str)
    cursor = connection.cursor()
    print(script_path)
    # Read the SQL query from the SQL file
    with open(script_path, 'r') as file:
        sql_query = file.read()

    # Execute the query with parameters if provided
    if params:
        cursor.execute(sql_query, params)
    else:
        cursor.execute(sql_query)

    # Fetch all rows returned by the query
    rows = cursor.fetchall()

    # Convert the rows to a 2D array (list of lists)
    result_array = [list(row) for row in rows]

    # Clean up: close the cursor and connection
    cursor.close()
    connection.close()

    return result_array

if __name__ == '__main__':
    # Example usage: dynamically provide a student_id parameter
    # Here, we're assuming you want to pass a student id to the SQL script.
    try:
        arguments = sys.argv[1:]
        # Replace with your actual script name and dynamic input
        first_entry = arguments[0]  # The first argument
        rest_entries = arguments[1:]
        result = call_sql_script(first_entry, rest_entries)
        print(result)
    except IndexError:
        print("ERROR: Please provide the path to a JSON message file when calling the program.")
        sys.exit(1)