import os
from os import path


def get_config_folder():
    # Global config Pathing. Changes here reflect everywhere.

    # Determines path of config folder
    # Generated on run.
    config_folder_name = "Config"
    # Qty of directories to rise
    num_directories = 3

    # Build path.
    current_directory = os.path.abspath(__file__)
    up_levels = ['..'] * num_directories
    parent_directory = os.path.abspath(os.path.join(current_directory, *up_levels))
    config_path = path.join(parent_directory, config_folder_name)

    return config_path
