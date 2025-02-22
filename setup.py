from os import path

from CodeBase.Communications.EmailSender.setup_email_sender import setup_email_sender
from CodeBase.Communications.TextSender.setup_text_sender import setup_text_sender
from CodeBase.FilePathing.get_config_path import get_config_path
from CodeBase.FilePathing.get_message_path import get_message_path
from CodeBase.FilePathing.get_secret_path import get_secret_path

if __name__ == "__main__":
    # Local Pathing is defined in the below methods. One change changes everywhere
    config_path = get_config_path()
    print("Config Path: ", config_path)
    secret_path = get_secret_path()
    print("Secret Path: ", secret_path)
    message_path = get_message_path()
    print("Message Path: ", message_path)


    setup_email_sender(secret_path, message_path)
    setup_text_sender(config_path, secret_path, message_path)