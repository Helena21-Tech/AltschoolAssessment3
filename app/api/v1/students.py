from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.student import StudentService
from app.schemas.students import StudentCreate
from app.core.deps import get_async_db

student_router = APIRouter()

#register a student
@student_router.post("/", status_code=201)
async def register_student(data: StudentCreate, db: AsyncSession = Depends(get_async_db)):
    new_student = await StudentService.register_student(data.name, data.email)
    await db.commit()
    return new_student
    

# View assignment for a specific student
@student_router.get("/{student_name}/assignments")
async def get_assignments_for_student(student_name: str, db: AsyncSession = Depends(get_async_db)):
    return await StudentService.get_assignments_for_student(db, student_name)

