import pytest
from io import BytesIO


@pytest.mark.asyncio
async def test_submit_assignment(client):
    file_data = BytesIO(b"Hello assignment file")

    response = await client.post(
        "/api/v1/assignments/",
        data={
            "student_name": "Temitope",
            "subject": "Math",
            "description": "Integration test assignment"
        },
        files={"file": ("test.txt", file_data, "text/plain")}
    )

    assert response.status_code == 201
    json_data = response.json()

    assert json_data["student_name"] == "Temitope"
    assert json_data["subject"] == "Math"
    assert "file_path" in json_data


@pytest.mark.asyncio
async def test_get_assignments(client):
    response = await client.get("/api/v1/assignments/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_add_comment(client):
    # Step 1: create assignment first
    file_data = BytesIO(b"Assignment for comment test")

    create_resp = await client.post(
        "/api/v1/assignments/",
        data={
            "student_name": "Temitope",
            "subject": "Physics",
            "description": "Test assignment"
        },
        files={"file": ("test.txt", file_data, "text/plain")}
    )

    assignment_id = create_resp.json()["id"]

    # Step 2: add comment
    response = await client.post(
        f"/api/v1/assignments/{assignment_id}/comments",
        data={
            "teacher_name": "Mr John",
            "comment": "Well done"
        }
    )

    assert response.status_code == 201
    assert response.json()["id"] == assignment_id