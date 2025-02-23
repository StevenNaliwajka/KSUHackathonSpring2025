import os
import pyodbc

from CodeBase.StandardFilePathing.get_sql_scripts_folder import get_sql_scripts_folder
from CodeBase.get_db_conn_str import get_db_conn_str


def call_sql_script(script_name):
    script_folder = get_sql_scripts_folder()
    script_path = os.path.join(script_folder, script_name)

    conn_str = get_db_conn_str()
    # Connect to the database
    connection = pyodbc.connect(conn_str)
    cursor = connection.cursor()

    # Read the SQL query from a local file (replace 'path/to/query.sql' with your file path)
    with open(script_path, 'r') as file:
        sql_query = file.read()

    # Execute the query
    cursor.execute(sql_query)

    # Fetch all rows returned by the query
    rows = cursor.fetchall()

    # Convert the rows to a 2D array (list of lists)
    result_array = [list(row) for row in rows]

    # Clean up: close the cursor and connection
    cursor.close()
    connection.close()

    # return the result
    return result_array
