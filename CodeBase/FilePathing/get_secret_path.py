import os
from os import path


def get_secret_path():
    # Global secret Pathing. Changes here reflect everywhere.

    # Secret Folder Path:
    # Secret Folder stores sensitive login data. Generated on run.
    secret_folder_name = "Secret"
    # Qty of directories to rise
    num_directories = 3

    # Build path.
    current_directory = os.path.abspath(__file__)
    up_levels = ['..'] * num_directories
    parent_directory = os.path.abspath(os.path.join(current_directory, *up_levels))
    secret_path = path.join(parent_directory, secret_folder_name)
    return secret_path