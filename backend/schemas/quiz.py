from pydantic import BaseModel

class QuizCreate(BaseModel):
    name: str
