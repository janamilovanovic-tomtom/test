#!/bin/bash

# Create a new folder for PDF files
OUTPUT_DIR="pdf_output"
mkdir -p "$OUTPUT_DIR"

# Convert all .md files to PDF
for INPUT_FILE in *.md; do
    if [ -f "$INPUT_FILE" ]; then
        OUTPUT_FILE="$OUTPUT_DIR/${INPUT_FILE%.md}.pdf"
        pandoc "$INPUT_FILE" -o "$OUTPUT_FILE" --pdf-engine=wkhtmltopdf
        echo "Conversion of $INPUT_FILE completed. Output file: $OUTPUT_FILE"
    else
        echo "No .md files to convert."
    fi
done
