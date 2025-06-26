from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI()

text = "Shree Ram Mandir is in Ayodhya, UP, India. Established on 2024."

response = client.embeddings.create(
  input = text,
  model = "text-embedding-3-small"
)
print("Vector embedding of the text ", response.data[0].embedding)
