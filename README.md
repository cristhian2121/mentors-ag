# **Mentorship AI Platform**

## **Overview**

This project is a centralized mentorship AI system built using **LangChain**. It provides intelligent, topic-specific agents to assist mentors and mentees across 20 different mentorship areas. The system uses a single centralized agent to route user queries to the appropriate knowledge base and provide relevant answers.

---

## **Features**

- **Centralized Routing**: Dynamically directs queries to topic-specific knowledge bases.
- **Customizable Knowledge Bases**: Each mentorship area has its curated resources for accurate and meaningful responses.
- **Scalable Design**: Easily add new mentorship topics or expand knowledge bases as needed.
- **User-Friendly API**: Facilitates seamless integration with web platforms for mentee and mentor interactions.
- **Support for 20 Mentorship Areas**: Topics include career growth, programming, leadership, mental wellness, and more.

---

## **Tech Stack**

- **Python**: Programming language for backend logic.
- **LangChain**: Framework for building conversational AI with LLMs.
- **OpenAI API**: Provides the LLM (e.g., GPT-4) for generating responses.
- **FAISS**: Vector database for storing and retrieving mentorship knowledge.
- **Flask**: Web framework for serving the centralized AI system.
- **Docker**: Containerization for deployment (optional).

---

## **Getting Started**

### **Prerequisites**

1. Python 3.8 or higher installed.
2. API keys for:
   - OpenAI (for GPT-4 or GPT-3.5 models).
3. Install the required Python libraries:
   ```bash
   pip install langchain openai faiss-cpu flask
   ```
