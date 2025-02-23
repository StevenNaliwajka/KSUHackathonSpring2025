from CodeBase.Communications.Sender.CoreMessageTypes.send_text import send_text

if __name__ == '__main__':
    # Example usage: dynamically provide a student_id parameter
    # Here, we're assuming you want to pass a student id to the SQL script.
    print("Testing Script")
    phone_number = "7702896896"
    send_text(phone_number, "Hello World", "Test")
    # print(data)