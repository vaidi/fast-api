from datetime import datetime

from pydantic import BaseModel

class Student(BaseModel):
    id: int
    name: str
    age: int
    gender: str
    time: datetime


# 正确：提供所有字段的值
student = Student(
    id=1,
    name="Alice",
    age=20,
    gender="female",
    time=datetime.now()
)
print(student.dict())