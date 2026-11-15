from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv("OPENAI_API_KEY")

print("Loaded Key =", key)

client = OpenAI(api_key=key)

history = []

while True:

    user_input = input("How can I help you: ")

    if user_input.lower() == "exit":
        break

    history.append({
        "role": "user",
        "content": user_input
    })

    response = client.responses.create(
        model="gpt-5.4-mini",
        input=history
    )

    ai_reply = response.output_text

    print("AI:", ai_reply)

    history.append({
        "role": "assistant",
        "content": ai_reply
    })