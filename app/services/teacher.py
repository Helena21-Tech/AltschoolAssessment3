from app.models.teachers import Teacher
from sqlalchemy.ext.asyncio import AsyncSession

class TeacherService:
    @staticmethod
    async def register_teacher(db: AsyncSession, name: str, email: str):
        new_teacher = Teacher(name=name, email=email)
        db.add(new_teacher)
        await db.flush()
        await db.refresh(new_teacher)
        return new_teacher