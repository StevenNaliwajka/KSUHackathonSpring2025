import os

from dotenv import load_dotenv


class Secret:
    def __init__(self, secret_folder):
        # Email
        email_secret_path = os.path.join(secret_folder, 'mail_secret.env')
        load_dotenv(email_secret_path)
        self.smtp_server = os.getenv("SMTP_SERVER")
        self.smtp_port = os.getenv("SMTP_PORT")
        self.user_email_address = os.getenv("USER_EMAIL_ADDRESS")
        self.app_password = os.getenv("APP_PASSWORD")
        print(self.smtp_server)
        print(self.smtp_port)
        print(self.user_email_address)
        print(self.app_password)

        # Text
        text_secret_path = os.path.join(secret_folder, 'text_secret.env')
        load_dotenv(text_secret_path)
        print(text_secret_path)
        self.account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        self.auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        self.my_phone_number = os.getenv("TWILIO_PHONE_NUMBER")

        print(self.account_sid)
        print(self.auth_token)
        print(self.my_phone_number)

        # Database
        database_secret_path = os.path.join(secret_folder, 'mail_secret.env')
        load_dotenv(database_secret_path)