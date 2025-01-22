#Create a fastapi app
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.types import Ask
from app.agents.agent import mentor_agent
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_item(item_id: int, q: str = None):
    return ({"item_id": item_id, "q": q})

@app.post("/ask")
def read_root(aks: Ask):
    print("**")
    question = aks.question
    mentorship_area = aks.mentorship_area

    mentor_name = "Cristhian"
    mentorship_area = "machine-learning"
    student_name = "Estefa"

    # response = route_question(mentorship_area, question)
    response  = mentor_agent(mentor_name=mentor_name, mentorship_name=mentorship_area, student_name=student_name)

    return {"response": response}
