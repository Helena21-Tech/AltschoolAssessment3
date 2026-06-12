import pytest
from io import BytesIO

@pytest.mark.asyncio
async def test_register_student(client):
    response = await client.post("/api/v1/students/", json = {"name": "Temitope", "email" : "Temi@gmail.com"})
    assert response.status_code == 201
    assert response.json()["name"] == "Temitope"
    assert response.json()["email"] == "Temi@gmail.com"



import pytest


@pytest.mark.asyncio
async def test_get_assignments_for_student(client):
    file_data = BytesIO(b"Student assignment content")

    await client.post(
        "/api/v1/assignments/",
        data={
            "student_name": "Temitope",
            "subject": "Math",
            "description": "Integration test assignment"
        },
        files={"file": ("test.txt", file_data, "text/plain")}
    )
    response = await client.get(
        "/api/v1/students/Temitope/assignments"
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1
    assert data[0]["student_name"] == "Temitope"
    assert "subject" in data[0]
    assert "description" in data[0]
    assert "file_path" in data[0]