from langchain_community.chat_models import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langchain_community.agent_toolkits.load_tools import load_tools
from app.settings import settings
from app.agents.tools.mentor_tool import mentor_introduction_tool




def mentor_agent(mentor_name: str, mentorship_name: str, student_name: str):
    llm = ChatOpenAI(model=settings.AI_MODEL, api_key=settings.OPENAI_API_KEY)
    tools = load_tools([mentor_introduction_tool], llm=llm)
    agent = create_react_agent(llm, tools)

    print("******")

    messages = agent.invoke(
        {"message": [
            ("human", f"mentorship of {mentor_name} about {mentorship_name} to {student_name}")
            ]}
        )

    print("***", messages)

    return messages