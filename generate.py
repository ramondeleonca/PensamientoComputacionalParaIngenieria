
import sys
import os
from PIL import Image as PILImage
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Preformatted
from reportlab.lib.styles import getSampleStyleSheet

max_width = 450  
max_height = 600 

def main():
    if len(sys.argv) != 2:
        print("Uso: python script.py <directorio_relativo>")
        sys.exit(1)

    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"Error: {directory} no es un directorio.")
        sys.exit(1)

    
    pdf_path = os.path.join(directory, f"resultado-{directory}.pdf")
    doc = SimpleDocTemplate(pdf_path, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    index = 1
    while True:
        png_fn = f"{index}.png"
        py_fn = f"{index}.py"
        png_file = os.path.join(directory, png_fn)
        py_file = os.path.join(directory, py_fn)

        
        if not os.path.exists(png_file) and not os.path.exists(py_file):
            break

        
        if os.path.exists(png_file):
            elements.append(Paragraph(f"Imagen {png_fn}", styles["Heading2"]))

            with PILImage.open(png_file) as img:
                w, h = img.size
            scale = min(max_width / w, max_height / h, 1.0)
            img_width = w * scale
            img_height = h * scale

            elements.append(Image(png_file, width=img_width, height=img_height))
            elements.append(Spacer(1, 12))

        
        if os.path.exists(py_file):
            elements.append(Paragraph(f"Código {py_fn}", styles["Heading2"]))
            with open(py_file, "r", encoding="utf-8") as f:
                code_content = f.read()
            code = code_content
            elements.append(Preformatted(code, styles["Code"], maxLineLength=80))
            elements.append(Spacer(1, 12))

        index += 1

    
    doc.build(elements)
    print(f"PDF generado en: {pdf_path}")

if __name__ == "__main__":
    main()
