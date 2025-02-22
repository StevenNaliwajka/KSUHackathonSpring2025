import os
from os import path


def get_message_path():
    # Global message Pathing. Changes here reflect everywhere.

    this_directory = path.abspath(path.dirname(__file__))
    parent_directory = os.path.dirname(this_directory)

    # Message Folder Path:
    # Messages stores formating for broadcasting data in JSON files. Generated on run.
    message_folder_name = "Messages"
    message_path = path.join(parent_directory, "Communications", message_folder_name)

    return message_path