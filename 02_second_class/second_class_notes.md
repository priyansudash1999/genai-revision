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
