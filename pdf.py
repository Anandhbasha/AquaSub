# import PyPDF2

# PyPDF2 is a Python library used to read, split, merge, and extract text from PDFs.
# But note: PyPDF2 is not good for exact layout-based text extraction (like tables).

# Read page count

# Extract plain text

# Merge multiple PDFs

# Split PDF pages

# Read and Extract Text from PDF
# # PDF file open panrom
# with open("Anandhakumar M_Developer.pdf", "rb") as file:
#     reader = PyPDF2.PdfReader(file)

#     # Total pages count
#     print("Total Pages:", len(reader.pages))

#     # First page text
#     page = reader.pages[0]
#     print(page.extract_text())


# # Split PDF (first page only)

# from PyPDF2 import PdfReader, PdfWriter

# reader = PdfReader("Anandhakumar M_Developer.pdf")
# writer = PdfWriter()

# # Only first page save panrom
# writer.add_page(reader.pages[0])

# with open("first_page.pdf", "wb") as output:
#     writer.write(output)

# import pdfplumber

# with pdfplumber.open("Anandhakumar M_Developer.pdf") as pdf:
#     page = pdf.pages[0]
#     print(page.extract_text())  # Layout kooda retain pannum


# for single page
# import pdfplumber


# with pdfplumber.open("Deepa.pdf") as pdf:
#     first_page = pdf.pages[0]

#     # Table extract pannrom
#     table = first_page.extract_table()

#     for row in table:
#         print(row)
# # For multiple Pages
# import pdfplumber

# with pdfplumber.open("Deepa.pdf") as pdf:
#     for page_number, page in enumerate(pdf.pages):
#         print(f"\n--- Page {page_number + 1} ---")
#         table = page.extract_table()

#         if table:
#             for row in table:
#                 print(row)
#         else:
#             print("No table found on this page.")

# # import pdfplumber

# with pdfplumber.open("Deepa.pdf") as pdf:
# #     page = pdf.pages[0]

# #     # Define bbox = [x0, top, x1, bottom] in points (1 inch = 72 points)
# #     # Example: top-left 100,100 to bottom-right 400,200
# #     area = (100, 100, 400, 200)

# #     # Area crop panrom
# #     cropped = page.within_bbox(area)

# #     # Extract text only from that area
# #     text = cropped.extract_text()
# #     print("Cropped Area Text:\n", text)


# import pdfplumber

# word_to_find = "Deepa"  # word you want to filter/search

# with pdfplumber.open("Deepa.pdf") as pdf:
#     for page_number, page in enumerate(pdf.pages, start=1):
#         text = page.extract_text()
#         if text and word_to_find in text:
#             print(f"Word '{word_to_find}' found on page {page_number}")
#             # If you want, print the line containing the word
#             for line in text.split('\n'):
#                 if word_to_find in line:
#                     print(">>", line)


# import pdfplumber
# import warnings

# warnings.filterwarnings("ignore", message="CropBox missing from /Page")

# word_to_find = "deepa"  # lowercase for safer search

# with pdfplumber.open("Deepa.pdf") as pdf:
#     found = False
#     for page_number, page in enumerate(pdf.pages, start=1):
#         text = page.extract_text()
#         if text:
#             # lowercase check to make case-insensitive search
#             if word_to_find.lower() in text.lower():
#                 print(f" Word '{word_to_find}' found on page {page_number}")
#                 for line in text.split('\n'):
#                     if word_to_find.lower() in line.lower():
#                         print(">>", line)
#                 found = True

#     if not found:
#         print(f" Word '{word_to_find}' not found in the PDF.")


# import pdfplumber
# import warnings
# import re

# warnings.filterwarnings("ignore", message="CropBox missing from /Page")

# word_to_find = "Deepa"  # we want to match this (case doesn't matter)
# found_word = None

# with pdfplumber.open("Deepa.pdf") as pdf:
#     for page_number, page in enumerate(pdf.pages, start=1):
#         text = page.extract_text()
#         if text:
#             # Case-insensitive match
#             matches = re.findall(r'\bdeepa\b', text, re.IGNORECASE)
#             if matches:
#                 print(f" Word matching '{word_to_find}' found on page {page_number}")
#                 print(">> Matches:", matches)
#                 # Store the *exact word* as it appears in PDF (like DEEPA or Deepa)
#                 found_word = matches[0]  # first match
#                 break

# if found_word:
#     print(f"\n  Stored variable contains exact word from PDF: {found_word}")
# else:
#     print(f" Word '{word_to_find}' not found in the PDF.")

# from pdf2image import convert_from_path
# import pytesseract

# # Explicitly set path to Poppler bin folder
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# poppler_path = r"C:\poppler-24.08.0\Library\bin"  # Replace with your actual path

# pages = convert_from_path('Deepa.pdf', dpi=300, poppler_path=poppler_path)

# # OCR example
# text = pytesseract.image_to_string(pages[0])
# print(text)

