import pytest

@pytest.mark.asyncio
async def test_register_teacher(client):
    response = await client.post("/api/v1/teachers/", json = {"name": "Daramola", "email" : "Dara@gmail.com"})
    assert response.status_code == 201
    assert response.json()["name"] == "Daramola"
    assert response.json()["email"] == "Dara@gmail.com"