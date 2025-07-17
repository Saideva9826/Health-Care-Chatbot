from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.chat_models import ChatOpenAI
from langchain.chains.retrieval_qa.base import RetrievalQA

# Load the FAISS vector store
vectorstore = FAISS.load_local(
    "retriever_db",
    OpenAIEmbeddings(),
    allow_dangerous_deserialization=True
)

# ✅ Convert vectorstore into a retriever object
retriever = vectorstore.as_retriever()

# Set up the language model
llm = ChatOpenAI(model_name="gpt-3.5-turbo")

# Create the RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever
)

# Ask a sample question
query = "What did patients say about Dr. Wallace?"
result = qa_chain.run(query)
print("Answer:", result)
