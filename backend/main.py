from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
from backend.recognition.match_snippet import match_snippet

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/match")
async def match_audio(file: UploadFile = File(...)):
    temp_path = f"temp_audio/{file.filename}"
    os.makedirs("temp_audio", exist_ok=True)

    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = match_snippet(temp_path)
    print(result)
    os.remove(temp_path)

    return {"result": result}