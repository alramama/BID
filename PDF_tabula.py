import tabula
from tkinter import filedialog
open_file = filedialog.askopenfilename()
file = tabula.read_pdf(open_file, pages = 0)
print(file)
