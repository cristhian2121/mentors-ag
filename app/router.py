from .agents import agents

def route_question(mentorship_area, question):
    agent = agents.get(mentorship_area, agents["general"])
    return agent.run(question)
