from PIL import Image
import pytesseract
import cv2
import pdfplumber
import PyPDF2
import tabula
import camelot
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

root = Tk()
root.geometry("400x400")

def filetype(e):
    open_file = filedialog.askopenfilename()
    if filetype1.get() == "text":
        pdf_file = PyPDF2.PdfFileReader(open_file)
        page = pdf_file.getPage(0)
        page_stuff = page.extractText()
        print(page_stuff)
    elif filetype1.get() =="table":
        mytable = tabula.read_pdf(open_file, pages=0)
        print(mytable)
    elif filetype1.get() == "camlote":
        tables = camelot.read_pdf(open_file)
        print(tables)
    elif filetype1.get() == "PDFplumber":
        with pdfplumber.open(open_file) as pdf:
            first_page = pdf.pages[0]
            print(first_page.extract_text())
    elif filetype1.get() == "tesseract":
        from pdf2image import convert_from_path
        images = convert_from_path(open_file)
        for i in range(len(images)):
            images[i].save('page' + str(i) + '.jpg', 'JPEG')
        pytesseract.tesseract_cmd = r"C:\Tesseract"
        myfile = Image.open(images)
        text = pytesseract.image_to_string(myfile, lang='eng')
        print(text)


filetype1 = ttk.Combobox(root)
filetype1['values'] = "text", "table","camlote","PDFplumber","tesseract"
filetype1.current()
filetype1.bind('<<ComboboxSelected>>', filetype)
filetype1.grid(row=0, column=1)
btn = Button(root,text = "extracted" , command = filetype)
btn.grid()
root.mainloop()
