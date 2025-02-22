import re

from CodeBase.Communications.Sender.send_email import send_email
from CodeBase.Communications.Sender.send_text import send_text


def process_contact(contact):
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