from fastapi import APIRouter, Depends



student_router = APIRouter()

#register a student
@student_router.post("/")
def register_student():
    return {"message": "Student registered successfully"}

# View assignment for a specific student
@student_router.get("/{student_name}/assignments")
def view_assignments(student_name: str):
    return {"message": f"List of assignments for student {student_name}"}