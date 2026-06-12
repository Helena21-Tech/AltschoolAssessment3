from pydantic import BaseModel
from typing import List
from app.schemas.comments import CommentRead

class AssignmentBase(BaseModel):
    student_name: str
    subject: str
    description: str
    file_path: str
    comments: List[CommentRead]= []

class AssignmentCreate(AssignmentBase):
    pass

class AssignmentRead(AssignmentBase):
    id: int

    model_config = {
        "from_attributes": True
    }