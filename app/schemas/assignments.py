from pydantic import BaseModel
from typing import List

class AssignmentBase(BaseModel):
    student_name: str
    subject: str
    description: str
    filename: str
    comments: List[str]= []

class AssignmentCreate(AssignmentBase):
    pass

class Assignment(AssignmentBase):
    id: int

    class Config:
        orm_mode = True