import os
import subprocess
import re
import os
def list_md_files_in_root():
    md_files = [file for file in os.listdir(".") if file.endswith('.md') and os.path.isfile(file)]
    return md_files


md_files = list_md_files_in_root()

for md_file in md_files:
    match = re.match(r'^(.*)\.md$', md_file)
    name_part = match.group(1)
    subprocess.run(['python3', 'scripts/convert_html_tables_to_md.sh', md_file, str(name_part)+"___.md"])
    subprocess.run(['python3', 'scripts/change_images_path.sh',  str(name_part)+"___.md",  str(name_part)+"___.md"])
    os.remove(md_file)
