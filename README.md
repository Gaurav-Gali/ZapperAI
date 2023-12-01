# ZapperAI

I am really excited to have the opportunity to introduce you to Zapper AI!
This is an AI chatbot that interacts with your documents in order to better analyze and understand them in depth. Students can upload multiple study materials and ask relevant doubts to Zapper AI and it will answer in detail or in a way you request it to answer.
Through Zapper AI you can summarise your long and lengthy documents or study materials to save time and learn faster.

How Zapper Was Made :
This was made using Python 3.11.3, Langchain for using OpenAI's language model, FAISS(Facebook AI Similarity Search) in order to search and compare embeddings and HuggingFace for NLP(Natural Language Processing).

How Zapper Works:
It works by first analyzing your documents and converting them to raw text.
Then the raw text is broken down into chunks of length 1000 with an overlap of 200 characters in this case. The chunks are then stored in a local vector DB in the form of embeddings. The embeddings are later fed into Langchain's OpenAI language model to process and return the required result.

https://scontent.cdninstagram.com/v/t51.2885-15/381862990_293973903366336_6085095540263788887_n.jpg?stp=dst-jpg_e35&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xNDQweDEzMzcuc2RyIn0&_nc_ht=scontent.cdninstagram.com&_nc_cat=100&_nc_ohc=uB2weU6fOXsAX9fizWf&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=MzE5ODkzNzc3Njk2NzY4OTQwMA%3D%3D.2-ccb7-5&oh=00_AfDPeDrCI8-epGmEo3vF3vkY9cQKHyUP-HzI28RA9sykUA&oe=656DDFBB&_nc_sid=10d13b
