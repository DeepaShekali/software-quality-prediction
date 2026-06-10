from reportlab.pdfgen import canvas

def generate_pdf(data, filename):
    c = canvas.Canvas(filename)

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 800, "Software Quality Prediction Report")

    c.setFont("Helvetica", 12)

    y = 750

    for key, value in data.items():
        c.drawString(50, y, f"{key}: {value}")
        y -= 25

    c.save()
