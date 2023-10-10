from pydantic import BaseModel, PydanticUserError, root_validator

try:
    class MyModel(BaseModel):
        query: str

        @root_validator(pre=False, skip_on_failure=True)
        @classmethod
        def _serialize(cls, x, y, z):
            return cls

except PydanticUserError as exc_info:
    assert exc_info.code == 'root-validator-pre-skip'
