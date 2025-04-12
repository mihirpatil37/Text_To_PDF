from fpdf import FPDF
import glob
from pathlib import Path

# Create a list of text filepaths
filepaths = glob.glob("Text_Files/*.txt")
# Create one pdf file
pdf = FPDF(orientation="P", unit="mm", format="A4")

# Go to each text files
for filepath in filepaths:
    # Add a page to the PDF Document for each text files
    pdf.add_page()

    # Get the filename without the extension
    # and convert it to title case (e.g. Cat)
    filename = Path(filepath).stem
    name = filename.title()

    # Add the name to the PDF
    pdf.set_font(family="Times", style="B", size=18)
    pdf.cell(w=50, h=8, txt=name, align="L", ln=1)

    with open(filepath, "r") as file:
        content = file.read()

    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(w=0, h=6, txt=content)

# Produce the PDF
pdf.output('text_to_pdf.pdf')
