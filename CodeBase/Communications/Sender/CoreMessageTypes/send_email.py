import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from CodeBase.Communications.ParseData.message import Message
from CodeBase.secret import Secret
from CodeBase.StandardFilePathing.get_secret_folder import get_secret_folder

def send_email(contact, subject, body):
    # Define where codebase should look for "secret" location
    secret_path = get_secret_folder()

    # Create Secret Object
    secret = Secret(secret_path)

    msg = MIMEMultipart()
    msg["From"] = secret.user_email_address
    msg["To"] = contact
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    # Send the email
    try:
        server = smtplib.SMTP(secret.smtp_server, secret.smtp_port)
        server.starttls()  # Secure the connection
        server.login(secret.user_email_address, secret.app_password)
        server.sendmail(secret.user_email_address, contact, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("Error:", e)


if __name__ == '__main__':
    # Ensure the correct number of arguments are provided
    try:
        contact = sys.argv[1]
        subject = sys.argv[2]
        body = sys.argv[3]
        send_email(contact, subject, body)
    except IndexError:
        print("ERROR: Please provide the path to a JSON message file on calling of program.")
        sys.exit(1)