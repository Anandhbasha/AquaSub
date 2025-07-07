import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io

# Set Tesseract executable path (Windows only)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

pdf_path = "New.pdf"
doc = fitz.open(pdf_path)

for page_num, page in enumerate(doc, start=1):
    images = page.get_images(full=True)

    if not images:
        print(f"\n--- Page {page_num}: No images found ---")
        continue

    print(f"\n--- Page {page_num}: Found {len(images)} image(s) ---")

    for img_index, img_info in enumerate(images, start=1):
        xref = img_info[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]

        img = Image.open(io.BytesIO(image_bytes)).convert("L")  # grayscale

        config = r"--oem 3 --psm 6"
        text = pytesseract.image_to_string(img, config=config)

        print(f"\n📸 Image {img_index} OCR Result:\n{text.strip() or '[No text found]'}")