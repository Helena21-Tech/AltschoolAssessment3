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

class AssignmentRead(AssignmentBase):
    id: int

    model_config = {
        "from_attributes": True
    }