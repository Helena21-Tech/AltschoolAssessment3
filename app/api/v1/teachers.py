from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.teachers import TeacherCreate
from app.core.deps import get_async_db
from app.services.teacher import TeacherService

teacher_router = APIRouter()

# Register a teacher
@teacher_router.post("/", status_code=201)
async def register_teacher(data: TeacherCreate, db: AsyncSession = Depends(get_async_db)):
    new_teacher = await TeacherService.register_teacher(data.name, data.email)
    await db.commit()
    return new_teacher
