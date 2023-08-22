from pydantic import BaseModel


class HelloWord(BaseModel):
    Hello: str
