# 🤖 Smart Service Desk Agent — Powered by AWS Strands + Streamlit

An intelligent, code-first support assistant built using **AWS Strands** for agents. It simulates a smart service desk system where users can ask questions or check their ticket status — all through a Streamlit UI.

---

## 🚀 Features

- 💬 Chat with a smart support agent via a user-friendly Streamlit UI
- 🧠 Agent powered by **Amazon Bedrock’s Claude Nova Premier model**
- 🧩 Agent is defined entirely in code using **AWS Strands** (no console setup)
- 📚 Uses **Bedrock Knowledge Base** for document-based answers
- 🗂️ Fetches ticket status from **Amazon DynamoDB**
- 🛠️ Tools defined programmatically via `tools.py` (code-first agent actions)
- 💡 Easy to extend for other support workflows (e.g., ticket creation, escalation)

---

## 🎯 Use Case

This project demonstrates how to build a **code-first AI agent** using AWS Strands. It mimics a modern support assistant capable of:

- Answering user questions based on internal knowledge
- Looking up live ticket statuses
- Automating helpdesk-style conversations
- Running without manual configuration in AWS Console

It's ideal for learning and prototyping smart support agents with full backend integration.

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **LLM**: Amazon Bedrock – Claude Nova Premier
- **Agent Runtime**: AWS Strands (code-first Bedrock Agent)
- **Knowledge Retrieval**: Amazon Bedrock Knowledge Base
- **Data Source**: Amazon DynamoDB (ticket system)
- **Language**: Python

---

## 📁 Project Structure

smart-service-agent/
│
├── tools.py # Tools defined for knowledge base + ticket status
├── agents.py # AWS Strands agent definition and logic
├── streamlit_app.py # 🔥 Main Streamlit UI entry point
├── requirements.txt
├── Output_Screenshots #Outputs for reference of Streamlit UI and responses.
└── README.md


---

## 📦 Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/chabburi/smart-service-desk-agent.git

# 2. Navigate into the project directory
cd smart-service-agent

# 3. (Optional) Create and activate a virtual environment
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate

# 4. Install all dependencies
pip install -r requirements.txt

# 5. Run the Streamlit application
streamlit run streamlit_app.py
