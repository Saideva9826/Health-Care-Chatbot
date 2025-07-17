
import pandas as pd
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter

# Load the reviews CSV file
df = pd.read_csv("data/reviews.csv")  # path based on your folder layout

# Convert review column into a list of text
documents = df["review"].dropna().tolist()  # remove any NaN entries to avoid crash

# Split the reviews into smaller text chunks
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
texts = text_splitter.create_documents(documents)

# Generate embeddings
embeddings = OpenAIEmbeddings()

# Create FAISS vector store from text chunks and embeddings
vectorstore = FAISS.from_documents(texts, embeddings)

# Save the retriever locally
vectorstore.save_local("retriever_db")

print("✅ Retriever created and saved successfully!")
