# 🩺 Health Care Chatbot

A conversational AI chatbot built using **LangChain**, **OpenAI**, and **Gradio** to assist users in understanding healthcare-related feedback. It allows natural language queries over patient reviews, providing relevant, concise, and context-aware responses.

---

## 📌 Project Overview

The Health Care Chatbot leverages **Natural Language Processing (NLP)** and **Vector Search** to respond to user queries based on a dataset of patient feedback.

> 💬 “Patients said Dr. Wallace explained treatment options well.”  
> 👉 You can ask:  
> _"What did patients say about Dr. Wallace’s communication?"_  
>  
> 🧠 The chatbot will respond with a context-rich answer.

---

## 🚀 Features

- 💡 **Semantic Search with FAISS** — Contextual document retrieval using vector embeddings.
- 🤖 **Chat Interface via Gradio** — Clean UI for seamless interaction.
- 🧠 **Powered by OpenAI (GPT-3.5)** — Real-time, intelligent response generation.
- 📂 **Local CSV Parsing** — Extracts data from structured feedback datasets.
- 🔁 **Reusable Chain Logic** — Uses LangChain for modular prompt handling.

---

## 🧰 Tech Stack

| Layer         | Technology                 |
|---------------|----------------------------|
| Frontend      | Gradio                     |
| Language Model| OpenAI GPT-3.5 Turbo       |
| Backend       | Python, LangChain          |
| Vector DB     | FAISS                      |
| Data Format   | CSV                        |
| Hosting       | Local (can be deployed)    |

---

## 🛠️ How to Run Locally

1. **Clone the repository**  
```bash
git clone git@github.com:Saideva9826/Health-Care-Chatbot.git
cd Health-Care-Chatbot
Create virtual environment (recommended)

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Add your .env file

Create a .env file in the root directory and include your OpenAI API key:

ini
Copy
Edit
OPENAI_API_KEY=your_openai_api_key_here
Create the FAISS retriever

bash
Copy
Edit
python3 langchain_intro/create_retriever.py
Run the chatbot interface

bash
Copy
Edit
python3 langchain_intro/chat_ui.py
Launches at:

Open your browser and go to:

cpp
Copy
Edit
http://127.0.0.1:7860/
📊 Data Used
reviews.csv: Contains anonymized patient feedback in a column named "review".

The chatbot reads and embeds the text to power semantic Q&A.

📷 Demo Screenshot
(Add a screenshot below if available)

less
Copy
Edit
![Chatbot UI](https://your-screenshot-url.com/demo.png)
👤 Author
Saideva Goud Nathi
📫 GitHub
🔗 LinkedIn

🏁 Future Enhancements
🌐 Deploy to Hugging Face Spaces or Streamlit Cloud

📈 Integrate Sentiment Analysis and Categorization

🧾 Accept PDFs and Docx files as input

🔐 Add User Authentication for Enterprise Use

📄 License
This project is licensed under the MIT License.
Feel free to use, modify, or contribute!
