from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import pdfplumber
import tkinter.messagebox
import time
import datetime
import tempfile, os
import re

Table_of_Qty = Tk()
Table_of_Qty.geometry("1500x1000+0+0")
Table_of_Qty.title("TABLE_OF_QTY INFORMATION")
#===================================================================TABLE_OF_QTYBOTTOMFram=================================================
Table_of_Qty_MainFrame = Frame(Table_of_Qty, bd=16, width=1350, height=600, relief=RAISED)
Table_of_Qty_MainFrame.grid(row=0, column=0)
#===================================================================Table_of_Qty_Cost_Eng.=================================================
FRAM_Table_of_Qty_Cost_Eng1 = Frame(Table_of_Qty_MainFrame, bd=16, width=700, height=600, relief=RIDGE )
FRAM_Table_of_Qty_Cost_Eng1.grid(row=0, column=0)
FRAM_text = Text(FRAM_Table_of_Qty_Cost_Eng1, bd=16, width=40, height=40, relief=RIDGE )
FRAM_text.grid(row=0, column=0)


FRAM_Table_of_Qty_Cost_Eng = Frame(Table_of_Qty_MainFrame, bd=16, width=700, height=600, relief=RIDGE )
FRAM_Table_of_Qty_Cost_Eng.grid(row=0, column=1)

lbl_RFQ_No =    Label(FRAM_Table_of_Qty_Cost_Eng, font=('arial', 20, 'bold'),text="RFQ_No",         fg="black", bd=5).grid(row=0, column=0)
lbl_dateOfIssue=Label(FRAM_Table_of_Qty_Cost_Eng, font=('arial', 20, 'bold'),text="dateOfIssue",    fg="black", bd=5).grid(row=1, column=0)
lbl_Lastdate =  Label(FRAM_Table_of_Qty_Cost_Eng, font=('arial', 20, 'bold'),text="Last Date",      fg="black", bd=5).grid(row=2, column=0)
lbl_Bayername = Label(FRAM_Table_of_Qty_Cost_Eng, font=('arial', 20, 'bold'),text="Bayer Name",     fg="black", bd=5).grid(row=3, column=0)
lbl_BayerPhone =Label(FRAM_Table_of_Qty_Cost_Eng, font=('arial', 20, 'bold'),text="Bayer Phone",    fg="black", bd=5).grid(row=4, column=0)
lbl_Unit =      Label(FRAM_Table_of_Qty_Cost_Eng, font=('arial', 20, 'bold'),text="Unit",           fg="black", bd=5).grid(row=5, column=0)
lbl_Qt =        Label(FRAM_Table_of_Qty_Cost_Eng, font=('arial', 20, 'bold'),text="QYN",            fg="black", bd=5).grid(row=6, column=0)
lbl_Qt =        Label(FRAM_Table_of_Qty_Cost_Eng, font=('arial', 20, 'bold'),text="RFQ Name",            fg="black", bd=5).grid(row=7, column=0)

ENT_RFQ_No =    Entry(FRAM_Table_of_Qty_Cost_Eng, font=('arial', 20, 'bold'),width = 30,text="RFQ_No",         fg="black", bd=5)
ENT_RFQ_No.grid(row=0, column=1)
ENT_dateOfIssue=Entry(FRAM_Table_of_Qty_Cost_Eng, font=('arial', 20, 'bold'),width = 30,text="dateOfIssue",    fg="black", bd=5)
ENT_dateOfIssue.grid(row=1, column=1)
ENT_Lastdate =  Entry(FRAM_Table_of_Qty_Cost_Eng, font=('arial', 20, 'bold'),width = 30,text="Last Date",      fg="black", bd=5)
ENT_Lastdate.grid(row=2, column=1)
ENT_Bayername = Entry(FRAM_Table_of_Qty_Cost_Eng, font=('arial', 20, 'bold'),width = 30,text="Bayer Name",     fg="black", bd=5)
ENT_Bayername.grid(row=3, column=1)
ENT_BayerPhone =Entry(FRAM_Table_of_Qty_Cost_Eng, font=('arial', 20, 'bold'),width = 30,text="Bayer Phone",    fg="black", bd=5)
ENT_BayerPhone.grid(row=4, column=1)
ENT_Unit =      Entry(FRAM_Table_of_Qty_Cost_Eng, font=('arial', 20, 'bold'),width = 30,text="Unit",           fg="black", bd=5)
ENT_Unit.grid(row=5, column=1)
ENT_Qt =        Entry(FRAM_Table_of_Qty_Cost_Eng, font=('arial', 20, 'bold'),width = 30,text="QYN",            fg="black", bd=5)
ENT_Qt.grid(row=6, column=1)
ENT_RFQname =        Entry(FRAM_Table_of_Qty_Cost_Eng, font=('arial', 20, 'bold'),width = 30,text="RFQ Name",            fg="black", bd=5)
ENT_RFQname.grid(row=7, column=1)


def rfq():
    aaa = filedialog.askopenfilename()
    with pdfplumber.open(aaa) as pdf:
        first_page = pdf.pages[0]
        a10 = first_page.extract_text()
        a = first_page.extract_table()
        a1 = first_page.extract_tables()


        a3 = (a1[1])
        a4 = (a3[2])
        a5 = (a3[3])
        a6 = (a5)

        a7 = re.split("\n",a10)
        print(a7[12])
        a2 = a[1]
        rfqno = a2[2]
        ENT_RFQ_No.insert(END,rfqno)
        RFQdate = a2[4]
        ENT_dateOfIssue.insert(END, RFQdate)
        RFQlastdate = a2[6]
        ENT_Lastdate.insert(END, RFQlastdate)
        a3 = a[4]
        RFQbyer = a3[3]
        ENT_Bayername.insert(END, RFQbyer)
        RFQtelbyer = a3[5]
        ENT_BayerPhone.insert(END, RFQtelbyer)
        RFQtelbyer = a3[5]
        ENT_BayerPhone.insert(END, RFQtelbyer)
        ENT_Unit1 = a4[3]
        ENT_Unit.insert(END, ENT_Unit1)
        ENT_Qt0 = a4[4]
        ENT_Qt.insert(END, ENT_Qt0)
        ENT_RFQname0 = a7[12]
        ENT_RFQname.insert(END, ENT_RFQname0)



        #print(a)

FRAM_Button = Frame(Table_of_Qty_MainFrame, bd=16, width=700, height=600, relief=RIDGE )
FRAM_Button.grid(row=1, column=0)
lbl_Qt =        Button(FRAM_Button, font=('arial', 20, 'bold'),width = 20,text="uplode",            fg="black",command = rfq, bd=5)
lbl_Qt.grid(row=6, column=1)



Table_of_Qty.mainloop()
