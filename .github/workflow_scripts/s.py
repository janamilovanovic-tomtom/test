import os
import re
import subprocess
from pathlib import Path

def convert_md_to_pdf(src_dir, output_dir):
    # Kreiraj output direktorijum
    os.makedirs(output_dir, exist_ok=True)

    # Iteracija kroz sve fajlove i foldere u src_dir
    for root, dirs, files in os.walk(src_dir):
        # Mapiranje trenutnog direktorijuma na output strukturu
        relative_path = os.path.relpath(root, src_dir)
        current_output_dir = os.path.join(output_dir, relative_path)
        os.makedirs(current_output_dir, exist_ok=True)

        for file in files:
            if file.endswith(".md"):
                src_file = os.path.join(root, file)
                output_file = os.path.join(current_output_dir, file.replace(".md", ".pdf"))

                # Čitanje sadržaja Markdown fajla
                with open(src_file, "r", encoding="utf-8") as f:
                    content = f.read()

                # Zamenjivanje .md linkova sa .pdf u sadržaju
                updated_content = re.sub(r'\((.*?\.md)\)', lambda m: f"({m.group(1).replace('.md', '.pdf')})", content)

                # Privremeni fajl za ažurirani sadržaj
                temp_md_file = os.path.join(current_output_dir, file)
                with open(temp_md_file, "w", encoding="utf-8") as temp_f:
                    temp_f.write(updated_content)

                # Konvertovanje u PDF pomoću pandoc
                try:
                    subprocess.run(
                        ["pandoc", temp_md_file, "-o", output_file],
                        check=True
                    )
                    print(f"Generated PDF: {output_file}")
                except subprocess.CalledProcessError as e:
                    print(f"Error converting {src_file} to PDF: {e}")

                # Brisanje privremenog Markdown fajla
                os.remove(temp_md_file)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python script.py <src_dir> <output_dir>")
        sys.exit(1)

    src_dir = sys.argv[1]
    output_dir = sys.argv[2]
    convert_md_to_pdf(src_dir, output_dir)
