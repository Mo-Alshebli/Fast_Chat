from pydantic import BaseModel, ValidationError, validator

from pydantic import BaseModel, model_validator
from pydantic.error_wrappers import PydanticError

try:

    class MyModel(BaseModel):
        query: str
        @validator("query", pre=True, always=True)
        @model_validator(pre=False, skip_on_failure=True)
        @classmethod
        def _serialize(cls, x, y, z):
            return cls

except PydanticError as exc_info:
    assert exc_info.code == 'model-validator-instance-method'

