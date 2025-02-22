from CodeBase.Communications.Setup.CreateJson.create_default_email_json import \
    create_default_email_json
from CodeBase.Communications.Setup.CreateSecret.create_email_secret import create_email_secret
from CodeBase.Communications.Setup.CreateJson.create_default_text_json import \
    create_default_text_json
from CodeBase.Communications.Setup.CreateSecret.create_text_secret import create_text_secret


def setup_communications(secret_path, message_path):
    # Setup Email
    create_default_email_json(message_path)
    create_email_secret(secret_path)
    # Setup text
    create_default_text_json(message_path)
    create_text_secret(secret_path)
