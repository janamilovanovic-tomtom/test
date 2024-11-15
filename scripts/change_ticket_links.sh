import os
import re

# Funkcija za zamenu linkova
def replace_links_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Regularni izraz koji prepoznaje Jira linkove
    pattern = r'https://jira\.tomtomgroup\.com/browse/(GOSDK-\d+)\?src=confmacro'

    # Zamena linkova
    updated_content = re.sub(pattern, r'https://tomtom.atlassian.net/browse/\1?src=confmacro', content)

    # Upisivanje izmenjenog sadržaja u fajl
    if content != updated_content:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(updated_content)
            print(f"Zamena izvršena u fajlu: {file_path}")

# Funkcija koja rekurzivno prolazi kroz sve fajlove u direktorijumu i poddirektorijumima
def process_files_in_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                #print(file_path)
                replace_links_in_file(file_path)

# Pokretanje skripte za trenutni direktorijum
if __name__ == "__main__":
    current_directory = os.getcwd()
    process_files_in_directory(current_directory)
    print("Zamena linkova je završena.")
