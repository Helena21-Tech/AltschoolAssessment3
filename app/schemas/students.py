from pydantic import BaseModel

class StudentBase(BaseModel):
    name: str
    email: str

class StudentCreate(StudentBase):
    pass

class StudentRead(StudentBase):
    id: int

    model_config = {
        "from_attributes": True
    }