from CodeBase.Communications.Sender.process_contact import process_contact
from DataBase.Scripts.call_sql_script import call_sql_script


def send_sql(query_name, subject, body):
    # call SQL Query and then pass the data to either send_email or send_text
    # ensure the data is 1d.

    new_contact_list = call_sql_script(query_name)

    for contact in new_contact_list:
        process_contact(contact, subject, body)
