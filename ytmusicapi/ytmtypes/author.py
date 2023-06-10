from pydantic import BaseModel

class Author(BaseModel):
    name: str
    id: str