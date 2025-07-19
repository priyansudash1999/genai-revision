from openai import OpenAI
from dotenv import load_dotenv
import os
import json
import requests



load_dotenv()
client = OpenAI()
my_brain_key = os.getenv("OPENAI_API_KEY")
google_api_key = os.getenv("GOOGLE_SEARCH_API")
google_csd = os.getenv("GOOGLE_CSE_ID")





def search_on_google(query, api_key, cse_id):
  url = f"https://cse.google.com/cse?cx={cse_id}"
  params = {
      "q": query,
      "key": api_key,
      "cx": cse_id
    }
  resp = requests.get(url, params=params)
  return resp.json()


available_tools = {
  "search_on_google":{
    "fn": search_on_google,
    "description": "Takes user input and give output after your opeation through my function"
  }
}

system_prompt = """
  You are an helpful AI assistant who is specialize in searching google and solve user query.

  You work on start - plan - observe - action mode

  Always priortize about safe search.
  Only text based data you will provide.

  - search_on_google function has 3 params which are query which is given by user. api_key which is google_api_key and cse_id which is google_csd

  Rules:-
  -  FOllow the output in json format
  - Always perform one step at a time and wait for next input
  - Carefully analyse the user query

  Availble tools:-
  - search_on_google - Takes user input and give output after your opeation through my function and your thoughts

  Output JSON format: 
  {{
    "step" : "string",
    "content": "string",
    "function" : "The name in function is the step is action",
    "input" : "The input parameter of the function"
  }}


  Example 1:-
  User query:- What is weather in Puri, Odisha, India ?
  Output:- {{"step": "analyse", "content": "The user is interested in weather data of Puri Jagannath, Odisha, India"}}
  Output:- {{"step": "plan", "content": "From the availabe tools I should call search_on_google"}}
  Output:- {{"step": observe", "content": "User is asking about weather based data and it is safe to search"}}
  Output:- {{"step": "action", "content": "search_on_google", "input", "What is weather in Puri, Odisha, India"}}
  Output:- {{"step": "result", "content" : "The weather is 19 degree celsius with some clouds in sky and safe to travel"}}
"""


while True:
  user_query = input("> ")

  messages = [
    {"role": "system", "content": system_prompt}
  ]
  messages.append({"role": "user", "content": user_query})
  while True:
    response = client.chat.completions.create(
      model="gpt-4o",
      response_format= {"type": "json_object"} ,
      messages= messages
    )
    parsed_output = json.loads(response.choices[0].message.content)
    messages.append({"role": "assistant", "content": json.dumps(parsed_output)})

    if parsed_output.get("step") == "plan":
      print(f"Thinking {parsed_output.get('content')}")
      continue

    if parsed_output.get("step") == "action":
      tool_name = parsed_output.get("function")
      tool_input = parsed_output.get("input")

      if available_tools.get(tool_name, False) != False:
        output = available_tools[tool_name].get("fn")(tool_input)
        messages.append({
          "role": "assistant",
          "content": json.dumps({"step": "observe", "content": output})
        })

        continue
    if parsed_output.get("step") == "output":
      print(f"Answer:- {parsed_output.get('content')}")
      break

