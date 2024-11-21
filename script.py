import markdown
import os
import sys
import re
import pdfkit

def convert_md_to_pdf(src_dir, build_dir):
    """
    Converts Markdown files in a directory to PDF files.

    Args:
        src_dir (str): Path to the source directory containing .md files.
        build_dir (str): Path to the output directory for .pdf files.
    """
    os.makedirs(build_dir, exist_ok=True)

    options = {
        "enable-local-file-access": True,
        "quiet": ""
    }

    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith('.md'):
                relative_path = os.path.relpath(root, src_dir)
                output_dir = os.path.join(build_dir, relative_path)
                os.makedirs(output_dir, exist_ok=True)

                with open(os.path.join(root, file), 'r') as infile:
                    content = infile.read()

                # Convert Markdown links from .md to .pdf
                content = re.sub(r'\[(.*?)\]\((.+?)(\.md)([?#]?.*?)\)', r'[\1](\2.pdf\4)', content)

                # Convert Markdown to HTML
                html_content = markdown.markdown(content, extensions=['tables'])

                # Add basic HTML styling for the output
                styled_html = f"""
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>{os.path.splitext(file)[0]}</title>
                    <style>
                        body {{
                            font-family: Arial, sans-serif;
                            line-height: 1.6;
                            margin: 20px;
                        }}
                        table {{
                            border-collapse: collapse;
                            width: 100%;
                        }}
                        th, td {{
                            border: 1px solid black;
                            padding: 8px;
                            text-align: left;
                        }}
                        th {{
                            background-color: #f2f2f2;
                        }}
                    </style>
                </head>
                <body>
                {html_content}
                </body>
                </html>
                """

                # Generate the output PDF path
                pdf_filename = os.path.splitext(file)[0] + '.pdf'
                pdf_path = os.path.join(output_dir, pdf_filename)

                # Convert the styled HTML to PDF
                try:
                    pdfkit.from_string(styled_html, pdf_path, options=options)
                    print(f"Generated PDF: {pdf_path}")
                except Exception as e:
                    print(f"Error generating PDF for {file}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <src_dir> <build_dir>")
        sys.exit(1)

    src_dir = sys.argv[1]
    build_dir = sys.argv[2]
    convert_md_to_pdf(src_dir, build_dir)
