from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.chat_models import ChatOpenAI
from langchain.chains.retrieval_qa.base import RetrievalQA

# 1. Load retriever (memory)
retriever = FAISS.load_local("langchain_intro/retriever_db", OpenAIEmbeddings(), allow_dangerous_deserialization=True)


# 2. Load the language model (brain)
llm = ChatOpenAI(model_name="gpt-3.5-turbo")

# 3. Create QA chain (brain + memory working together)
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# 4. Chat loop
print("Ask me anything about the reviews (type 'exit' to quit):")
while True:
    query = input("You: ")
    if query.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break
    response = qa_chain.run(query)
    print("Bot:", response)
