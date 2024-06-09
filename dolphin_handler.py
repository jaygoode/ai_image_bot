from ollama import chat
import ollama
import os
import subprocess


class AiHandler:
    def __init__(self, image_folder):
        self.image_folder = image_folder

    def start_model(self, model_name):
        # results = subprocess.run(
        #     f"ollama run {model_name}", capture_output=True, text=True
        # )
        results = subprocess.run(f"ollama run {model_name}", shell=True)
        print(f"Return code: {results.returncode}")
        print(f"Return code: {results.stdout}")
        print(f"Return code: {results.stderr}")
        return results.returncode

    def chat(self, message: str) -> str:
        messages = [
            {
                "role": "user",
                "content": message,
            },
        ]
        response = ""
        for part in chat(model="dolphin-mixtral", messages=messages, stream=True):
            print(part["message"]["content"], end="", flush=True)
            response += part["message"]["content"]
        return response
        print()

    def ask_about_image(self, question: str, image_file: str) -> str:
        # TODO this does not yet work
        image_fp = os.path.join(self.image_folder, image_file)
        message = {
            "role": "user",
            "content": question,
            "images": [image_fp],
        }

        # Use the ollama.chat function to send the image and retrieve the description
        response = ollama.chat(
            model="llava",  # Specify the desired LLaVA model size
            messages=[message],
        )

        # Print the model's description of the image
        print(response["message"]["content"])
        return response["message"]["content"]


image_folder = f"C:\\Users\\johnny\\Desktop\\repos\\personal_repos\\fooocus\\Fooocus-api\\Fooocus-API\\outputs\\files\\2024-05-15"
ai_handler = AiHandler(image_folder)
breakpoint()
if ai_handler.start_model("dolphin-mixtral:latest"):
    image = "test.png"
    question = "what do you see in this image?"
    ai_handler.chat("hello")

ai_handler.ask_about_image(question, image)
