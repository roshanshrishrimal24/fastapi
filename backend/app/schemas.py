from pydantic import BaseModel

# Example Pydantic schemas

class User(BaseModel):
    id: int
    name: str
    email: str

class Item(BaseModel):
    id: int
    title: str
    description: str
    owner_id: int