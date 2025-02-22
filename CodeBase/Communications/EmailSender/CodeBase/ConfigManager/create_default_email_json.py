import json
from pathlib import Path


def create_default_email_json(message_path):
    path = Path(message_path)

    # Check if the directory exists; if not, create it (including any necessary parent directories)
    path.mkdir(parents=True, exist_ok=True)

    # Define the path to the JSON file within the folder
    json_file_path = path / "example_email.json"

    if not json_file_path.exists():
        # Define the JSON data to be written
        data = {
            "TO_EMAILS": [
                "JohnDoe123@gmail.com",
                "JaneDill456@gmail.com"
            ],
            "SUBJECT": "Test Email from Python",
            "BODY": "Hello, this is a test email sent using Python."
        }

        # Write the JSON data to the file with an indent for readability
        with open(json_file_path, "w") as json_file:
            json.dump(data, json_file, indent=2)
        print(f".json example email file created at: {json_file_path}")
    else:
        print(f".json example email file already exists at: {json_file_path}")
