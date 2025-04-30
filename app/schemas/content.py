from pydantic import BaseModel



class ContentBase(BaseModel):
    title: str
    description: str


class ContentCreate(ContentBase):
    pass


class Content(ContentBase):
    id: int
    owner_id: int


    class Config:
        orm_mode = True