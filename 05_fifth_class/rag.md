# Summary of the class

- What is RAG
- Difference between RAG and fine tuning
- How RAG solve problems what is in fine tunig
- What we do in RAG ?
- How to do RAG ?
- Context window
- Types of RAG
- Indexing
- langchain

# Notes

### What is RAG ? :-

- RAG, which stands for retrieval augmented generation, is an AI technique that combines the power of information retreival with llms to enhance the accuracy and context awarness of AI generated responses.
- It works by first searching for relevant information from external data sources(like databases, documents or the web) and then using that information to guide the llm in generating a more accurate and informative response.

### Difference between RAG and fine tuning :-

| Feature              | **RAG (Retrieval-Augmented Generation)**      | **Fine-Tuning**                                   |
| -------------------- | --------------------------------------------- | ------------------------------------------------- |
| **What it does**     | Adds external knowledge at runtime            | Modifies the model’s weights permanently          |
| **How it learns**    | Doesn't learn; retrieves from documents       | Learns from new data and updates internal weights |
| **Speed**            | Fast to set up; no training needed            | Slower; needs GPU, training time                  |
| **Use Case**         | When you want up-to-date or large data access | When you want the model to deeply “remember”      |
| **Data size**        | Works well with large documents (GBs)         | Needs curated, clean, usually smaller datasets    |
| **Cost**             | Cheaper (no retraining)                       | Expensive (compute-intensive)                     |
| **Real-Time Update** | Easy – just change the documents              | Hard – requires retraining                        |

#### Analogy :-

- Fine-Tuning Analogy:

  - Like teaching a kid new facts and rewriting their brain.

  - You show the model new examples (e.g., company rules).

  - It slowly learns them over time.

  - It remembers them forever, even if the documents are deleted.

- RAG Analogy:

  - Like giving the kid a textbook or cheat sheet to answer questions.

  - You don't teach them everything.

  - Instead, they look up the info each time a question is asked.

  - The textbook can be updated anytime.
    | Scenario | Use **RAG** if... | Use **Fine-Tuning** if... |
    | ------------------------------------------------ | ----------------- | ------------------------- |
    | You want real-time answers | ✅ Yes | ❌ No |
    | You need domain-specific tone or format | ❌ Not precise | ✅ Yes |
    | You can’t retrain the model | ✅ Yes | ❌ No |
    | Your data is large (GBs of PDFs, websites) | ✅ Yes | ❌ No |
    | Your model must **learn patterns** from examples | ❌ No | ✅ Yes |

### What we do in RAG ?

- Jo relevant data hai usse prompt me dalte hai

### How to do RAG ?

- RAG uses looks simpler but it is not😁.

- #### context window :-

  - At a given point of time how many tokens can be processed.

  #### Indexing :-

  - Store data using indexing, so when user will ask later then the data should be present because when it presents in only text format then its semantic meaning will be change.
  -
