from CodeBase.Communications.EmailSender.setup_email_sender import setup_email_sender
from CodeBase.Communications.TextSender.setup_text_sender import setup_text_sender
from CodeBase.FilePathing.get_config_folder import get_config_folder
from CodeBase.FilePathing.get_database_path import get_database_path
from CodeBase.FilePathing.get_message_folder import get_message_folder
from CodeBase.FilePathing.get_secret_folder import get_secret_folder
from DataBase.Scripts.FirstTime.create_db_and_populate import create_db_and_populate

if __name__ == "__main__":
    # Local Pathing is defined in the below methods. One change changes everywhere
    config_folder = get_config_folder()
    # print("Config folder: {}".format(config_folder))
    secret_folder = get_secret_folder()
    # print("Secret folder: {}".format(secret_folder))
    message_folder = get_message_folder()
    # print("Message folder: {}".format(message_folder))
    database_path = get_database_path()
    # print("Database path: {}".format(database_path))

    # Setups local files for email sender and text sender.
    setup_email_sender(secret_folder, message_folder)
    setup_text_sender(config_folder, secret_folder, message_folder)

    # Creates local DB and populates tables with dummy data.
    create_db_and_populate(database_path)
