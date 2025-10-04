from fastapi import APIRouter, UploadFile, File, Form, Depends
from .parser import extract_text_from_file, parse_resume
from .models import Student
from .database import SessionLocal
import shutil, os

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/upload-resume")
async def upload_resume(
    name: str = Form(...),
    email: str = Form(...),
    location: str = Form(...),
    file: UploadFile = File(...),
    db=Depends(get_db)
):
    os.makedirs("resumes", exist_ok=True)
    file_path = f"resumes/{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text_from_file(file_path)
    parsed_data = parse_resume(text, file_path)

    parsed_data.update({"name": name, "email": email, "location": location})

    student = Student(**parsed_data)
    db.add(student)
    db.commit()
    db.refresh(student)

    return parsed_data  # Return full parsed data for frontend display