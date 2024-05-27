from ollama import chat


class AiHandler:
    def __init__(self):
        pass

    def chat(self, message):
        messages = [
            {
                "role": "user",
                "content": message,
            },
        ]

        for part in chat("dolphin-mixtral", messages=messages, stream=True):
            print(part["message"]["content"], end="", flush=True)

        # end with a newline
        print()


ai = AiHandler()
ai.chat("hello")
