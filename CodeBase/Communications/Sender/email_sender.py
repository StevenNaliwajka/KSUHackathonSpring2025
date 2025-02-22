import os
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from CodeBase.Communications.ParseData.message import Message
from CodeBase.Communications.ParseData.secret import Secret
from CodeBase.StandardFilePathing.get_message_folder import get_message_folder
from CodeBase.StandardFilePathing.get_secret_folder import get_secret_folder
from CodeBase.send_email import send_email

if __name__ == "__main__":
    # Define where codebase should look for "secret" location
    secret_path = get_secret_folder()
    # Define where messages folder should be generated
    messages_folder = get_message_folder()

    # Create Secret Object
    secret = Secret(secret_path)

    try:
        message_path = sys.argv[1]
    except IndexError:
        print("ERROR: Please provide the path to a JSON message file on calling of program.")
        sys.exit(1)

    message = Message(message_path)

    # Create the email message
    for to_email in message.recipients_list:
        msg = MIMEMultipart()
        msg["From"] = secret.user_email_address
        msg["To"] = to_email
        msg["Subject"] = message.subject
        msg.attach(MIMEText(message.body, "plain"))

        # Send the email
        try:
            server = smtplib.SMTP(secret.smtp_server, secret.smtp_port)
            server.starttls()  # Secure the connection
            server.login(secret.user_email_address, secret.app_password)
            server.sendmail(secret.user_email_address, to_email, msg.as_string())
            server.quit()
            print("Email sent successfully!")
        except Exception as e:
            print("Error:", e)
