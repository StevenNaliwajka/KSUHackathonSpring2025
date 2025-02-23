import os

from CodeBase.Communications.ParseData.validate_json_file import validate_json_file
from CodeBase.Communications.Sender.process_contact import process_contact
from CodeBase.StandardFilePathing.get_message_folder import get_message_folder


def send_message(message_name):
    message_folder = get_message_folder()
    message_path = os.path.join(message_folder, message_name)

    try:
        data = validate_json_file(message_path)

        subject = data['SUBJECT']
        body = data['BODY']

        for contact in data["TO_EMAILS"]:
            process_contact(contact, subject, body)

    except:
        print("ERROR: Please verify the formating/contents of the JSON message file.")
        exit(1)
