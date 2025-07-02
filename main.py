# main.py
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from parser import parse_resume
import os

app = FastAPI()
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.get("/")
def read_root():
    return {"message": "Resume Parsing API is running"}

@app.post("/upload")
def upload_resume(resume: UploadFile = File(...)):
    if not resume.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported")

    file_path = os.path.join(UPLOAD_FOLDER, resume.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(resume.file.read())

    try:
        result = parse_resume(file_path)
        return JSONResponse(content=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error parsing resume: {str(e)}")
