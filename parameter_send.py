from pydantic import BaseModel, ValidationError, validator

class MyModel(BaseModel):
    query: str

    @validator("query", pre=True, always=True)
    def validate_query(cls, value):
        # Your validation logic here
        return value
