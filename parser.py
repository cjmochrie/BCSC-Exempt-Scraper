from PyPDF2 import PdfFileReader
import re

test = PdfFileReader('test.pdf')
print(test.pages)

full_text = ''
for count, page in enumerate(test.pages):
    print(count)
    full_text += page.extractText()
    
#print(full_text)
issuer = re.findall(r'if its name has changed since this report was last filed; ([^;.]*)', full_text)[0].strip()
print(issuer)

