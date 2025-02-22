def send_text():
    from twilio.rest import Client

    # Your Twilio credentials
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    client = Client(account_sid, auth_token)

    # Create and send the message
    message = client.messages.create(
        body='Hello from Python!',
        from_='+1234567890',  # Your Twilio phone number
        to='+0987654321'  # Recipient's phone number
    )

    print(f"Message sent with SID: {message.sid}")