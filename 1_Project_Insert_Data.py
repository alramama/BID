from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import random
import time
import datetime
import mysql.conncter

root = Tk()
root.geometry("1350x650+0+0")
root.title("Tendring System")

titleFram = Frame(root, bd=16, width=1350, height=50, relief=RAISED)
titleFram.grid(row =0 , column = 0)
#==============================START_TEXTFRAME===================================================
textFram = Frame(root, bd=16, width=1350, height=50, relief=RIDGE)
textFram.grid(row=1,column = 0)
textlbl = Label(textFram, text = "Data Text", bd=16, width=1350, height=5, relief=RIDGE)
textlbl.grid(row=1,column = 0)
textform = Text(textFram, bd=16, width=1350, height=50, relief=RIDGE)
textform.grid(row =2,column = 0)
#==============================END_TEXT_FRAME===================================================
#
#==============================START_lbl_ent_FRAME===================================================

lbl_ent_Fram = Frame(root, bd=16, width=1350, height=50, relief=RIDGE)
lbl_ent_Fram.grid(row =1 , column = 1)

lblRFQ_No = Label(lbl_ent_Fram, font = ('arial',12, 'bold'), text= "RFQ_NO", fg = "black", bd = 20 )
lblRFQ_No.grid(row = 0 , column = 0)

lblRFQ_name = Label(lbl_ent_Fram, font = ('arial',12, 'bold'), text= "RFQ_NO", fg = "black", bd = 20 )
lblRFQ_name.grid(row = 1 , column = 0)

lblRFQ_date = Label(lbl_ent_Fram, font = ('arial',12, 'bold'), text= "RFQ_NO", fg = "black", bd = 20 )
lblRFQ_date.grid(row = 2 , column = 0)

lblRFQ_Customer = Label(lbl_ent_Fram, font = ('arial',12, 'bold'), text= "RFQ_NO", fg = "black", bd = 20 )
lblRFQ_Customer.grid(row = 3 , column = 0)

lblRFQ_lastdate = Label(lbl_ent_Fram, font = ('arial',12, 'bold'), text= "RFQ_NO", fg = "black", bd = 20 )
lblRFQ_lastdate.grid(row = 4 , column = 0)

lblRFQ_SOW = Label(lbl_ent_Fram, font = ('arial',12, 'bold'), text= "RFQ_NO", fg = "black", bd = 20 )
lblRFQ_SOW.grid(row = 5 , column = 0)

#ENTRY

entRFQ_No = Label(lbl_ent_Fram, font = ('arial',12, 'bold'), textvariable= RFQ_NO, fg = "black", bd = 20 )
entRFQ_No.grid(row = 0 , column = 1)

entRFQ_name = Label(lbl_ent_Fram, font = ('arial',12, 'bold'), textvariable= RFQ_name, fg = "black", bd = 20 )
entRFQ_name.grid(row = 1 , column = 1)

entRFQ_date = Label(lbl_ent_Fram, font = ('arial',12, 'bold'), textvariable= RFQ_date, fg = "black", bd = 20 )
entRFQ_date.grid(row = 2 , column = 1)

entRFQ_Customer = Label(lbl_ent_Fram, font = ('arial',12, 'bold'), textvariable= RFQ_Customer, fg = "black", bd = 20 )
entRFQ_Customer.grid(row = 3 , column = 1)

entRFQ_lastdate = Label(lbl_ent_Fram, font = ('arial',12, 'bold'), textvariable= RFQ_lastdate, fg = "black", bd = 20 )
entRFQ_lastdate.grid(row = 4 , column = 1)

entRFQ_SOW = Label(lbl_ent_Fram, font = ('arial',12, 'bold'), textvariable= RFQ_SOW, fg = "black", bd = 20 )
entRFQ_SOW.grid(row = 5 , column = 1)
#==============================END_lbl_ent_FRAME===================================================

def insert_into_mysql():
  a = textform.get("1.0",END)
  a0 = a.split("\n\n")
  i = 0
  while i < len(a0):
    def insert_into_table():
      
    insert_into_table()
      



btnFram = Frame(root, bd=16, width=1350, height=50, relief=RIDGE)
btnFram.grid(row =0 , column = 0)

BtnRest = Button(btnFram, bd = 8 , pady = 8 , fg = "black", font = ('arial',16, 'bold'), width =11, text = "Rest", bg = "white", command = insert_into_mysql).grid(row = 0 , column = 0)

root.mainloop()


