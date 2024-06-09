from vault import Vault
from logger_setup import logger
import os
from dotenv import load_dotenv
from selenium_handler import Selenium_Handler
from file_handler import FileHandler
from datetime import datetime as dt
import argparse
from dolphin_handler import AiHandler


def main():
    parser = argparse.ArgumentParser(
        description="bot for generating, analyzing and posting images with captions and hashtags to instagram"
    )
    parser.add_argument(
        "-g", type=str, help="Generate images from list of strings in json doc"
    )
    parser.add_argument(
        "-c",
        help="chat with LLM",
        action="store_true",
    )
    parser.add_argument(
        "-p",
        help="Post images from folder to instagram",
        action="store_true",
    )
    parser.add_argument(
        "-a",
        help="Analyze images from folder and get a text back with description",
        action="store_true",
    )

    args = parser.parse_args()

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
    image_folder = f"C:\\Users\\johnny\\Desktop\\repos\\personal_repos\\fooocus\\Fooocus-api\\Fooocus-API\\outputs\\files\\2024-05-15\\"
    file_handler = FileHandler(image_folder)
    ai_handler = AiHandler(image_folder)

    if args.c:
        if ai_handler.start_model("dolphin-mixtral:latest"):
            image = "test.png"
            question = "what do you see in this image?"
            ai_handler.chat("hello")

    if args.a:
        if int(ai_handler.start_model("llava:latest")) == 0:
            question = "what do you see in this image?"
            image = "test.png"
            breakpoint()
            ai_handler.ask_about_image(question, image_folder + image)

    if args.p:
        instagram = Selenium_Handler(logger, insta_username, insta_password)
        instagram.open_instagram()
        instagram.login(username, password)

        for image in file_handler.get_files():
            instagram.create_post(image_folder + "\\" + image)
            file_handler.move_files(image_folder + "\\" + image)


if __name__ == "__main__":
    main()
