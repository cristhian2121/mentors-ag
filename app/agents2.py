from langchain.agents import initialize_agent, Tool
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from .vector_store import vector_stores
from .settings import settings

# Initialize the LLM
llm = OpenAI(model=settings.AI_MODEL, api_key=settings.OPENAI_API_KEY)

# Define agents for each mentorship area
agents = {}
for area, vector_store in vector_stores.items():
    tools = [
        Tool(
            name=f"{area} Mentor",
            func=RetrievalQA.from_chain_type(llm=llm, retriever=vector_store.as_retriever()).run,
            description=f"Answers questions related to {area}."
        ),
    ]
    agents[area] = initialize_agent(tools, llm)
