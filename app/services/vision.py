import numpy as np
import cv2
from typing import Dict, List

def analyze_image(image_bytes: bytes, filename: str) -> Dict:
    np_arr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_GRAYSCALE)

    if img is None:
        return {"error": "Invalid image file"}

    height, width = img.shape
    orientation = "landscape" if width > height else "portrait"

    brightness = float(np.mean(img))
    threshold = 120.0

    occupied = brightness < threshold

    distance = abs(brightness - threshold)
    confidence = min(distance / threshold, 1.0)

    return {
        "filename": filename,
        "width": width,
        "height": height,
        "orientation": orientation,
        "brightness": round(brightness, 2),
        "occupied": occupied,
        "confidence": round(confidence, 2)
    }

