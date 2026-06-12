from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.assignments import Assignment
from app.models.comments import Comment
from sqlalchemy import select

class AssignmentService:
    @staticmethod
    async def submit_assignment(db: AsyncSession, student_name: str, subject: str, description: str, file_path: str):
        new_assignment = Assignment(
            student_name=student_name,
            subject=subject,
            description=description,
            file_path=file_path
        )
        db.add(new_assignment)
        await db.flush()
        await db.refresh(new_assignment)
        return new_assignment
    
    @staticmethod
    async def get_submitted_assignments(db: AsyncSession, skip: int = 0, limit: int = 100):
        result = await db.execute(select(Assignment).offset(skip).limit(limit))
        return result.scalars().all()
    
    @staticmethod
    async def get_by_id(db: AsyncSession, id:int):
        result = await db.execute(select(Assignment).where(Assignment.id == id))
        return result.scalars().first()
    
    @staticmethod
    async def add_comment_to_assignment(db: AsyncSession, assignment_id: int, teacher_name: str, comment: str):
        result = await db.execute(select(Assignment).where(Assignment.id == assignment_id))
        assignment = result.scalars().first()
        if not assignment:
            raise HTTPException(status_code=404, detail="Assignment not found")
        
        new_comment = Comment(
            teacher_name=teacher_name,
            comment=comment,
            assignment_id=assignment_id
        )
        db.add(new_comment)
        await db.flush()
        await db.refresh(new_comment)
        return new_comment