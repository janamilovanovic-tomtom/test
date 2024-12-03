from bs4 import BeautifulSoup
import re
import markdownify
import argparse

def convert_html_table_to_md(html_table):
    soup = BeautifulSoup(html_table, 'html.parser')
    rows = []
    for tr in soup.find_all('tr'):
        tds = tr.find_all(['th', 'td'])
        if not tds:  # Skip empty rows
            continue
        row_data = []
        for td in tds:
            content = markdownify.markdownify(td.decode_contents(), heading_style="ATX")
            cleaned_content = content.replace('\n', '').strip()
            row_data.append(cleaned_content)
        rows.append(row_data)
    if not rows:
        return ""
    header_row = [rows[0][i] for i in range(len(rows[0]))]
    markdown_table = "| " + " | ".join(header_row) + " |\n"
    markdown_table += "|---" + "|---" * (len(header_row) - 1) + "|\n"
    for row in rows[1:]:
        markdown_table += "| " + " | ".join(row) + " |\n"
    markdown_table = re.sub(r'\n\s*\n', '\n', markdown_table)  # Remove multiple newlines
    markdown_table = markdown_table.strip()  # Trim leading/trailing whitespace
    return markdown_table

# Konfiguracija argparse-a za unos argumenta iz komandne linije
parser = argparse.ArgumentParser(description="Convert HTML tables in a Markdown file to Markdown table format.")
parser.add_argument("input_file", help="Path to the input Markdown file with HTML tables.")
parser.add_argument("output_file", help="Path to save the output Markdown file with converted tables.")

# Parsiranje argumenata
args = parser.parse_args()
input_file = args.input_file
output_file = args.output_file


with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()
soup = BeautifulSoup(content, 'html.parser')
for table in soup.find_all('table'):
    html_table = str(table)
    markdown_table = convert_html_table_to_md(html_table)
    table.replace_with(markdown_table)
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(str(soup))
print(f"Converted tables to Markdown format in '{output_file}'.")