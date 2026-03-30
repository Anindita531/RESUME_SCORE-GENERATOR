import easyocr
from pdf2image import convert_from_path

images = convert_from_path(
    "resume_2.pdf",
    poppler_path=r"C:\poppler\poppler-25.12.0\Library\bin"
)

reader = easyocr.Reader(['en'])

for img in images:
    result = reader.readtext(img, detail=0)
    print(result)