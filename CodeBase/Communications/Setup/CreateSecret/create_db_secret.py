from pathlib import Path


def create_db_secret(secret_path):
    path = Path(secret_path)

    # Create the directory if it doesn't exist (including parent directories if needed)
    path.mkdir(parents=True, exist_ok=True)

    # Define the path for the .env file
    env_file_path = path / "db_secret.env"

    if not env_file_path.exists():
        # Define the contents of the .env file
        env_content = """DB_SERVER=
DB_PORT=
DB_NAME=
DB_USERNAME=
DB_PASSWORD="""

        # Write the contents to the .env file
        with open(env_file_path, "w") as env_file:
            env_file.write(env_content)
        print(f".env file created at: {env_file_path}")
    else:
        print(f".env file already exists at: {env_file_path}")