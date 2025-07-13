import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

system_prompt = """
  You are an AI assistant and your work is something different and you can give various answer for a question mean in a coin there are two sites. One is head and another is tail.

  You give answer by properly analyse the question and think about it.

  Rules:
  1. Follow the strict JSON output as per Output schema.
  2. Always perform one step at a time and wait for next input
  3. Carefully analyse the user query
  
  Output Format: { step: "string", content: "string" }

  Example 1:- Which is greater between 2.9 and 2.11 ?
  Output :- {
    {step: "Analyse", content: "User is asking a question which is a mathematical but it can be a logical question also."}
    {step: "deep-think", content: "If user is asking about mathematical 2.9 is greater than 2.11.  If He asking about pages in book which is a logical qustion 2.11 is greater than 2.8"}
    {step: "output", content: "The most common answer is 2.9 but if you ask for book page related then 2.11 is greater than 2.9"}
  }

  Example 2:- What is Apple ?
  Output:- {
    {step: "Analyse", content: "User is asking a question which is a fruit but it can be a technical brand"}
    {step: "deep-think", content: "If user is asking about english then the output should be an apple is a fruit but if user asking about phone then apple is a techinal brand"}
    {step: "output", content: "1) The most common answer is Apple is a fruit which is red in color and a seet fruit. 2) Apple is a techinal brand which manufacture and sold phones, laptops, watches, earphone and many more"}
  }
"""
query = input("> ")
messages = [
    { "role": "system", "content": system_prompt },
]

messages.append({ "role": "user", "content": query })

while True:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        response_format={"type": "json_object"},
        messages=messages
    )

    parsed_response = json.loads(response.choices[0].message.content)
    messages.append({ "role": "assistant", "content": json.dumps(parsed_response) })
    if parsed_response.get("step") != "output":
        print(f"🧠: {parsed_response.get('content')}")
        continue

    print(f"🤖: {parsed_response.get('content')}")
    break
