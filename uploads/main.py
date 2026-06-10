from fastapi import FastAPI, UploadFile, File
import shutil
import os
from metric_extractor import extract_metrics

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def home():
    return {"message": "Software Quality Prediction API is running"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    metrics = extract_metrics(file_path)

    return {
        "filename": file.filename,
        "metrics": metrics
    }
