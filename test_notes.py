# test_notes.py
import pytest
from fastapi.testclient import TestClient
from notes import router, Note
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)

client = TestClient(app)

def test_create_note():
    response = client.post("/notes", json={
        "id": 1,
        "title": "Test Note 1st",
        "content": "This is a test note",
        "timestamp": 11111111
    })
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Note created"
    assert data["note"]["id"] == 1

def test_get_all_notes():
    response = client.get("/notes")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1

def test_get_note_success():
    response = client.get("/notes/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1

def test_get_note_not_found():
    response = client.get("/notes/100")
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]

def test_update_note_success():
    response = client.put("/notes/1", json={
        "id": 1,
        "title": "Updated Note",
        "content": "Updated content",
        "timestamp": 111111112
    })
    assert response.status_code == 200
    data = response.json()
    assert data["note"]["title"] == "Updated Note"

def test_delete_note_success():
    response = client.delete("/notes/1")
    assert response.status_code == 200
    data = response.json()
    assert data["note"]["id"] == 1

def test_delete_note_not_found():
    response = client.delete("/notes/100")
    assert response.status_code == 404
