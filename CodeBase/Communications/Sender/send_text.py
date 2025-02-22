import sys

from twilio.rest import Client

from CodeBase.Communications.ParseData.message import Message
from CodeBase.secret import Secret
from CodeBase.StandardFilePathing.get_secret_folder import get_secret_folder


def send_text():
    # Define where codebase should look for "secret" location
    secret_path = get_secret_folder()

    # Create Secret Object
    secret = Secret(secret_path)

    message = Message(message_path)

    # Your Twilio credentials
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    client = Client(account_sid, auth_token)

    # Create and send the message
    message = client.messages.create(
        body='Hello from Python!',
        from_='+1234567890',  # Your Twilio phone number
        to='+0987654321'  # Recipient's phone number
    )

    print(f"Message sent with SID: {message.sid}")

if __name__ == '__main__':
    # Ensure the correct number of arguments are provided
    try:
        message_path = sys.argv[1]
        send_text(message_path)
    except IndexError:
        print("ERROR: Please provide the path to a JSON message file on calling of program.")
        sys.exit(1)