# .github/workflow_scripts/generate_html.py

import markdown
import os
import sys

def main(src_dir, build_dir):
    os.makedirs(build_dir, exist_ok=True)

    for file in os.listdir(src_dir):
        if file.endswith('.md'):
            with open(os.path.join(src_dir, file), 'r') as infile:
                content = infile.read()
            html = markdown.markdown(content)
            filename = os.path.splitext(file)[0]
            with open(os.path.join(build_dir, f'{filename}.html'), 'w') as outfile:
                outfile.write(html)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: generate_html.py <src_dir> <build_dir>")
        sys.exit(1)

    src_dir = sys.argv[1]
    build_dir = sys.argv[2]
    main(src_dir, build_dir)
