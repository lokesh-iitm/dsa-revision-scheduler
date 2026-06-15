from pydantic import BaseModel


class Problem(BaseModel):
    title: str
    topic: str
    difficulty: str