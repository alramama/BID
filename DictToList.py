from tkinter import *
import tkinter.messagebox
import time
import datetime
import tempfile, os
import self as self
from tkinter import filedialog
import PyPDF2

BID = Tk()
BID.geometry("1500x500+0+0")
BID.title("BID INFORMATION")

data ="""MOUNT:
PAD;
KVA RATING:
1500 KVA;
PHASE:
3 PH;
APPLICATION PRIMARY VOLT:
34500 V AC;
ACTUAL PRIMARY VOLT:
34.5K V AC;
SECONDARY VOLT:
4160/480 V AC;
FREQUENCY:
60 HZ;
PRIMARY BIL RATING:
150 KV;
SECONDARY BIL RATINGS:
30 KV;
VECTOR GROUP:
YYYN0;
PRIMARY BUSHINGS:
(3) LOAD BREAK BUSHING INSERT;
SECONDARY BUSHINGS:
(3) LOAD BREAK BUSHING INSERT FOR 4160 V, (4) ENCLOSED 4-HOLES SPADE TERMINATI ONS FOR 480 V;"""

clean1 = data.replace(";","")
clean2 = clean1.replace(":"," ")
clean3 = clean2.replace(","," ")
#clean4 = clean3.strip()
clean4 = clean3.split("\n")
#A = clean4.strip()

#print(A)
#print(len(A))

MOUNT = StringVar()
KVA_RATING = StringVar()
lbl_MOUNT =             Label(BID, font=('arial', 20, 'bold'), text="MOUNT",   fg="black", bd=5).grid(row=1, column=0, sticky=W)
lbl_KVA_RATING =        Label(BID, font=('arial', 20, 'bold'), text="KVA_RATING",       fg="black", bd=5).grid(row=2, column=0, sticky=W)
ent_MOUNT =             Entry(BID, font=('arial', 22, 'bold'), textvariable=MOUNT,   fg="black", bd=5)
ent_MOUNT.grid(row=1, column=1, sticky=W)
ent_KVA_RATING =        Entry(BID, font=('arial', 22, 'bold'), textvariable=KVA_RATING,       fg="black", bd=5)
ent_KVA_RATING.grid(row=2, column=1, sticky=W)
ent_SOW = Text(BID, font=('arial', 20, 'bold'), width= 100,height=15, fg="black", bd=5)
ent_SOW.grid(row=7, column=1, sticky=W)
#def convert1():
A1 = ent_SOW.get("1.0", END)
#print(A1)


def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct

lst = clean4
Z = (Convert(lst))
print(Z)
x = Z["MOUNT "]
x1 = Z["KVA RATING "]

print(x)
ent_MOUNT.insert(END,x)
ent_KVA_RATING.insert(END,x1)

Convert(lst)






def insert_sow():

    open_file = filedialog.askopenfilename()
    if open_file:
        pdf_file = PyPDF2.PdfFileReader(open_file)
        page = pdf_file.getPage(0)
        page_stuff = page.extractText()
        ent_SOW.insert(1.0,page_stuff)

def get():
    A = ent_SOW.insert(1.0, Z)
    data = ent_SOW.get("1.0", END)
    #A2 = ent_SOW.get(["MOUNT"])


get()


btn = Button(BID,bd = 8 , pady = 8 , fg = "black", font = ('arial',16, 'bold'), width =11, text = "insert_sow", bg = "white",command = insert_sow)
btn.grid(row = 4 , column = 0)
btn = Button(BID,bd = 8 , pady = 8 , fg = "black", font = ('arial',16, 'bold'), width =11, text = "get", bg = "white",command = get)
btn.grid(row = 5 , column = 0)
btn = Button(BID,bd = 8 , pady = 8 , fg = "black", font = ('arial',16, 'bold'), width =11, text = "convert", bg = "white",command = Convert)
btn.grid(row = 6 , column = 0)



BID.mainloop()
