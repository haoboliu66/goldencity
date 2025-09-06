#!/bin/zsh

echo "List all notes:"
curl -X GET "http://127.0.0.1:8000/notes"

echo '\n==================================================='

echo "Create a note with id 1:"
curl -X POST "http://127.0.0.1:8000/notes" \
-H "Content-Type: application/json" \
-d '{"id": 1, "title": "First Note", "content": "1st note", "timestamp": 11111}'

echo '\n==================================================='

echo "Get the note with id 1:"
curl -X GET "http://127.0.0.1:8000/notes/1"

echo '\n==================================================='

echo "Create a note with id 2:"
curl -X POST "http://127.0.0.1:8000/notes" \
-H "Content-Type: application/json" \
-d '{"id": 2, "title": "Second Note", "content": "2nd note", "timestamp": 22222}'

echo '\n==================================================='

echo "List all notes:"
curl -X GET "http://127.0.0.1:8000/notes"

echo '\n==================================================='

echo "Update note with id 1:"
curl -X PUT "http://127.0.0.1:8000/notes/1" \
-H "Content-Type: application/json" \
-d '{"id": 1, "title": "Updated Note", "content": "This note has been updated", "timestamp": 11112}'

echo '\n==================================================='

echo "Get the note with id 1:"
curl -X GET "http://127.0.0.1:8000/notes/1"

echo '\n==================================================='

echo "Delete the note with id 1:"
curl -X DELETE "http://127.0.0.1:8000/notes/1"

echo '\n==================================================='

echo "List all notes:"
curl -X GET "http://127.0.0.1:8000/notes"
