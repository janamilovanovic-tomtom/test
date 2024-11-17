import os
import re

def update_links_to_pdf(folder):
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith('.md') and file.lower() != 'readme.md':
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Replace .md links with .pdf
                updated_content = re.sub(r'\(([^)]+)\.md\)', r'(\1.pdf)', content)

                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                print(f'Updated links in: {filepath}')

if __name__ == "__main__":
    # Call the function to update links
    update_links_to_pdf('./')
