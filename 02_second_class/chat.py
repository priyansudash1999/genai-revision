from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages = [
    {"role": "user", "content": "Hello"}  # This is zero shot prompting
  ]
)

print(response.choices[0].message.content)