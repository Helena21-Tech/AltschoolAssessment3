from fastapi import FastAPI
from app.api.v1.assignments import assignment_router
from app.api.v1.teachers import teacher_router
from app.api.v1.students import student_router


app = FastAPI()
app.include_router(assignment_router, prefix="/api/v1/assignments", tags=["assignments"])
app.include_router(teacher_router, prefix="/api/v1/teachers", tags=["teachers"])
app.include_router(student_router, prefix="/api/v1/students", tags=["students"])
