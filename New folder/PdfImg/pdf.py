import fitz
import pytesseract
from PIL import Image
import io

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

doc = fitz.open("New.pdf")

for page_num, page in enumerate(doc):
    pix = page.get_pixmap(dpi=300)
    img = Image.open(io.BytesIO(pix.tobytes()))

    gray = img.convert("L")  # convert to grayscale

    config = r"--oem 3 --psm 6"
    text = pytesseract.image_to_string(gray, config=config)

    print(f"\n--- Page {page_num + 1} ---\n{text}")


# Explanation Code
# import fitz

#  fitz is PyMuPDF package.
#  Use: PDF open panna, read panna, page ah image change panna.

# import pytesserac
#  Ithu Tesseract OCR engine-ku Python interface.
#  Use: Image la irukkura letters ah text ah OCR panni edukka.

# from PIL import Image
#  PIL (Python Imaging Library) la irundhu Image class import panrom.
#  Use: Image open, convert, process panna.

# import io
#  io.BytesIO  Memory la irukkura image data va fake file maari treat panna use panrom.
#  Use: Image bytes-a read panna.




# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


#  Windows system la tesseract install irukkura path-a specify panrom.
#  Use: Python ku tesseract OCR engine path solradhu.




# doc = fitz.open("New.pdf")


#  "New.pdf" file open panrom using PyMuPDF (fitz).
#  doc la andha PDF oda page data store aagudhu.
#  Use: Full PDF handle panna.




# for page_num, page in enumerate(doc):


#  enumerate(doc) -> Every page ku page_num (index), page object kedakkum.
#  Loop potrukom -> PDF oda every page process aagum.

#     pix = page.get_pixmap(dpi=300)


#  get_pixmap() -> andha page-a image maathudhu
#  dpi=300 -> High resolution image (better OCR accuracy)
#  Use: Full PDF page ah screenshot maari convert panna.




#     img = Image.open(io.BytesIO(pix.tobytes()))


#  pix.tobytes() -> Image ah bytes-a maathudhu
#  io.BytesIO(...) -> Memory la fake image file create pannudhu
#  Image.open(...) -> Final ah PIL image object create pannudhu
#  Use: Image object OCR panna ready.


#     gray = img.convert("L")  # convert to grayscale


#  img.convert("L") -> Image ah grayscale la maathudhu
#  OCR ku color thevaila, grayscale accuracy improve pannum
#  Use: OCR-ku perfect image prepare panna.

#     config = r"--oem 3 --psm 6"

#  OCR config set panrom:

#  --oem 3 -> Best OCR engine (neural network LSTM)
#  --psm 6 -> Assume image contains uniform text block (like scanned pages)

#  Use: OCR engine-ku nalla instruction kudukka.
#     text = pytesseract.image_to_string(gray, config=config)


#  image_to_string() -> OCR function
#  gray la irukkura image-a scan panni text ah detect pannudhu
#  Use: Image-la irukkura words read panni text la store pannudhu.

#     print(f"\n--- Page {page_num + 1} ---\n{text}")
#  Each page ku OCR result print aagudhu
#  page_num + 1 -> Human readable format (1-based index)
#  text -> OCR result (image la irundha content)



# Summary Table :

# | Line                  | Meaning                    |
# | --------------------- | -------------------------- |
# | fitz.open()         | PDF open panrom            |
# | get_pixmap(dpi=300) | Page -> Image               |
# | Image.open(...)     | Image object create panrom |
# | convert("L")        | Grayscale (better OCR)     |
# | image_to_string()   | OCR run pannudhu           |
# | print()             | Result print panrom        |