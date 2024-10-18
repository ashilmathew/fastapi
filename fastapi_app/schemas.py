from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str
    is_admin: bool = False  # Default to False

class PostBase(BaseModel):
    title: str
    content: str

class CommentBase(BaseModel):
    content: str

class ChangePassword(BaseModel):
    current_password: str
    new_password: str
