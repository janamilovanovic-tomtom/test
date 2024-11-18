import markdown
import os
import sys
import re

def main(src_dir, build_dir):
    os.makedirs(build_dir, exist_ok=True)

    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith('.md'):
                relative_path = os.path.relpath(root, src_dir)
                output_dir = os.path.join(build_dir, relative_path)
                os.makedirs(output_dir, exist_ok=True)
                with open(os.path.join(root, file), 'r') as infile:
                    content = infile.read()
                content = re.sub(r'\[(.*?)\]\((.+?)(\.md)([?#]?.*?)\)', r'[\1](\2.html\4)', content)

                html = markdown.markdown(content, extensions=['tables'])

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
                {html}
                </body>
                </html>
                """

                filename = os.path.splitext(file)[0] + '.html'
                with open(os.path.join(output_dir, filename), 'w') as outfile:
                    outfile.write(styled_html)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)

    src_dir = sys.argv[1]
    build_dir = sys.argv[2]
    main(src_dir, build_dir)
