from CodeBase.Communications.EmailSender.CodeBase.ConfigManager.create_default_email_json import \
    create_default_email_json
from CodeBase.Communications.EmailSender.CodeBase.ConfigManager.create_email_secret import create_secret


def setup_email_sender(secret_path, message_path):
    create_default_email_json(message_path)
    create_secret(secret_path)