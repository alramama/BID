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
RFQ_NO = Stringvar()
font = ('arial',7, 'bold')
titleFram = Frame(root, bd=16, width=1350, height=50, relief=RAISED)
titleFram.grid(row =0 , column = 0,sticky= N, padx=5, pady=5)
#==============================START_TEXTFRAME===================================================
fram_width = 20
fram_height=20
textFram = Frame(root, bd=16, width=fram_width, height=fram_height, relief=RIDGE)
textFram.grid(row=1,column = 0,sticky= NW, padx=5, pady=5)
textlbl = Label(textFram, text = "Data Text", bd=16, width=fram_width, relief=RIDGE)
textlbl.grid(row=1,column = 0,sticky= NW, padx=5, pady=5)
textform = Text(textFram, bd=16, width=fram_width, height=fram_height, relief=RIDGE)
textform.grid(row =2,column = 0,sticky= NW, padx=5, pady=5)

#==============================END_TEXT_FRAME===================================================
#
#==============================START_lbl_ent_FRAME===================================================

lbl_ent_width = 20
lbl_bd = 5
ent_bd = 5

lbl_sticky = NW
lbl_padx = 5
lbl_pady =5

ent_sticky = NS
ent_padx = 5
ent_pady = 5

lbl_ent_Fram00 = Frame(root, bd=16, width=1350, height=50, relief=RIDGE)
lbl_ent_Fram00.grid(row =1 , column = 1,sticky= lbl_sticky, padx=lbl_padx, pady=lbl_pady)

lbl_ent_Fram01 = Fram(lbl_ent_Fram, text = "Data Text", bd=16, width=fram_width, relief=RIDGE)
lbl_ent_Fram01.grid(row=0,column = 0,sticky= NW, padx=5, pady=5)

lblRFQ_No = Label(lbl_ent_Fram, font = font, text= "RFQ_NO", width = lbl_ent_width,  fg ="black", bd = lbl_bd )
lblRFQ_No.grid(row = 0 , column = 0,sticky= lbl_sticky, padx=lbl_padx, pady=lbl_pady)

lblRFQ_No = Label(lbl_ent_Fram, font = font, text= "RFQ_NO" , width = lbl_ent_width,fg = "black", bd = lbl_bd )
lblRFQ_No.grid(row = 0 , column = 0,sticky= lbl_sticky, padx=lbl_padx, pady=lbl_pady)

lblRFQ_name = Label(lbl_ent_Fram, font = font, text= "RFQ_NO" , width = lbl_ent_width,fg = "black", bd = lbl_bd )
lblRFQ_name.grid(row = 1 , column = 0,sticky= lbl_sticky, padx=lbl_padx, pady=lbl_pady)

lblRFQ_date = Label(lbl_ent_Fram, font = font, text= "RFQ_NO" , width = lbl_ent_width,fg = "black", bd = lbl_bd )
lblRFQ_date.grid(row = 2 , column = 0,sticky= lbl_sticky, padx=lbl_padx, pady=lbl_pady)

lblRFQ_Customer = Label(lbl_ent_Fram, font = font, text= "RFQ_NO" , width = lbl_ent_width,fg = "black", bd = lbl_bd )
lblRFQ_Customer.grid(row = 3 , column = 0,sticky= lbl_sticky, padx=lbl_padx, pady=lbl_pady)

lblRFQ_lastdate = Label(lbl_ent_Fram, font = font, text= "RFQ_NO" , width = lbl_ent_width,fg = "black", bd = lbl_bd )
lblRFQ_lastdate.grid(row = 4 , column = 0,sticky= lbl_sticky, padx=lbl_padx, pady=lbl_pady)

lblRFQ_SOW = Label(lbl_ent_Fram, font = font, text= "RFQ_NO", width = lbl_ent_width,fg = "black", bd = 20 )
lblRFQ_SOW.grid(row = 5 , column = 0,sticky= lbl_sticky, padx=lbl_padx, pady=lbl_pady)

#ENTRY
entRFQ_No = Entry(lbl_ent_Fram, font = font, textvariable= RFQ_NO,width = lbl_ent_width, fg = "black", bd = ent_bd )
entRFQ_No.grid(row = 0 , column = 1,sticky= ent_sticky, padx=ent_padx, pady=ent_pady)

entRFQ_name = Entry(lbl_ent_Fram, font = font, textvariable= RFQ_NO,width = lbl_ent_width, fg = "black", bd = ent_bd )
entRFQ_name.grid(row = 1 , column = 1,sticky= ent_sticky, padx=ent_padx, pady=ent_pady)

entRFQ_date = Entry(lbl_ent_Fram, font = font, textvariable= RFQ_NO,width = lbl_ent_width, fg = "black", bd = ent_bd )
entRFQ_date.grid(row = 2 , column = 1,sticky= ent_sticky, padx=ent_padx, pady=ent_pady)

entRFQ_Customer = Entry(lbl_ent_Fram, font = font, textvariable= RFQ_NO,width = lbl_ent_width, fg = "black", bd = ent_bd )
entRFQ_Customer.grid(row = 3 , column = 1,sticky= ent_sticky, padx=ent_padx, pady=ent_pady)

entRFQ_lastdate = Entry(lbl_ent_Fram, font = font, textvariable= RFQ_NO,width = lbl_ent_width, fg = "black", bd = ent_bd )
entRFQ_lastdate.grid(row = 4 , column = 1,sticky= ent_sticky, padx=ent_padx, pady=ent_pady)

entRFQ_SOW = Entry(lbl_ent_Fram, font = font, textvariable= RFQ_NO,width = lbl_ent_width, fg = "black", bd = ent_bd )
entRFQ_SOW.grid(row = 5 , column = 1,sticky= ent_sticky, padx=ent_padx, pady=ent_pady)

#==============================END_lbl_ent_FRAME===================================================

def insert_into_mysql():
  a = textform.get("1.0",END)
  a0 = a.split("\n\n")
  i = 0
  while i < len(a0):
    print(a0[i])
    i+=1



btnFram = Frame(root, bd=16, width=1350, height=50, relief=RIDGE)
btnFram.grid(row =2 , column = 0)

BtnInsert = Button(btnFram, bd = 8 , pady = 8 , fg = "black", font = ('arial',16, 'bold'), width =11, text = "Rest", bg = "white", command = insert_into_mysql).grid(row = 0 , column = 0)

root.mainloop()


