import json
from pathlib import Path


def create_default_text_json(message_path):
    path = Path(message_path)

    # Check if the directory exists; if not, create it (including any necessary parent directories)
    path.mkdir(parents=True, exist_ok=True)

    # Define the JSON data to be written
    data = {
        "TO_TEXT": [
            "770-999-8855",
            "404-223-8565"
        ],
        "SUBJECT": "Test TEXT from Python",
        "BODY": "Hello, this is a test text sent using Python."
    }

    # Define the path to the JSON file within the folder
    json_file_path = path / "example_text.json"

    # Write the JSON data to the file with an indent for readability
    with open(json_file_path, "w") as json_file:
        json.dump(data, json_file, indent=2)
