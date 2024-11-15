import os
import subprocess

# Pronađi punu putanju do skripte
script_to_run = os.path.join(os.getcwd(), "delete.sh")

# Prolazi kroz sve podfoldere u trenutnom folderu
for root, dirs, files in os.walk('.'):
    for dir_name in dirs:
        # Dobij putanju do podfoldera
        folder_path = os.path.join(root, dir_name)

        # Pokreni skriptu u podfolderu
        try:
            # Pokreće `delete.sh` pomoću `bash`
            result = subprocess.run(['python3', script_to_run], cwd=folder_path, check=True)
            print(f"Pokrenuta skripta u: {folder_path}")
        except subprocess.CalledProcessError as e:
            print(f"Greška pri izvršavanju skripte u: {folder_path}. Greška: {e}")
