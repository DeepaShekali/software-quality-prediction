from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf(data, output_path):
    c = canvas.Canvas(output_path, pagesize=letter)
    c.setFont("Helvetica", 12)

    c.drawString(50, 750, "Software Quality Prediction Report")

    c.drawString(50, 700, f"Filename: {data['filename']}")
    c.drawString(50, 680, f"LOC: {data['metrics']['loc']}")
    c.drawString(50, 660, f"Complexity: {data['metrics']['complexity']}")
    c.drawString(50, 640, f"Coupling: {data['metrics']['coupling']}")

    c.drawString(50, 600, f"Risk Score: {data['risk_score']}")
    c.drawString(50, 580, f"Prediction: {data['prediction']}")

    c.save()