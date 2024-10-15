#!/bin/bash

# Proverite da li je datoteka prosleđena kao argument
if [ "$#" -ne 1 ]; then
    echo "Upotreba: $0 putanja/do/fajla.md"
    exit 1
fi

# Putanja do Markdown fajla
FILE="$1"

# Kreirajte privremeni fajl
TEMP_FILE="$(mktemp)"

# Obrada fajla
awk '
    {
        # Proverite da li red sadrži "Reviewed by"
        if ($0 ~ /^\| \*\*Reviewed by\*\*/) {
            next;  # Preskočite ovaj red
        }
        print $0;  # Štampajte ostale redove
    }
' "$FILE" > "$TEMP_FILE"

# Zamenite originalni fajl
mv "$TEMP_FILE" "$FILE"

echo "Redovi sa 'Reviewed by' su obrisani."
