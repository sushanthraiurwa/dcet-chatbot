# generate_pdf.py
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

output_path = "data/top_coaching.pdf"

# Ensure data folder exists
os.makedirs("data", exist_ok=True)

text_content = """
DCET – Karnataka Diploma CET Exam Information

Top best DCET Acamedy :
NDA Namma Diploma
TTT this is also best top two

there are many more
TGI and all
"""

# Create PDF
c = canvas.Canvas(output_path, pagesize=letter)
c.setFont("Helvetica", 10)

y = 750
for line in text_content.split("\n"):
    if y < 40:  # Start new page
        c.showPage()
        c.setFont("Helvetica", 10)
        y = 750
    c.drawString(40, y, line.strip())
    y -= 15

c.save()
print("DCET PDF created successfully at:", output_path)
