from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

while True:
    user = input("You: ")
    
    response = client.responses.create(
        model="gpt-5.4-mini",
        input=user
    )

    print("AI:", response.output_text)
