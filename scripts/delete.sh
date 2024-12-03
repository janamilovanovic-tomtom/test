import os
import re

# Putanja do foldera sa slikama
image_folder = 'images'
# Putanja do foldera sa Markdown fajlovima
markdown_folder = '.'

# Ekstenzije slika koje će biti uzete u obzir
image_extensions = {'.png', '.jpg', '.jpeg', '.gif','svg'}

# Prikupi sve slike iz foldera sa slikama
all_images = set()
for root, dirs, files in os.walk(image_folder):
    for file in files:
        if any(file.lower().endswith(ext) for ext in image_extensions):
            all_images.add(os.path.join(root, file))

# Pronađi sve reference slika u Markdown fajlovima
referenced_images = set()
image_pattern = re.compile(r'!\[.*?\]\((.*?)\)')  # Regex za traženje slika u Markdown formatu

for root, dirs, files in os.walk(markdown_folder):
    for file in files:
        if file.endswith('.md'):
            with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                content = f.read()
                matches = image_pattern.findall(content)
                for match in matches:
                    # Prilagodi relativne putanje i dodaj ih u referenced_images
                    image_path = os.path.join(image_folder, os.path.basename(match))
                    if image_path in all_images:
                        referenced_images.add(image_path)

# Pronađi slike koje nisu referencirane
unreferenced_images = all_images - referenced_images

# Obrisati slike koje nisu referencirane
for image in unreferenced_images:
    os.remove(image)
    print(f'Obrisana slika: {image}')

print("Sve nereferencirane slike su obrisane.")

