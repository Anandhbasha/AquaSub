# PdfPlumber Methos

# Exact Word

import pdfplumber

# with pdfplumber.open(r"C:\Users\Admin\Downloads\save.pdf") as pdf:
#     for page in pdf.pages:
#         words = page.extract_words()
#         for word in words:
#             if "Name" in word: 
#                 print(f"Found at: Page {page.page_number}, X: {word['x0']}, Y: {word['top']}")

#         # Alternative 
#         text = page.extract_text()
#         import re
#         if re.search(r'\bName\b', text):  
#             print(f"Found 'Name' on page {page.page_number}")

# PDF Page Dimensions
# with pdfplumber.open(r"C:\Users\Admin\Downloads\save.pdf") as pdf:
#     first_page = pdf.pages[0]
#     print(f"Page size: {first_page.width} x {first_page.height} points")
#     print(f"Page size in inches: {first_page.width/72} x {first_page.height/72} inches")


# # PyPDF2 
# # Read PDF & Extract Text
from PyPDF2 import PdfReader

reader = PdfReader('New.pdf')
for page in reader.pages:
    print(page.extract_text())

# # Length of Pages

reader = PdfReader("New.pdf")
print(len(reader.pages))

# # Merge Multiple PDFs
from PyPDF2 import PdfMerger

# pdfMerger Is Merger Tool

merger = PdfMerger() 
merger.append("New.pdf")
merger.append(r"C:\Users\Admin\Downloads\save.pdf")
merger.write("merged.pdf")
merger.close()


# #  Split PDF - Save One Page
from PyPDF2 import PdfWriter

reader = PdfReader("New.pdf")
writer = PdfWriter()
writer.add_page(reader.pages[0])

with open("page1.pdf", "wb") as f:
    writer.write(f)


# # Rotate PDF Pages

# reader = PdfReader(r"D:\AquaSub\New.pdf")
# writer = PdfWriter()

# page = reader.pages[0]
# page.rotate(90)
# writer.add_page(page)

# with open("rotated.pdf", "wb") as f:
#     writer.write(f)

# # Encryption

reader = PdfReader("New.pdf")
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

writer.encrypt("mypassword")

with open("rotated.pdf", "wb") as f:
    writer.write(f)

# # Decrypt Password

# reader = PdfReader("rotated.pdf")
# reader.decrypt("mypassword")

# for page in reader.pages:
#     print(page.extract_text())

# # Metadata 

# reader = PdfReader("page1.pdf")
# print(reader.metadata)

# # Add Blank Page or Create PDF from Scratch

# writer = PdfWriter()
# writer.add_blank_page(width=612, height=792)  # A4 size

# with open("blank.pdf", "wb") as f:
#     writer.write(f)


# # PyMuPdf
# # ReportLab
# # Text from Img
#     # pytesseract - Image text extraction(Easy Method)
#     # install pytesseract
#     #install pillow
#     # choco install tesseract
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img = Image.open(r"C:\Users\Admin\Downloads\Black And Gold Modern Birthday Party Invitation Portrait.png")
text = pytesseract.image_to_string(img)
print(text)