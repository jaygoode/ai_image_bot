from ollama import chat
import ollama
import os
import subprocess
from logger_setup import logger
from time import sleep


class AiHandler:
    def __init__(self, image_folder):
        self.image_folder = image_folder

    def start_fooocus_model(self):
        try:
            process = subprocess.Popen(
                f"python C:\\Users\\johnny\Desktop\\repos\\personal_repos\\fooocus\\image_bot\\fooocus_api\\main.py",
                # stdout=subprocess.PIPE,
                # stderr=subprocess.PIPE,
                shell=True,
            )
            # Wait for the process to fully terminate
            sleep(5)
            # stdout, stderr = process.communicate()
            # stdout = stdout.decode("utf-8")
            # stderr = stderr.decode("utf-8")
            # breakpoint()

            # print("Standard Output:", stdout)
            # print("Standard Error:", stderr)
            # process.terminate()
            # stdout, stderr = process.communicate(timeout=15)
            # logger.info(f"Return code: {process.returncode}")
            # logger.info(f"Return code: {stdout}")
            # logger.info(f"Return code: {stderr}")
            # if process.returncode:
            #     pass
            return True
            return process.returncode
            # process.terminate()
            # stdout, stderr = process.communicate(timeout=15)
            # logger.info(f"Return code: {process.returncode}")
            # logger.info(f"Return code: {stdout}")
            # logger.info(f"Return code: {stderr}")
            # if process.returncode:
            #     pass
            # return process.returncode
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            # Kill the program immediately
            os._exit(1)

    def start_model(self, model_name):
        # TODO FIX
        # return True
        try:
            # results = subprocess.run(f"ollama run {model_name}", shell=True)
            process = subprocess.Popen(
                f"ollama run {model_name}",
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True,
            )
            # Wait for the process to fully terminate
            # sleep(5)
            process.stdin.write(b"/bye\n")
            process.terminate()
            stdout, stderr = process.communicate(timeout=15)
            logger.info(f"Return code: {process.returncode}")
            logger.info(f"stdout: {stdout}")
            logger.info(f"stderr: {stderr}")
            if process.returncode:
                pass
            return process.returncode
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            # Kill the program immediately
            os._exit(1)

    def chat(self, message: str) -> str:
        messages = [
            {
                "role": "user",
                "content": message,
            },
        ]
        response = ""
        for part in chat(model="dolphin-mixtral", messages=messages, stream=True):
            logger.info(part["message"]["content"], end="", flush=True)
            response += part["message"]["content"]
        return response

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
        logger.info(response["message"]["content"])
        return response["message"]["content"]
