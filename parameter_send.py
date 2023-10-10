from pydantic import BaseModel


class MyModel(BaseModel):
    query: str
