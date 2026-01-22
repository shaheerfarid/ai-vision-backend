from typing import List, Dict
import numpy as np

def generate_heatmap_from_results(results: List[dict], zones: int = 3, use_confidence: bool = False) -> Dict:
    
    heatmap = {}
    if not results:
        return heatmap

    zone_size = max(len(results) // zones, 1)

    for i in range(zones):
        zone_results = results[i * zone_size : (i + 1) * zone_size]
        if not zone_results:
            continue

        if use_confidence:
            avg_conf = np.mean([r.get("confidence", 0.0) for r in zone_results])
            heatmap[f"zone_{i + 1}"] = round(avg_conf, 2)
        else:
            occupied_count = sum(1 for r in zone_results if r.get("occupied"))
            heatmap[f"zone_{i + 1}"] = round(occupied_count / len(zone_results), 2)

    return heatmap


def generate_heatmap_from_json(data: Dict, use_confidence: bool = False) -> Dict:

    if not data:
        return {}

    if use_confidence:
        # assume values are already confidence scores
        heatmap = {zone: round(float(value), 2) for zone, value in data.items()}
    else:
        # assume values are binary occupancy
        heatmap = {zone: float(value) for zone, value in data.items()}

    return heatmap
