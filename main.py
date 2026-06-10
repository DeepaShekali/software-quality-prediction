from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import shutil
import os
import joblib

from metric_extractor import extract_metrics
from pdf_generator import generate_pdf

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
REPORT_DIR = "reports"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)

# LOAD ML MODEL
model = joblib.load("quality_model.pkl")


@app.get("/")
def home():
    return {"message": "ML Software Quality Prediction API Running"}


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # EXTRACT METRICS
    metrics = extract_metrics(file_path)

    X = [[
        metrics["loc"],
        metrics["complexity"],
        metrics["coupling"]
    ]]

    # ML PREDICTION
    prediction = model.predict(X)[0]
    probability = model.predict_proba(X)[0][prediction]

    label = "Defective" if prediction == 1 else "Clean"
    confidence = round(float(probability) * 100, 2)

    result = {
        "filename": file.filename,
        "metrics": metrics,
        "prediction": label,
        "confidence": confidence
    }

    # PDF REPORT
    pdf_path = os.path.join(REPORT_DIR, file.filename + ".pdf")
    generate_pdf(result, pdf_path)

    result["pdf_report"] = f"/download/{file.filename}"

    return result


@app.get("/download/{filename}")
def download_pdf(filename: str):
    return FileResponse(
        f"reports/{filename}.pdf",
        media_type="application/pdf",
        filename=f"{filename}.pdf"
    )