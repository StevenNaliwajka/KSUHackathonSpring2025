from pathlib import Path


def create_secret(secret_path):
    path = Path(secret_path)

    # Create the directory if it doesn't exist (including parent directories if needed)
    path.mkdir(parents=True, exist_ok=True)

    # Define the contents of the .env file
    env_content = """SMTP_SERVER=
SMTP_PORT=
USER_EMAIL_ADDRESS=
APP_PASSWORD="""

    # Define the path for the .env file
    env_file_path = path / "mail_secret.env"

    # Write the contents to the .env file
    with open(env_file_path, "w") as env_file:
        env_file.write(env_content)

    print(f".env file created at: {env_file_path}")