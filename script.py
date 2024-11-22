import fitz  # PyMuPDF

# Otvorite PDF fajl
doc = fitz.open("a.pdf")

# Prolazak kroz sve stranice u PDF-u
for page_num in range(len(doc)):
    page = doc.load_page(page_num)

    # Pronađite sve linkove na stranici
    links = page.get_links()

    # Prolazak kroz sve linkove i zamena URL-ova
    for link in links:
        print("1")
        print(link)
        if 'file' in link:
            print("2")
            uri = link['file']
            # Proverite da li link počinje sa file:///home/runner/work/test/test/
            if uri.startswith("/home/runner/work/test/test/"):
                print("yes")
                # Zamenite ga sa ./ (relativni link)
                new_uri = uri.replace("/home/runner/work/test/test/", "./")
                # Modifikujte link direktno
                link['file'] = new_uri

                # Ponovo postavite link sa novim uri

                print(link)
                page.update_link(link)

# Sačuvajte izmenjeni PDF
doc.save("a1.pdf")
