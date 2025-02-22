import os
import sys

from CodeBase.FilePathing.get_message_path import get_message_path
from CodeBase.FilePathing.get_secret_path import get_secret_path
from CodeBase.Parse.message import Message
from CodeBase.Parse.secret import Secret
from CodeBase.send_email import send_email

if __name__ == "__main__":
    # Define where codebase should look for "secret" location
    secret_path = get_secret_path()
    # Define where messages folder should be generated
    messages_folder = get_message_path()

    # Create Secret Object
    secret = Secret(secret_path)

    try:
        message_path = sys.argv[1]
    except IndexError:
        print("ERROR: Please provide the path to a JSON message file on calling of program.")
        sys.exit(1)

    message = Message(message_path)
    send_email(message, secret)
