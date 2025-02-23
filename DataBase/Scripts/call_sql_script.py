import os
import sys
from CodeBase.StandardFilePathing.get_sql_scripts_folder import get_sql_scripts_folder
from CodeBase.get_db_conn_str import get_db_conn_str


def call_sql_script(script_name, params=None):
    """
    Executes an SQL script.

    - If it's a SELECT query, returns the results.
    - If it's an INSERT, UPDATE, or DELETE query, commits the transaction and returns the affected row count.

    :param script_name: Name of the SQL file to execute.
    :param params: Optional list of parameters to pass to the SQL query.
    :return: Query results (for SELECT) or affected row count (for INSERT/UPDATE/DELETE).
    """

    script_folder = get_sql_scripts_folder()
    script_path = os.path.join(script_folder, script_name)

    connection = get_db_conn_str()
    cursor = connection.cursor()

    print(f"Executing SQL Script: {script_path}")

    # Read the SQL query from the file
    with open(script_path, 'r') as file:
        sql_query = file.read().strip()

    # Execute query with parameters if provided
    if params:
        cursor.execute(sql_query, params)
    else:
        cursor.execute(sql_query)

    # Determine if query is a SELECT or a data-modifying query
    if sql_query.lower().startswith("select"):
        # Fetch results for SELECT queries
        rows = cursor.fetchall()
        result = [list(row) for row in rows]
    else:
        # Commit transaction for INSERT, UPDATE, DELETE
        connection.commit()
        result = cursor.rowcount  # Number of affected rows

    # Clean up resources
    cursor.close()
    connection.close()

    return result  # Returns result set or affected row count


if __name__ == '__main__':
    try:
        arguments = sys.argv[1:]
        script_name = arguments[0]  # First argument is script name
        params = arguments[1:]  # Rest are parameters

        result = call_sql_script(script_name, params)
        print(result)
    except IndexError:
        print("ERROR: Please provide a script name and parameters.")
        sys.exit(1)