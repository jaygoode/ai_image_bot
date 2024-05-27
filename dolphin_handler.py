from ollama import chat

message = "hello"
messages = [
    {
        "role": "system",
        "content": message,
    },
]

for part in chat("dolphin-mixtral", messages=messages, stream=True):
    print(part["message"]["content"], end="", flush=True)

# end with a newline
print()
