import os
import pdfkit
import sys

def convert_html_to_pdf(html_dir, pdf_dir):
    """
    Converts HTML files to PDF files, preserving relative links in the HTML.
    """
    # Kreiraj izlazni direktorijum za PDF fajlove
    os.makedirs(pdf_dir, exist_ok=True)

    # Opcije za pdfkit
    options = {
        "enable-local-file-access": True,  # Omogući lokalni pristup fajlovima
        "no-pdf-compression": True,       # Sprečava dodatne promene PDF-a
    }

    for root, dirs, files in os.walk(html_dir):
        for file in files:
            if file.endswith(".html"):
                # Ulazna putanja do HTML fajla
                input_path = os.path.join(root, file)

                # Relativna putanja za strukturu direktorijuma
                relative_path = os.path.relpath(input_path, html_dir)

                # Izlazna putanja za PDF fajl
                output_path = os.path.join(pdf_dir, os.path.splitext(relative_path)[0] + ".pdf")

                # Kreiraj direktorijum za izlaz ako ne postoji
                os.makedirs(os.path.dirname(output_path), exist_ok=True)

                # Izmena HTML-a u memoriji pre generisanja PDF-a
                with open(input_path, 'r', encoding='utf-8') as html_file:
                    html_content = html_file.read()

                # Zameni apsolutne linkove relativnim (opcionalno, ako je potrebno)
                updated_html = html_content.replace('file:///', '')

                # Privremena datoteka za modifikovan HTML
                temp_html_path = input_path + ".temp.html"
                with open(temp_html_path, 'w', encoding='utf-8') as temp_file:
                    temp_file.write(updated_html)

                # Generiši PDF iz privremene HTML datoteke
                pdfkit.from_file(temp_html_path, output_path, options=options)

                # Ukloni privremenu datoteku
                os.remove(temp_html_path)

    print(f"PDF files generated in {pdf_dir}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <source_directory> <output_directory>")
        sys.exit(1)

    src_dir = sys.argv[1]
    build_dir = sys.argv[2]

    convert_html_to_pdf(src_dir, build_dir)
