# Mentorship AI Platform

## Overview

This project is a centralized mentorship AI system built using **LangChain**. It provides intelligent, topic-specific agents to assist mentors and mentees across 20 different mentorship areas. The system uses a single centralized agent to route user queries to the appropriate knowledge base and provide relevant answers.

---

## Features

- **Centralized Routing**: Dynamically directs queries to topic-specific knowledge bases.
- **Customizable Knowledge Bases**: Each mentorship area has its curated resources for accurate and meaningful responses.
- **Scalable Design**: Easily add new mentorship topics or expand knowledge bases as needed.
- **User-Friendly API**: Facilitates seamless integration with web platforms for mentee and mentor interactions.
- **Support for 20 Mentorship Areas**: Topics include career growth, programming, leadership, mental wellness, and more.

---

## Tech Stack

- **Python**: Programming language for backend logic.
- **LangChain**: Framework for building conversational AI with LLMs.
- **OpenAI API**: Provides the LLM (e.g., GPT-4) for generating responses.
- **FAISS**: Vector database for storing and retrieving mentorship knowledge.
- **Flask**: Web framework for serving the centralized AI system.
- **Docker**: Containerization for deployment (optional).

### Project Structure

```plaintext
mentors-ag/
│
├── data/                       # Knowledge base files for mentorship topics
│   ├── career_growth.txt
│   ├── programming.txt
│   └── ...
│
├── app.py                      # Flask application for serving the API
├── agents.py                   # Centralized routing logic
├── chains.py                   # Retrieval chains for each topic
├── vector_store.py             # Code for embedding and storing knowledge bases
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

## Getting Started

### Prerequisites

1. Python 3.11 or higher installed.
2. API keys for:
   - OpenAI (for model).

### Run project

- **Active envrironment:** `poetry shell`
- **Run project (dev):** `poetry run fastapi dev main.py`

### Utils

- **Close environment:** `exit`
- **export to txt:** `poetry export -f requirements.txt --output requirements.txt`
