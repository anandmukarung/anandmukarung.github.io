import pdfplumber

with pdfplumber.open('Anand_Rai_Resume.pdf') as pdf:
    text = '\n'.join(page.extract_text() for page in pdf.pages if page.extract_text())
    print(text)