'''
This code is used to generate multiple PDF files using data fetched from an Excel file.

The Excel in this example contains information of different animals, and for each animal, 
a PDF file is created with its name as the filename.

Each row in the Excel file corresponds to a different animal, and the code iterates through each row to 
create a PDF for that animal.

Packages used:
- pandas: for reading the Excel file and handling data in a DataFrame.
- openpyxl: for reading Excel files (used by pandas).
- fpdf: for creating PDF files.

'''

import pandas as pd
from fpdf import FPDF

df= pd.read_excel(r'generating_PDFs\animal_workbook.xlsx')

for index, row in df.iterrows():
    pdf= FPDF(orientation= 'P', unit= 'pt', format= 'A4')
    pdf.add_page()

    #add Title
    pdf.set_font(family= 'Times', size= 24, style= 'B')
    pdf.cell(w=0, h= 50, txt= row['name'], align= 'C', ln= 1)

    #slicing name column from the excel:
    for column in df.columns[1:]:
        #print(column)
        pdf.set_font(family= 'Times', size= 14, style= 'BI')
        pdf.cell(w=100, h= 25, txt= f"{column.title()}: ")

        pdf.set_font(family= 'Times', size= 14)
        pdf.cell(w=100, h= 25, txt= row[column], ln= 1)

    #output PDF
    pdf.output(f'{row["name"]}.pdf'.lower())