import os
import pdfkit

def convert_html_to_pdf(html_dir, pdf_dir):
    # Kreiraj izlazni direktorijum za PDF
    os.makedirs(pdf_dir, exist_ok=True)

    options = {
        "enable-local-file-access": True,  # Omogući lokalni pristup fajlovima
    }

    for root, dirs, files in os.walk(html_dir):
        for file in files:
            if file.endswith(".html"):
                input_path = os.path.join(root, file)
                relative_path = os.path.relpath(input_path, html_dir)
                output_path = os.path.join(pdf_dir, os.path.splitext(relative_path)[0] + ".pdf")

                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                pdfkit.from_file(input_path, output_path, options=options)

    print(f"PDF files generated in {pdf_dir}")

if __name__ == "__main__":
    html_dir = "."  # Putanja do HTML fajlova
    pdf_dir = "./pdf_output"  # Putanja do PDF fajlova
    convert_html_to_pdf(html_dir, pdf_dir)