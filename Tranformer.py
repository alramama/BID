from tkinter import *
import tkinter.messagebox
import time
import datetime
import tempfile, os
import self as self
from tkinter import filedialog
import PyPDF2

BID = Tk()
BID.geometry("1500x1000+0+0")
BID.title("BID INFORMATION")


MOUNT = StringVar()
KVA_RATING = StringVar()
PHASE = StringVar()
APPLICATION_PRIMARY_VOLT = StringVar()
ACTUAL_PRIMARY_VOLT = StringVar()
SECONDARY_VOLT = StringVar()
PRIMARY_BIL_RATING = StringVar()
SECONDARY_BIL_RATINGS = StringVar()
VECTOR_GROUP = StringVar()
PRIMARY_BUSHINGS = StringVar()
SECONDARY_BUSHINGS = StringVar()
PRIMARY_CONNECTIONS = StringVar()
SECONDARY_CONNECTIONS = StringVar()
STANDARD_SPECIFICATION = StringVar()

BID_MainFrame = Frame(BID, bd=16, width=1350, height=600, relief=RIDGE)
BID_MainFrame.grid(row=0, column=0)

FRAM_BID_Emp_Ent = Frame(BID_MainFrame, bd=16, width=100, height=80, relief=RIDGE)
FRAM_BID_Emp_Ent.grid(row=1, column=0)

lbl_MOUNT =                     Label(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text="MOUNT",                     fg="black", bd=5).grid(row=0, column=0, sticky=W)
lbl_KVA_RATING =                Label(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text="KVA_RATING",                fg="black", bd=5).grid(row=1, column=0, sticky=W)
lbl_PHASE =                     Label(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text="PHASE",                     fg="black", bd=5).grid(row=2, column=0, sticky=W)
lbl_APPLICATION_PRIMARY_VOLT =  Label(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text="APPLICATION_PRIMARY_VOLT",  fg="black", bd=5).grid(row=3, column=0, sticky=W)
lbl_ACTUAL_PRIMARY_VOLT =       Label(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text="ACTUAL_PRIMARY_VOLT",       fg="black", bd=5).grid(row=4, column=0, sticky=W)
lbl_SECONDARY_VOLT =            Label(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text="SECONDARY_VOLT",            fg="black", bd=5).grid(row=5, column=0, sticky=W)
lbl_PRIMARY_BIL_RATING =        Label(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text="PRIMARY_BIL_RATING",        fg="black", bd=5).grid(row=6, column=0, sticky=W)
lbl_SECONDARY_BIL_RATINGS =     Label(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text="SECONDARY_BIL_RATINGS",     fg="black", bd=5).grid(row=7, column=0, sticky=W)
lbl_VECTOR_GROUP =              Label(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text="VECTOR_GROUP",              fg="black", bd=5).grid(row=8, column=0, sticky=W)
lbl_PRIMARY_BUSHINGS =          Label(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text="PRIMARY_BUSHINGS",          fg="black", bd=5).grid(row=9, column=0, sticky=W)
lbl_SECONDARY_BUSHINGS =        Label(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text="SECONDARY_BUSHINGS",        fg="black", bd=5).grid(row=10, column=0, sticky=W)
lbl_PRIMARY_CONNECTIONS =       Label(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text="PRIMARY_CONNECTIONS",       fg="black", bd=5).grid(row=11, column=0, sticky=W)
lbl_SECONDARY_CONNECTIONS =     Label(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text="SECONDARY_CONNECTIONS",     fg="black", bd=5).grid(row=12, column=0, sticky=W)
lbl_STANDARD_SPECIFICATION =    Label(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text="STANDARD_SPECIFICATION",    fg="black", bd=5).grid(row=13, column=0, sticky=W)

ent_MOUNT =                     Entry(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text=MOUNT,                     fg="black", bd=5).grid(row=0, column=1, sticky=W)
ent_KVA_RATING =                Entry(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text=KVA_RATING,                fg="black", bd=5).grid(row=1, column=1, sticky=W)
ent_PHASE =                     Entry(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text=PHASE,                     fg="black", bd=5).grid(row=2, column=1, sticky=W)
ent_APPLICATION_PRIMARY_VOLT =  Entry(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text=APPLICATION_PRIMARY_VOLT,  fg="black", bd=5).grid(row=3, column=1, sticky=W)
ent_ACTUAL_PRIMARY_VOLT =       Entry(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text=ACTUAL_PRIMARY_VOLT,       fg="black", bd=5).grid(row=4, column=1, sticky=W)
ent_SECONDARY_VOLT =            Entry(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text=SECONDARY_VOLT,            fg="black", bd=5).grid(row=5, column=1, sticky=W)
ent_PRIMARY_BIL_RATING =        Entry(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text=PRIMARY_BIL_RATING,        fg="black", bd=5).grid(row=6, column=1, sticky=W)
ent_SECONDARY_BIL_RATINGS =     Entry(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text=SECONDARY_BIL_RATINGS,     fg="black", bd=5).grid(row=7, column=1, sticky=W)
ent_VECTOR_GROUP =              Entry(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text=VECTOR_GROUP,              fg="black", bd=5).grid(row=8, column=1, sticky=W)
ent_PRIMARY_BUSHINGS =          Entry(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text=PRIMARY_BUSHINGS,          fg="black", bd=5).grid(row=9, column=1, sticky=W)
ent_SECONDARY_BUSHINGS =        Entry(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text=SECONDARY_BUSHINGS,        fg="black", bd=5).grid(row=10, column=1, sticky=W)
ent_PRIMARY_CONNECTIONS =       Entry(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text=PRIMARY_CONNECTIONS,       fg="black", bd=5).grid(row=11, column=1, sticky=W)
ent_SECONDARY_CONNECTIONS =     Entry(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text=SECONDARY_CONNECTIONS,     fg="black", bd=5).grid(row=12, column=1, sticky=W)
ent_STANDARD_SPECIFICATION =    Entry(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text=STANDARD_SPECIFICATION,    fg="black", bd=5).grid(row=13, column=1, sticky=W)


FRAM_BID_Emp_text = Frame(BID_MainFrame, bd=16, width=100, height=80, relief=RIDGE)
FRAM_BID_Emp_text.grid(row=2, column=0)
ent_SOW = Text(FRAM_BID_Emp_text, font=('arial', 12, 'bold'), width= 50,height=10, fg="black", bd=5)
ent_SOW.grid(row=7, column=1, sticky=W)

FRAM_BID_Emp_BTN = Frame(BID_MainFrame, bd=16, width=100, height=80, relief=RIDGE)
FRAM_BID_Emp_BTN.grid(row=3, column=0)
btn = Button(FRAM_BID_Emp_BTN,bd = 8 , pady = 8 , fg = "black", font = ('arial',16, 'bold'), width =11, text = "insert_sow", bg = "white")
btn.grid(row = 0 , column = 0)
btn = Button(FRAM_BID_Emp_BTN,bd = 8 , pady = 8 , fg = "black", font = ('arial',16, 'bold'), width =11, text = "find", bg = "white")
btn.grid(row = 0 , column = 1)



BID.mainloop()
