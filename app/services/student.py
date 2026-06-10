from sqlalchemy.ext.asyncio import AsyncSession
from app.models.students import Student
from sqlalchemy import select

class StudentService:

    @staticmethod
    async def register_student(db: AsyncSession, name: str, email: str):
        new_student = Student(name=name, email=email)
        db.add(new_student)
        await db.flush()
        await db.refresh(new_student)
        return new_student
    
    @staticmethod
    async def get_assignments_for_student(db: AsyncSession, student_name: str):
        result = await db.execute(select(Student).where(Student.name == student_name))
        student = result.scalars().first()
        if not student:
            return None
        return student.assignments
    
   