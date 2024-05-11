









from openai import OpenAI

client = OpenAI(
    base_url='https://api.openai-proxy.org/v1',
    api_key='sk-u5h9Q4RB8GtRYMA9hgYjDyBeM0nMO6iprXALXiLT2Ypbk5G4',
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say hi",
        }
    ],
    model="gpt-3.5-turbo",
)
print(chat_completion)
