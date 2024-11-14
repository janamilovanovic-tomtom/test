# .github/workflow_scripts/generate_html.py

import markdown
import os
import sys
import re

def main(src_dir, build_dir):
    os.makedirs(build_dir, exist_ok=True)

    for file in os.listdir(src_dir):
        if file.endswith('.md'):
            with open(os.path.join(src_dir, file), 'r') as infile:
                content = infile.read()

            # Convert Markdown to HTML
            html = markdown.markdown(content, extensions=['tables'])

            # Replace .md with .html in links
            html = re.sub(r'\[([^]]+)\]\(([^)]+)\.md\)', r'[\1](\2.html)', html)

            # Add CSS for table borders
            styled_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{os.path.splitext(file)[0]}</title>
    <style>
        table {{
            border-collapse: collapse;
            width: 100%;
        }}
        th, td {{
            border: 1px solid black; /* Border for table cells */
            padding: 8px; /* Padding inside cells */
            text-align: left; /* Align text to the left */
        }}
        th {{
            background-color: #f2f2f2; /* Light grey background for header */
        }}
    </style>
</head>
<body>
{html}
</body>
</html>
"""

            filename = os.path.splitext(file)[0]
            with open(os.path.join(build_dir, f'{filename}.html'), 'w') as outfile:
                outfile.write(styled_html)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: generate_html.py <src_dir> <build_dir>")
        sys.exit(1)

    src_dir = sys.argv[1]
    build_dir = sys.argv[2]
    main(src_dir, build_dir)
