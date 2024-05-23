from vault import Vault
from logger_setup import logger
import os
from dotenv import load_dotenv
from selenium_handler import Selenium_Handler
from file_handler import FileHandler
from datetime import datetime as dt


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
    insta_username = os.environ.get("INSTA_USERNAME")
    insta_password = os.environ.get("INSTA_PASSWORD")
    archive_fp = ""
    date = dt.today().strftime("%Y-%m-%d")
    date = "2024-05-15"
    image_folder = f"C:\\Users\\johnny\\Desktop\\repos\\personal_repos\\fooocus\\Fooocus-api\\Fooocus-API\\outputs\\files\\{date}"
    instagram = Selenium_Handler(logger, insta_username, insta_password)
    file_handler = FileHandler(image_folder)
    instagram.open_instagram()
    instagram.login(username, password)

    for image in file_handler.get_files():
        instagram.create_post(image_folder + "\\" + image)
        file_handler.move_files(image_folder + "\\" + image)


if __name__ == "__main__":
    main()
