import sys

from twilio.rest import Client

from CodeBase.secret import Secret
from CodeBase.StandardFilePathing.get_secret_folder import get_secret_folder


def send_text(contact, subject, body):
    # Define where codebase should look for "secret" location
    secret_path = get_secret_folder()

    # Create Secret Object
    secret = Secret(secret_path)

    # Your Twilio credentials
    account_sid = secret.account_sid
    auth_token = secret.auth_token
    client = Client(account_sid, auth_token)

    # Create and send the message
    message = client.messages.create(
        body=f"{subject}\n{body}",
        from_=secret.my_phone_number,  # Your Twilio phone number
        to=contact  # Recipient's phone number
    )

    print(f"Message sent with SID: {message.sid}")

if __name__ == '__main__':
    # Ensure the correct number of arguments are provided
    try:
        contact = sys.argv[1]
        subject = sys.argv[2]
        body = sys.argv[3]
        send_text(contact, subject, body)
    except IndexError:
        print("ERROR: Please provide the path to a JSON message file on calling of program.")
        sys.exit(1)