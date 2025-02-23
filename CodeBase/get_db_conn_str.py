import os

from dotenv import load_dotenv

from CodeBase.StandardFilePathing.get_secret_folder import get_secret_folder


def get_db_conn_str():
    # Database
    secret_folder = get_secret_folder()
    database_secret_path = os.path.join(secret_folder, 'mail_secret.env')
    load_dotenv(database_secret_path)


    conn_str = (
        f'DRIVER={driver};'
        f'SERVER={server};'
        f'DATABASE={database};'
        f'UID={username};'
        f'PWD={password}'
    )

    return conn_str