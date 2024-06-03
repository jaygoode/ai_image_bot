from ollama import chat
import ollama
import os


class AiHandler:
    def __init__(self, image_folder):
        self.image_folder = image_folder

    def chat(self, message):
        messages = [
            {
                "role": "user",
                "content": message,
            },
        ]

        for part in chat(model="dolphin-mixtral", messages=messages, stream=True):
            print(part["message"]["content"], end="", flush=True)

        print()

    def ask_about_image(self, question, image_file):
        image_fp = os.path.join(self.image_folder, image_file)
        with open(image_fp, "rb") as file:
            message = [{"role": "user", "content": {question}, "image": [file.read()]}]
            response = ollama.chat(model="llava", messages=message)
        print(response["message"]["content"])


image_folder = f"C:\\Users\\johnny\\Desktop\\repos\\personal_repos\\fooocus\\Fooocus-api\\Fooocus-API\\outputs\\files\\2024-05-15"
image_folder = f"C:\\Users\\johnny\\Desktop\\repos\\personal_repos\\fooocus\\Fooocus-api\\Fooocus-API\\outputs\\files\\2024-05-15"
ai = AiHandler(image_folder)
image = "test.png"
question = "what do you see in this image?"
ai.ask_about_image(question, image)
ai.chat("hello")
