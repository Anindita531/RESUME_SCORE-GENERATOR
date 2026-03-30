import PyPDF2

file = open("resume_1.pdf", "rb")   # PDF open with read binary
reader = PyPDF2.PdfReader(file)

print(len(reader.pages))  # total pages

page = reader.pages[0]
text = page.extract_text()

print(text)