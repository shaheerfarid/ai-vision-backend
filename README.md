# AI Vision Backend 🚀

A high-performance backend service for occupancy detection and heatmap generation. Built with **FastAPI**, **OpenCV**, and **NumPy**, this system provides a flexible foundation for computer vision tasks, prioritizing speed and clarity.

---

## 🧠 Project Philosophy

> "Progress is better than perfection."

I solved the initial problem using **simple math and pixel analysis** because it’s fast, clear, and practical. This "math-first" approach provides immediate value while establishing a robust architecture where advanced ML models can be plugged in later without breaking the system.

---

## ⚡ Key Features

- **Occupancy Analysis**: Detect occupancy in desk or zone images based on brightness and motion-like heuristics.
- **Batch Processing**: Analyze multiple images in a single request for aggregated insights.
- **Heatmap Generation**:
  - **Dynamic**: Generate heatmaps directly from a batch of images.
  - **Static**: Generate heatmaps from predefined JSON data.
- **Confidence Scoring**: Optional weighted heatmaps for smoother data visualization.
- **Local Visualization**: Includes a utility script to render and view heatmaps instantly.
- **Developer Friendly**: Fully typed with Python hints, includes automated tests, and interactive Swagger docs.

---

## 🛠 Tech Stack

- **API Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Image Processing**: [OpenCV](https://opencv.org/) & [NumPy](https://numpy.org/)
- **Visualization**: [Matplotlib](https://matplotlib.org/)
- **Server**: [Uvicorn](https://www.uvicorn.org/)

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- [Optional] Virtual environment manager (venv, conda)

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/shaheerfarid/ai-vision-backend.git
   cd ai-vision-backend
   ```

2. **Set up Virtual Environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Server

Start the development server with hot-reload enabled:

```bash
uvicorn app.main:app --reload
```

- **API Documentation**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Health Check**: [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health)

---

## 📌 API Endpoints

### 1. Single Image Analysis

`POST /analyze-image`
Analyzes a single image for brightness, orientation, and occupancy.

- **Request**: Form-data with `file` field.
- **Response**:
  ```json
  {
    "filename": "desk.jpg",
    "width": 640,
    "height": 480,
    "occupied": true,
    "confidence": 0.85
  }
  ```

### 2. Batch Analysis

`POST /analyze-batch`
Processes multiple images at once. Useful for historical data analysis.

### 3. Heatmap Generation

`POST /heatmap/batch` or `POST /heatmap/json`
Generates occupancy percentages across configured zones.

---

## 🖼 Heatmap Visualization

You can visualize the generated heatmap data locally using the provided script:

```bash
python scripts/visualize_heatmap.py
```

_This script will open a window showing a color-coded heatmap (Blue = Low, Red = High)._

---

## 🧪 Testing

We use `pytest` for automated testing. To run the test suite:

```bash
pytest
```

---

## 🗂 Project Structure

```text
.
├── app/
│   ├── api/            # Route definitions
│   ├── core/           # Configuration & Settings
│   ├── services/       # Vision & Heatmap logic
│   └── main.py         # App entry point
├── data/               # Sample data & storage
├── models/             # Future ML model storage
├── scripts/            # Utility scripts (Visualization)
├── tests/              # Unit & Integration tests
└── requirements.txt    # Project dependencies
```

---

## 💡 Roadmap

- [ ] Support for custom zone configurations via API.
- [ ] Integration of YOLO/ResNet models in `models/`.
- [ ] Real-time video stream analysis.
- [ ] Frontend dashboard for live heatmap viewing.
