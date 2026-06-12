from fastapi import APIRouter, Depends, UploadFile, File, Form
from app.core.deps import get_async_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.assignment import AssignmentService
from app.schemas.assignments import AssignmentRead
import shutil
import os
assignment_router = APIRouter(prefix="/assignments", tags=["assignments"])

# Submit an assignment
UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

@assignment_router.post("/", response_model=AssignmentRead, status_code=201)
async def submit_assignment(student_name: str = Form(...),
    subject: str = Form(...),
    description: str = Form(...),
    file: UploadFile = File(...),db: AsyncSession = Depends(get_async_db)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
       shutil.copyfileobj(file.file, buffer)
    
    new_assignment = await AssignmentService.submit_assignment(db, student_name, subject, description, file_path)
    await db.commit()
    return new_assignment


# Get all submitted assignments
@assignment_router.get("/",response_model= list[AssignmentRead] ,status_code=200)
async def get_submitted_assignments(skip: int = 0, limit: int = 100,db: AsyncSession = Depends(get_async_db)):
    return await AssignmentService.get_submitted_assignments(db, skip, limit)


@assignment_router.post("/{id}/comments",response_model=AssignmentRead, status_code=201)
async def add_comment_to_assignment(id: int, teacher_name: str = Form(...), comment: str = Form(...), db: AsyncSession = Depends(get_async_db)):
    new_comment = await AssignmentService.add_comment_to_assignment(db, id, teacher_name, comment)
    await db.commit()
    assignment = await AssignmentService.get_by_id(db, id)
    return assignment