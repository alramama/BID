import pdfplumber
from tkinter import filedialog

open_file = filedialog.askopenfilename()
with pdfplumber.open(open_file) as pdf:
    any_page = pdf.pages[0]
    #action = any_page.extract_words()
    action = any_page.extract_table()
    print(action)
    print("------------------------------------")
    action1 = any_page.extract_tables()
    print(action1)
    print("------------------------------------")
    action2 = any_page.extract_text()
    print(action2)
