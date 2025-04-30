from datetime import datetime

from pydantic import BaseModel


class Item(BaseModel):
    title: str
    timestamp: datetime
    description: str



