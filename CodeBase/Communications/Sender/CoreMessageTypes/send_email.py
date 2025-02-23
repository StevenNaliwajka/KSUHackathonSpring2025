import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from CodeBase.secret import Secret
from CodeBase.StandardFilePathing.get_secret_folder import get_secret_folder

def send_email(contact, subject, body):
    secret_path = get_secret_folder()
    secret = Secret(secret_path)

    msg = MIMEMultipart()
    msg["From"] = secret.user_email_address
    msg["To"] = contact
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        # Directly use SMTP_SSL for SSL connections
        server = smtplib.SMTP_SSL(secret.smtp_server, secret.smtp_port)
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