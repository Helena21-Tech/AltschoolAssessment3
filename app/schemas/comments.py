from pydantic import BaseModel

class CommentBase(BaseModel):
    teacher_name: str
    comment: str
    assignment_id: int

class CommentCreate(CommentBase):
    pass

class CommentRead(CommentBase):
    id: int

    model_config = {
        "from_attributes": True
    }
