from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    username: str


#用于创建的pydantic模型
class UserCreate(UserBase):
    password: str

#用于相应的用户的pydantic模型
class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True