from fastapi import APIRouter, Depends



assignment_router = APIRouter()

# Submit an assignment
@assignment_router.post("/", status_code=201)
def submit_assignment():
    return {"message": "Assignment submitted successfully"}

# Get all submitted assignments
@assignment_router.get("/")
def get_submitted_assignments():
    return {"message": "List of submitted assignments"}

@assignment_router.post("/{id}/comments")
def add_comment_to_assignment(id: int):
    return {"message": f"Comment added to assignment {id}"}