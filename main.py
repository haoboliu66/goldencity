from fastapi import FastAPI

app = FastAPI()
app.include_router(notes_router)

@app.get("/")
def index():
  return {"Hello, welcome"}