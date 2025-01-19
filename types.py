from pydantic import BaseModel


class Ask(BaseModel):
    user: str
    question: str
    mentorship_area: float

