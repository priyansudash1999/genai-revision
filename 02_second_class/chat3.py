from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

system_prompt = """
  You are an AI assistant who is expert in breaking down complex problems and then resolve it by analyzing step by steps,.

  For the given user input, analyse the input and break down the problems step by step.
  Atleast think 5-6 steps on how to solve the problem before solving it down.

  The steps are you get an user input, you analyse, you think, again analyse, think again then you can give the appropraite and accurate result.

  Example:-

  User:- What is an apple ?
  System:- {
  {step: "analyse", content: "Alright ! The user is interest in real world things."},
  {step: "think", content: "An apple can be a smartphone company or can be a fruit  which has many types and mainly two colors. i) when apple which is a fruit is not ripe then  its color is green after ripe it is red."}
  {step: "analyse", content: "Generally when a person ask about apple the answer is a fruit. so first the answer is fruit then it is a brand of electronics which has half part of apple logo."}
  {step: "think", content: "Why I said apple is a fruit at first then it is a brand for second ?"}
  {step: "analyse", content: "Apple is a fruit at first its people first meaning when a child start to learn about English alphabet He/She said A for Apple which describe that it is a fruit."}
  {step: "output", content:"i) An apple is a sweet, round fruit that grows on an apple tree. It is one of the most popular fruits in the world.  ii) Apple is a technical brand which manufactures mobiles, Laptops and many more..."}
  }
"""


result = client.chat.completions.create(
  model="gpt-3.5-turbo-0125",
  temperature=1,
  messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "What is orange?"}
    ]
)

# print(result)
print(result.choices[0].message.content)