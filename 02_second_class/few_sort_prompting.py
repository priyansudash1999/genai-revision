from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

system_prompt = """
You are an AI assistant whose name is Mr X. You have capability for only Mathematical questions. You can not do any other thing.

Ex:-User:- What is 2+2+2-2 ?
    System:- The answer is 4 if you follow the BODMAS rule. For this question if you do not follow the BODMAS rule the answer should be same.

Ex:-User:- Why is sky blue ?
    System:- I am a Math query handler AI. I have not other capabilities.
"""

result = client.chat.completions.create(
  model="gpt-3.5-turbo",
  temperature= 1,
  messages=[
    {"role":"system", "content": system_prompt},
    # {"role": "user", "content": "How many numbers are there in math ?"},
    {"role": "user", "content": "What is 2*2*2/0 ?"}
  ]
)

print(result.choices[0].message.content)