'''
PyMuPDF is a high-performance Python library for data extraction, analysis, conversion, 
and manipulation of PDF (and other documents).

This script extracts all details from the students.pdf file including:
- Document metadata
- Text content from all pages

To extract tables from a PDF file, we are using tabula-py library, which can read tables 
from PDF file and convert them into a pandas DataFrame or CSV file, TSV file, JSON file, or Excel file.

'''

import fitz  # PyMuPDF to extract text and metadata from PDF files
import json
import subprocess
import pandas as pd
import os

# Open the PDF file: Create a function to extract data from the PDF file

def extract_pdf_data(pdf_path):
    with fitz.open(pdf_path) as pdf:
        # Extract document metadata
        metadata = pdf.metadata
        print("Document Metadata:")
        for key, value in metadata.items():
            print(f"{key}: {value}")
        print("\n" + "="*50 + "\n") # Separator for readability

        # Extract text content from all pages
        text = ''
        for page in pdf:
            text += page.get_text()  # Extract and append text content from each page

        return text
'''
Issue faced:
tabula.read_pdf() 
    → tries to import jpype (for direct Java integration)
    → jpype crashes on import (missing Visual C++ redistributables)
    → falls back to subprocess to run Java
    → subprocess also has issues in your venv
    → Python script terminates silently

Solution:
Instead of relying on tabula.read_pdf()'s internal machinery, I bypass it entirely and call the Tabula Java jar directly using Python's subprocess module.
Step 1: Locate the Tabula Java Jar file using tabula.backend.jar_path()
    I. This is the actual engine that extracts tables from PDFs
    II. We get its path directly (works because importing tabula.backend doesn't trigger JPype)
Step 2: Build the Java command to run the jar with appropriate arguments (like page number and output format)
    example: java -jar tabula-1.0.5-jar-with-dependencies.jar -p 1 -f JSON weather.pdf
Step 3: Use subprocess.run() to execute the command and capture the output
    I. If there's an error, print it out
    II. If successful, parse the JSON output to extract table data
Step 4: Parse the JSON output
    tables_data = json.loads(result.stdout)
Step 5: Convert the extracted table data into pandas DataFrames for easier manipulation and display

'''

def read_pdf_table(pdf_path, page_number=1):
    """
    Extract tables from PDF using tabula Java jar directly via subprocess.
    This works around JPype/subprocess issues in virtual environments on Windows.
    """
    # Find the tabula jar file
    import tabula.backend
    jar_path = tabula.backend.jar_path()
    
    # Build the Java command
    cmd = [
        'java', '-jar', jar_path,
        '-p', str(page_number),
        '-f', 'JSON',
        pdf_path
    ]
    
    # Run the command
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return None
    
    # Parse the JSON output
    tables_data = json.loads(result.stdout)
    
    # Convert to pandas DataFrames
    '''
    Scenario:
    ┌─────────────────────────────────────────────────────────────────────┐
│  JSON from Tabula (tables_data)                                     │
│  [{                                                                 │
│    "data": [                                                        │
│      [{"text":"Year"}, {"text":"Month"}],      ← Header cells       │
│      [{"text":"2013"}, {"text":"1"}],          ← Data row 1         │
│      [{"text":"2013"}, {"text":"1"}]           ← Data row 2         │
│    ]                                                                │
│  }]                                                                 │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│  Extract text from cells (list comprehension)                       │
│                                                                     │
│  rows = [                                                           │
│    ["Year", "Month"],                    ← rows[0] (header)         │
│    ["2013", "1"],                        ← rows[1] (data)           │
│    ["2013", "1"]                         ← rows[2] (data)           │
│  ]                                                                  │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│  Create DataFrame                                                   │
│                                                                     │
│  pd.DataFrame(rows[1:], columns=rows[0])                            │
│                                                                     │
│       Year  Month                                                   │
│  0   2013      1                                                    │
│  1   2013      1                                                    │
└─────────────────────────────────────────────────────────────────────┘
    '''
    dataframes = []
    for table in tables_data:
        # Extract data from the table structure
        rows = []
        for row in table.get('data', []):
            row_data = [cell.get('text', '') for cell in row]
            rows.append(row_data)
        
        if rows:
            # First row as header
            df = pd.DataFrame(rows[1:], columns=rows[0])
            dataframes.append(df)
    
    return dataframes


# Example usage:
pdf_path = r'generating_PDFs\weather.pdf'
tables = read_pdf_table(pdf_path, page_number=1)
print(type(tables))
if tables:
    print("Extracted tables:")
    for i, table in enumerate(tables):
        print(f"\n--- Table {i+1} ---")
        print(table)
    table.to_csv(f'table_{i+1}.csv', index=False)  # Save each table as a CSV file
else:
    print("No tables found.")
