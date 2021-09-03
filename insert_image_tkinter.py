from PIL import Image,ImageTk
from tkinter import *
from tkinter import filedialog
root=Tk()
text = Text(root)
text.pack()
#Insert Image

yourImage=filedialog.askopenfilename(title = "Select your image",filetypes = [("Image Files","*.png"),("Image Files","*.jpg")])
#imgFile=Image.open(yourImage)
imgToInsert=ImageTk.PhotoImage(file=yourImage)

text.image_create("current",image=imgToInsert)

root.mainloop()
