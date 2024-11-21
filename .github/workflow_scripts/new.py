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
                content = re.sub(r'\[(.*?)\]\((.+?)(\.html)([?#]?.*?)\)', r'[\1](\2.pdf\4)', content)


                filename = os.path.splitext(file)[0] + '.html'

                with open(os.path.join(output_dir, filename), 'w') as outfile:
                    outfile.write(styled_html)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)

    src_dir = sys.argv[1]
    build_dir = sys.argv[2]
    main(src_dir, build_dir)
