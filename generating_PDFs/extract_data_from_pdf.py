'''
PyMuPDF is a high-performance Python library for data extraction, analysis, conversion, 
and manipulation of PDF (and other documents).

This script extracts all details from the students.pdf file including:
- Document metadata
- Text content from all pages
- Images (if any)
- Links/annotations (if any)
- Page structure information
'''

import fitz  # PyMuPDF


# Open the PDF file
with fitz.open('students.pdf') as pdf:
    # extract the text and store it as a string
    #print(pdf.metadata)
    text= ''

    for page in pdf:
        #print(20*'-') # Separator for readability
        text += page.get_text()  # Extract and append text content from each page

# Print the extracted text
print(text)

