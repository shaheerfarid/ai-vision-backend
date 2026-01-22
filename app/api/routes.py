from fastapi import APIRouter, UploadFile, File
from typing import List, Dict

from app.services.vision import analyze_image
from app.services.heatmap import generate_heatmap_from_results, generate_heatmap_from_json

router = APIRouter()


# ---------- Health Check ----------
@router.get("/health")
def health_check():
    return {"status": "ok"}


# ---------- Single Image Analysis ----------
@router.post("/analyze-image")
async def analyze_image_route(file: UploadFile = File(...)):
    image_bytes = await file.read()
    result = analyze_image(image_bytes, file.filename)
    return result


# ---------- Batch Image Analysis ----------
@router.post("/analyze-batch")
async def analyze_batch(files: List[UploadFile] = File(...)):
    results = []

    for idx, file in enumerate(files):
        image_bytes = await file.read()
        analysis = analyze_image(image_bytes, file.filename)
        analysis["id"] = idx + 1
        results.append(analysis)

    return {"count": len(results), "results": results}


# ---------- Heatmap from Batch Images ----------
@router.post("/heatmap/batch")
async def heatmap_from_batch(files: List[UploadFile] = File(...), use_confidence: bool = False):
    batch_results = []

    for file in files:
        image_bytes = await file.read()
        analysis = analyze_image(image_bytes, file.filename)
        batch_results.append(analysis)

    heatmap = generate_heatmap_from_results(batch_results, use_confidence=use_confidence)
    return {"zones": len(heatmap), "heatmap": heatmap}


# ---------- Heatmap from JSON ----------
@router.post("/heatmap/json")
def heatmap_from_json(data: Dict, use_confidence: bool = False):
    heatmap = generate_heatmap_from_json(data, use_confidence=use_confidence)
    return {"zones": len(heatmap), "heatmap": heatmap}
