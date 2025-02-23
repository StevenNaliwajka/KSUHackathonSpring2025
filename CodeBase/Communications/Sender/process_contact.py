import re
from CodeBase.Communications.Sender.CoreMessageTypes.send_email import send_email
from CodeBase.Communications.Sender.CoreMessageTypes.send_text import send_text

def process_contact(contact, subject, body):
    from CodeBase.Communications.Sender.send_sql import send_sql  # Moved inside function

    print("Processing contact {}".format(contact))
    if "@" in contact:
        send_email(contact, subject, body)
    elif re.sub(r"[-\s]", "", contact).isdigit():
        cleaned_number = re.sub(r"[-\s]", "", contact)
        send_text(cleaned_number, subject, body)
    else:
        send_sql(contact, subject, body)
