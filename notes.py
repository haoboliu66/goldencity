from pydantic import BaseModel
from fastapi import HTTPException, APIRouter

notes_router = APIRouter()


class Note(BaseModel):
  id: int
  title: str
  content: str
  timestamp: int


notes_dict = {}  # key=id, value=Note for quick lookup


@notes_router.post("/notes")
def create_note(note: Note):
  if note.id in notes_dict:
    raise HTTPException(
        status_code=400,
        detail=f"ERROR: Note with id {note.id} already exists"
    )
  notes_dict[note.id] = note
  return {"message": "Note created", "note": note}


@notes_router.get("/notes")
def get_all_notes():
  return notes_dict.values()


@notes_router.get("/notes/{note_id}")
def get_note(note_id: int):
  validate_note_id(note_id)

  return notes_dict[note_id]


@notes_router.put("/notes/{note_id}")
def update_note(note_id: int, updated_note: Note):
  validate_note_id(note_id)

  notes_dict[note_id] = updated_note
  return {"message": "Note updated", "note": updated_note}


@notes_router.delete("/notes/{note_id}")
def delete_note(note_id: int):
  validate_note_id(note_id)

  removed_note = notes_dict.pop(note_id)
  return {"message": "Note deleted", "note": removed_note}


def validate_note_id(note_id: int):
  if note_id not in notes_dict:
    raise HTTPException(status_code=404,
                        detail=f"ERROR: Note with id {note_id} not found")
