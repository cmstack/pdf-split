# import requests

# x = requests.get('https://w3schools.com/python/demopage.htm')

# print(x.text)


import os
from PyPDF2 import PdfWriter, PdfReader

input = PdfReader(open("input/document.pdf", "rb"))
for i in range(len(input.pages)):
    output = PdfWriter()
    output.add_page(input.pages[i])
    with open("output/document-page%s.pdf" % i, "wb") as outputStream:
        output.write(outputStream)