import re
import argparse
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
content = re.sub(r'!\[([^\]]*)\]\(attachments/([^?]+)(\?width=\d+)?\)', r'![\1](\2)', content)
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(content)
