from pydantic import BaseModel


class UserBase(BaseModel):
    name: str


# Request
class UserCreate(UserBase):
    password: str

    
# Response
class UserRead(UserBase):
    id: int
    is_admin: bool

    class Config:
        from_attributes = True
