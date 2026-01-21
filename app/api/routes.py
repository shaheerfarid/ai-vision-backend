from fastapi import APIRouter
from app.services.vision import analyze_image_dummy


router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "ok"}

from fastapi import UploadFile, File
from app.services.vision import analyze_image_dummy

@router.post("/analyze-image")
async def analyze_image(file: UploadFile = File(...)):
    result = analyze_image_dummy(file.filename)
    return result

