from pydantic import BaseModel


class TeacherBase(BaseModel):
    name: str
    email: str

class TeacherCreate(TeacherBase):
    pass

class TeacherRead(TeacherBase):
    id: int

    model_config = {
        "from_attributes": True
    }