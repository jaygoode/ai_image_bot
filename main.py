from vault import Vault
from logger_setup import logger
import os
from dotenv import load_dotenv
from selenium_handler import Selenium_Handler
from file_handler import FileHandler
from datetime import datetime as dt
import argparse
from dolphin_handler import AiHandler
import sys
from fooocus_api import generate_image


def main():
    parser = argparse.ArgumentParser(
        description="bot for generating, analyzing and posting images with captions and hashtags to instagram"
    )
    parser.add_argument(
        "-g",
        help="Generate images from list of strings in json doc",
        action="store_true",
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
    image_folder = f"C:\\Users\\johnny\\Desktop\\repos\\personal_repos\\fooocus\\Fooocus-api\\outputs\\files\\{date}"
    image_folder = f"C:\\Users\\johnny\\Desktop\\repos\\personal_repos\\fooocus\\Fooocus-api\\outputs\\files\\2024-05-15\\"
    state_file_filepath = "./state.yaml"

    file_handler = FileHandler(image_folder)
    file_handler.create_ai_state_file(state_file_filepath)
    file_handler.read_yaml_file(state_file_filepath)

    ai_handler = AiHandler(image_folder)
    try:
        if args.g:
            # if flag -g is added run code to generate images with Fooocus AI through API
            prompts_file = "./prompts_list.yaml"
            image_amount = 3
            negative_prompt = ""
            prompts = file_handler.read_yaml_file(prompts_file)
            if ai_handler.start_fooocus_model():
                breakpoint()
                for prompt in prompts["prompts"]:
                    generate_image.generate(prompt, negative_prompt, image_amount)

        if args.c:
            # with flag -c you can chat with an LLM, currently set to dolpin-mixtral uncensored.
            if ai_handler.start_model("dolphin-mixtral:latest"):
                image = "test.png"
                message = "what do you see in this image?"
                answer = ai_handler.chat(message)

        if args.a:
            # with flag -a you can have the llava model inspect images. ability of the model is underwhelming, seemingly useless for now.
            if ai_handler.start_model("llava:latest"):
                questions = [
                    "generate 10 descriptive words from this image, put them as strings in a python list, all strings starting with a hashtag",
                    "generate a motivating caption based on this image.",
                ]
                image = "test_image.png"
                answers = []
                for question in questions:
                    answers.append(
                        ai_handler.ask_about_image(question, image_folder + image)
                    )
                logger.info(answers)
                filepath = "./hashtags.yaml"
                file_handler.add_to_yaml_file(filepath, answers)
                logger.info(
                    "successfully generated hashtags and added them to hashtags.yaml"
                )

        if args.p:
            # flag -p is for running the selenium part to upload images from a specific folder to instagram.
            instagram = Selenium_Handler(logger, insta_username, insta_password)
            instagram.open_instagram()
            instagram.login(username, password)

            for image in file_handler.get_files():
                instagram.create_post(image_folder + "\\" + image)
                file_handler.move_files(image_folder + "\\" + image)
    except Exception as e:
        os._exit(1)

    sys.exit()


if __name__ == "__main__":
    main()
