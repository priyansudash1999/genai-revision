from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

result = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role":"system", "content": "You are an AI assistant and Your name is Mr. Dash"},
    {"role": "user", "content": "What is your name ?"}
  ]
)

print(result.choices[0].message.content)