# Summary of the class

- GIGO Concept
- Prompt Engineering is an art.
  - Zero-shot prompting
  - Few-shot prompting
  - Chain-of-thought
  - Persona based Prompt
  - Role playing prompt
  - Contextual prompt
  - Multimedia prompt

# Notes start here

## GIGO Concept:-

- If you will give meaningless input then obviously you will get meaningless output.
- GIGO stands for Garbage in garbage out.
- In case of AI, language models don't understand like humans, they generate based on patterns.

  > Galat input ==> GALAT TOKENS => Galat Outputs

## Prompt Engineering:-

> What is Prompt ?

- Initial tokens given to gpt by user. (Hm ham question puchhte hai unko GPT ka transformer tokens mai convert karta hai)
- Agar ham 1,2,3,4,5 denge aur puchhenge ki uska agla 3 number batao wo answer mai dega 6,7,8.

  > We can not generate prompts from gpt because GPT is pretrained for not creating prompts

  - Always prompts are important.

### Type of prompts:-

- Alpaca prompt
- INST format
- Chatml

#### ALPACA Prompt:-

- The Alpaca prompt format is a specific instruction-based prompt format designed by Stanford's Alpaca model, a fine-tuned version of LLaMA.

  ##### Prompt format:-

  **Instruction**:-
  You are a calculator. Calculate sum of 2 numbers.
  Input:- 2, 5
  Output: 7

  > Based on this it creates a token which value should be 7

#### INST Prompt:-

- An INST prompt (short for "instruction prompt") is similar in spirit to prompts used for instruction-tuned models (like Alpaca) but can be adapted to your own style

  ##### Prompt format:-

  [INST] Hello [/INST]

  - These tokens enclose user messages in multi turn conversations.

  System message:-
  <<SYS>> Hi <</SYS>> :- Enclos system message

#### ChatML:-

- Use by OpenAI.

  ##### Prompt format:-

  {"role": "system", " ontent": "You are an assistant"}
  {"role": "user", "content": "What is react ?"}

  ##### Prompting technique:-

  ```python
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
  ```

### Types of Prompting:-

- Zero shot prompting
- One shot prompting
- Few shot prompting
- Chain-of-Thought (CoT) Prompting
- Self-Consistency Prompting
- Retrieval-Augmented Prompting
- Instruction Prompting
- Role-based Prompting
- Persona Prompting
- Multi-Turn Prompting (Conversation Prompting)

| Type                  | Description                       | Best For                          |
| --------------------- | --------------------------------- | --------------------------------- |
| Zero-Shot             | No examples                       | Simple tasks                      |
| One-Shot              | One example                       | Slightly unclear tasks            |
| Few-Shot              | Few examples                      | Complex tasks                     |
| Chain-of-Thought      | Step-by-step thinking             | Math, reasoning                   |
| Self-Consistency      | Multiple CoT outputs for accuracy | Logical reasoning                 |
| Retrieval-Augmented   | Uses external context             | Domain-specific or live knowledge |
| Instruction Prompting | Direct instruction                | General LLMs (like ChatGPT)       |
| Role-based Prompting  | Assign expert role                | Better tone, accuracy             |
| Persona Prompting     | Assign consistent personality     | Chatbots, tutors, agents          |
| Multi-Turn Prompting  | Contextual dialogue               | Conversations, assistants         |

#### 1. Zero shot Prompting:-

- It means asking a language model to perform a task without giving it any examples to perform a task without giving it any examples of how to do it.
- Example of code:-

  ```Python
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
  ```

#### 2. One shot Prompting:-

- Asking a language model to perform a task with giving one example.
- Example:-
  ```
  Q: Translate "Good night" to French
  A: Bonne nuit
  Q: Translate "Thank you" to French
  A:
  ```

#### 3. Few Shot Prompting:-

- Asking a language model to perform a task with giving few examples.

#### 4. Chain-of-Thought (CoT) Prompting :-

- You ask the model to think step by step before giving the final answer.
- Helpful for math, reasoning, logic-based questions.
- Example:-
  ```
  Q: If Sam has 3 apples and buys 2 more, how many does he have?
  A: Let's think step by step. Sam starts with 3 apples. He buys 2 more. 3 + 2 = 5. So the answer is 5.
  ```

#### 5. Self Consistency Prompting :-

- The model generates multiple responses and select the most constitency common answer.
- Example:- (query---research) Which is greater between 9.8 and 9.11 ?
  - Answer should be if question is mathematically then 9.8 is greater and if contextualy like book pages 9.11 is greater.

#### 6. Persona based Prompting:-

- The model is instructed to respond as if it were a particular character of profession.
