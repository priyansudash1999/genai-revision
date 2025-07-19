# Summary of the class

- Build a project weather agent which takes a city as an input and gives weather condition after api calling

- Fine tuning

## Fine tuning :-

- #### **What is fine tuning ?**

  - Fine tuning is a process of taking a pre-trained model and retraining it on a smaller task specific dataset to adapt it to a more specialized task.

    > It means teaching an already smart model some extra lessons so it become an expert in something specific.

  - **Analogy** :- If a pretrained model trained on general english. Fine tuning is train the model how to write docs in english, or essay, application in englsh...

### Techniques of fine tuning :-

- There are several methods of technique in fine tuning.
  - Full fine tuning
  - Lora
  - PEFT
  - Prompt tuning / Prefix tuning
  - Instruction tuning

#### 1. **Full fine tuning** :-

- Update all the weights of the model on your new dataset
- pros:-
  - Highly customized model
- cons:-
  - Require a lot of compute and data
- use:-
  - When we hire a large, domain-specific data set

#### 2. **LoRA - Low rank adaption** :-

- Freeze the base model and only train small adapter weights
- pros:-
  - Easy to implement
  - Easy to train
  - Cost effective
- cons:-
  - Not as good as full fine tuning

#### 3. **PEFT - Parameter efficient fine tuning** :-

- Includes method like LoR, Prefix tuning , adapter tuning
- Update only a small portion of model paramters
- Pros :-
  - Saves GPU memory andstorage
  - Great for multiple tasks
- Use:-
  - For small organizations

#### 4. **Prompt tuning :-**

- Train a sequence of prompt embeddings
- pros :-
  - fast and memory efficient
- cons :-
  - less effective for complex task
- Uses :-

  - When task is prompt sensitive

- Example:-
  - Q&A

#### 5. **Instruction training :-**

-

### Hugging face:-

- An AI community where all models, libraries, dataset and packages present of AI.
