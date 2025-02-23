import re

from CodeBase.Communications.ParseData.validate_json_file import validate_json_file
from CodeBase.Communications.Sender.CoreMessageTypes.send_email import send_email
from CodeBase.Communications.Sender.send_sql import send_sql
from CodeBase.Communications.Sender.CoreMessageTypes.send_text import send_text


class Message:
    def __init__(self, message_path):
        # Loads JSON file and parses
        data = validate_json_file(message_path)
        try:
            '''
            # Loads email recipients from 'data'
            self.recipients_list = []
            for email in data["TO_EMAILS"]:
                self.recipients_list.append(email)

            # loads subject and body.
            self.subject = data["SUBJECT"]
            self.body = data["BODY"]
            '''
            for contact in data["TO_EMAILS"]:
                # Checks for email.
                if "@" in contact:
                    send_email(contact)
                # Check if the contact is a phone number.
                # Remove dashes and spaces, and then check if the result is all digits.
                elif re.sub(r"[-\s]", "", contact).isdigit():
                    cleaned_number = re.sub(r"[-\s]", "", contact)
                    send_text(cleaned_number)
                else:
                    send_sql(contact)

        except:
            print("ERROR: Please verify the formating/contents of the JSON message file.")
            exit(1)
