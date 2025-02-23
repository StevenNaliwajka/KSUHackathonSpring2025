from CodeBase.Communications.Sender.CoreMessageTypes.send_email import send_email

if __name__ == '__main__':
    # Example usage: dynamically provide a student_id parameter
    # Here, we're assuming you want to pass a student id to the SQL script.
    print("Testing Script")
    email_address = "Steven716@live.com"
    data = send_email(email_address, "Hello World", "Test")
    print(data)