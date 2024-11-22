import os
import PyPDF2
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def update_pdf_links(input_pdf_path, output_pdf_path):
    with open(input_pdf_path, 'rb') as input_file:
        reader = PyPDF2.PdfReader(input_file)

        # Create a new PDF to write the modified content
        c = canvas.Canvas(output_pdf_path, pagesize=letter)

        for page in reader.pages:
            page_content = page.extract_text()
            if page_content:
                # Replace links from '.md' to '.pdf'
                modified_content = page_content.replace('.md', '.pdf')

                # Write the modified content to the new PDF
                # This assumes a simple one-line layout; adjust as necessary
                c.drawString(100, 750, modified_content)  # Adjust the position as needed
                c.showPage()  # End the current page and start a new one

        # Save the new PDF
        c.save()

# Example usage
def main():
    pdf_files = ['a.pdf', 'b.pdf']  # List your PDF files
    for pdf_file in pdf_files:
        update_pdf_links(pdf_file, f'updated_{pdf_file}')

if __name__ == "__main__":
    main()
