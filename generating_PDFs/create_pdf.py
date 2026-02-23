'''
This code is used to create a PDF file using the FPDF library in Python.
It initializes a PDF document, adds a page, and includes an image of a tiger on the right-hand side. 
Additionally, it adds text to the PDF before saving it as 'output.pdf'. 


This code requires the FPDF library, which can be installed using pip:
pip install fpdf


The code demonstrates how to set the font, add a cell with text, and use multi_cell for longer text that needs to wrap.

Note: Manually add texts and image to create a PDF file.

'''

from fpdf import FPDF
pdf= FPDF(orientation= 'P', unit= 'pt', format= 'A4')
pdf.add_page()
# Add image in the right hand side
pdf.image(r'generating_PDFs\tiger.jpeg', w= 80, h= 50)
# Add text, before creating the cell define the Font to avoid any error such as: 
# AttributeError: 'FPDF' object has no attribute 'unifontsubset'
# style: Bold(B), Italic(I), Underline(U)
pdf.set_font(family= 'Times', size= 24, style= 'B')
#ln: 0 - to the right, 1 - to the next line, 2 - below
#border: 0 - no border, 1 - border, L - left, T - top, R - right, B - bottom: let's you visualize as well
#align: L - left, C - center, R - right

pdf.cell(w=0, h= 50, txt= 'Malayan Tiger', align= 'C', ln= 1)

# Add sub-heading
pdf.set_font(family= 'Times', size= 14, style= 'BI')
pdf.cell(w=0, h= 15, txt= 'Description', ln=1)

# Adding a multi_line text:
pdf.set_font(family= 'Times', size= 12)
text='''The Malayan tiger is a subspecies of tiger that is native to the Malay Peninsula. 
It is one of the smallest tiger subspecies and is known for its distinctive orange coat with
black stripes. The Malayan tiger is currently listed as critically endangered due to habitat 
loss and poaching. Conservation efforts are underway to protect this majestic species and ensure 
its survival for future generations'''
pdf.multi_cell(w= 0, h= 15, txt= text, align= 'J')

#Adding subheading again to show the difference between cell and multi_cell
pdf.set_font(family= 'Times', size= 14, style= 'BI')
pdf.cell(w=100, h= 25, txt= 'Kingdom:')
pdf.set_font(family= 'Times', size= 14)
pdf.cell(w=100, h= 25, txt= 'Animalia')
pdf.output('output.pdf')
