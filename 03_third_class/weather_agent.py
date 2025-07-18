from dotenv import load_dotenv
from openai import OpenAI
import os
import requests
import json

load_dotenv()
client = OpenAI()

TIMEZONE_API = os.getenv("TIMEZONE_API_KEY ")

def get_weather(city):
  print("tool called: get weather ", city)
  url =  f"https://wttr.in/{city}?format=%c+%t"
  response = requests.get(url)
  if response.status_code == 200:
    return f"The weather in {city} is {response.text}"
  return "something went wrong"

def get_date(city):
    print("Tool called: ", city)
    url = f"https://timeapi.io/api/time/current/zone?timeZone=Asia%2F{city}"
    response = requests.get(url)
    if response.status_code != 200:
        return "Something went wrong"

    data = response.json()
    return f"{data['day']}-{data['month']}-{data['year']}"


available_tools = {
  "get_weather": {
    "fn": get_weather,
    "description": "Takes a city name as an input and returns the current weather in city"
  },
  "get_date": {
    "fn": get_date,
    "description": "Takes a city name with its continent as an input and returns the current date in city"
  }
}

system_prompt = """
  You are an helpful AI assistant who is specialize in resolving user query.
  You work on start - plan - action - observe mode
  For the given user quey and available tools, plan the step by step execution based on planning.
  Select the relevant tool from the available tools and based on the tool selection you perform an action toall the tool and wait for the observation and baes on the observation from the tool call resolve the user query.

  Rules:-
  -  FOllow the output in json format
  - Always perform one step at a time and wait for next input
  - Carefully analyse the user query

  Available tools: 
  - get_weather: Takes a city name as an input and returns the current weather for the city
  - get_date: Takes a city name with its continent name and return the current date on the city.

  Output JSON format: 
  {{
    "step" : "string",
    "content": "string",
    "function" : "The name in function is the step is action",
    "input" : "The input parameter of the function"
  }}

  Example:-
  User query:- What is weather in Puri, Odisha, India ?
  Output:- {{"step": "analyse", "content": "The user is interested in weather data of Puri Jagannath, Odisha, India"}}
  Output:- {{"step": "plan", "content": "From the availabe tools I should call get_weather"}}
  Output:- {{"step": "action", "content": "get_weather", "input", "Puri"}}
  Output:- {{"step": "observe", "content": "12 degree celsius"}}
  Output: {{"step": "output", "content": "It is 12 degree celsius in Puri Jagannath, Odisha, India and It is very good for travelling"}}

  Example 2:-
  User query:- What is date in Puri, Asia ?
  Output:- {{"step": "analyse", "content": "The user is interested in date data of Puri Jagannath, Odisha, India"}}
  Output:- {{"step": "plan", "content": "From the availabe tools I should call get_date"}}
  Output:- {"step": "action", "content": "get_weather", "input": "Puri"}
  Output:- {{"step": "observe", "content": "18th July 2025"}}
  Output: {{"step": "output", "content": "It is 18th July 2025 in Puri Jagannath, Odisha, India, Asia"}}
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