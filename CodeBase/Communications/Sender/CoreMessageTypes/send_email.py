import sys
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from CodeBase.secret import Secret
from CodeBase.StandardFilePathing.get_secret_folder import get_secret_folder

def send_email(contact, subject, body):
    secret_path = get_secret_folder()
    secret = Secret(secret_path)

    msg = MIMEMultipart()
    # print(secret.user_email_address)
    msg["From"] = secret.user_email_address
    msg["To"] = contact
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        # Create an SSL context
        context = ssl.create_default_context()

        # Instantiate the SMTP object with server and port so that self.host is set
        server = smtplib.SMTP(secret.smtp_server, secret.smtp_port)
        # server.set_debuglevel(1)  # Enable debug output
        #print(f"smtp_server {secret.smtp_server}")
        #print(f"smtp_port {secret.smtp_port}")

        server.ehlo()
        # Call starttls() with the SSL context (do not pass server_hostname)
        server.starttls(context=context)
        server.ehlo()

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