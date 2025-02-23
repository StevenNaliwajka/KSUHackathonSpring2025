import re

from CodeBase.Communications.Sender.CoreMessageTypes.send_email import send_email
from CodeBase.Communications.Sender.CoreMessageTypes.send_text import send_text
from CodeBase.Communications.Sender.send_sql import send_sql


def process_contact(contact, subject, body):
    # Checks for email.
    if "@" in contact:
        send_email(contact, subject, body)
    # Check if the contact is a phone number.
    # Remove dashes and spaces, and then check if the result is all digits.
    elif re.sub(r"[-\s]", "", contact).isdigit():
        cleaned_number = re.sub(r"[-\s]", "", contact)
        send_text(cleaned_number, subject, body)
    else:
        send_sql(contact, subject, body)