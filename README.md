# ZapperAI

I am really excited to have the opportunity to introduce you to Zapper AI!
This is an AI chatbot that interacts with your documents in order to better analyze and understand them in depth. Students can upload multiple study materials and ask relevant doubts to Zapper AI and it will answer in detail or in a way you request it to answer.
Through Zapper AI you can summarise your long and lengthy documents or study materials to save time and learn faster.

**How Zapper Was Made :**
This was made using Python 3.11.3, Langchain for using OpenAI's language model, FAISS(Facebook AI Similarity Search) in order to search and compare embeddings and HuggingFace for NLP(Natural Language Processing).

**How Zapper Works:**
It works by first analyzing your documents and converting them to raw text.
Then the raw text is broken down into chunks of length 1000 with an overlap of 200 characters in this case. The chunks are then stored in a local vector DB in the form of embeddings. The embeddings are later fed into Langchain's OpenAI language model to process and return the required result.
