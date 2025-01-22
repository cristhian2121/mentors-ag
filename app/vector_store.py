from langchain.document_loaders import TextLoader
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
import os

from openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langchain_community.tools import load_tools
from .settings import settings

# Path to knowledge base files
DATA_PATH = "./data"

# Initialize vector stores for each mentorship area
# vector_stores = {}
# embeddings = OpenAIEmbeddings(api_key=settings.OPENAI_API_KEY, model=settings.AI_MODEL)

# for file in os.listdir(DATA_PATH):
#     if file.endswith(".txt"):
#         area = file.replace(".txt", "")
#         loader = TextLoader(os.path.join(DATA_PATH, file))
#         docs = loader.load()
#         vector_stores[area] = FAISS.from_documents(docs, embeddings)
