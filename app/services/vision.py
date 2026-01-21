from typing import Dict

def analyze_image_dummy(filename: str) -> Dict:
    """
    Dummy image analysis function.
    Later this will contain real computer vision logic.
    """
    return {
        "filename": filename,
        "occupied": False,
        "confidence": 0.75,
        "note": "Dummy vision result"
    }
