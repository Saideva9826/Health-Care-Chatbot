import gradio as gr
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains.retrieval_qa.base import RetrievalQA

# Load retriever and LLM
retriever = FAISS.load_local("retriever_db", OpenAIEmbeddings(), allow_dangerous_deserialization=True)
llm = ChatOpenAI(model_name="gpt-3.5-turbo")
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever.as_retriever()
)


def chat_with_bot(query):
    result = qa_chain.run(query)
    return result

# Gradio Interface
demo = gr.Interface(fn=chat_with_bot, 
                    inputs=gr.Textbox(lines=2, placeholder="Ask me anything about patient reviews..."), 
                    outputs="text",
                    title="Patient Review Chatbot")

demo.launch()
