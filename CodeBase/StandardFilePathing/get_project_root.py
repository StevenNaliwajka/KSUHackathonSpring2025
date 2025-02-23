import os
from os import path


def get_project_root():
    # Global message Pathing. Changes here reflect everywhere.

    this_directory = path.abspath(path.dirname(__file__))
    parent_directory = os.path.dirname(this_directory)

    # Message Folder Path:
    # Messages stores formating for broadcasting data in JSON files. Generated on run.
    message_folder_name = "Messages"
    # Qty of directories to rise
    num_directories = 3

    current_directory = os.path.abspath(__file__)
    up_levels = ['..'] * num_directories
    parent_directory = os.path.abspath(os.path.join(current_directory, *up_levels))

    return parent_directory
