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


def validate_note_id(note_id: int):
  if note_id not in notes_dict:
    raise HTTPException(status_code=404,
                        detail=f"ERROR: Note with id {note_id} not found")
