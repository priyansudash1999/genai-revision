import fastapi
from ollama import Client


app = fastapi.FastAPI()
client = Client(
  host = 'http://localhost:11434',
)
client.pull('gemma3:1b')
@app.post("/chat")

def chat(message: str = fastapi.Body(... ,description="Chat message")):
  res = client.chat(
    model="gemma3:1b",
    messages=[
      {"role": "user", "content": message}
    ]
  )
  return res['message']['content']

