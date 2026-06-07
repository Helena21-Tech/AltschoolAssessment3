from fastapi import APIRouter, Depends



teacher_router = APIRouter()

# Register a teacher
@teacher_router.post("/")
def register_teacher():
    return {"message": "Teacher registered successfully"}

# Add a comment
@teacher_router.post("/{assignment_id}/comments")
def add_comment(assignment_id: int):
    return {"message": f"Comment added to assignment {assignment_id}"}