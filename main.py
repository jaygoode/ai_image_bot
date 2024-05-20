from vault import Vault
from logger_setup import logger
import os
from dotenv import load_dotenv
from selenium_handler import Selenium_Handler
from file_handler import FileHandler


def main():
    load_dotenv()
    vault_token = os.environ.get("VAULT_TOKEN")
    vault_url = os.environ.get("VAULT_URL")
    secret_path = os.environ.get("SECRET_PATH")
    username = os.environ.get("USERNAME")
    password = os.environ.get("PASSWORD")

    # vault = Vault(vault_token, vault_url)
    # vault.authenticate_client()
    # username, password = vault.get_credentials(secret_path)
    archive_fp = ""

    instagram = Selenium_Handler()
    file_handler = FileHandler("")
    instagram.open_instagram()
    instagram.login(username, password)

    for image in file_handler.get_files():
        instagram.create_post(image)
        file_handler.move_files(image, archive_fp)


if __name__ == "__main__":
    main()
