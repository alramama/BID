from tkinter import *
import tkinter.messagebox
import time
import datetime
import tempfile, os

Proposed_Table_of_Qty = Tk()
Proposed_Table_of_Qty.geometry("800x1000+0+0")
Proposed_Table_of_Qty.title("PROPOSED_TABLE_OF_QTY INFORMATION")
#Proposed_Table_of_Qty_Type = ["Sales","Service","Contracts"]
#Customer = ["Gov","SEC","ARAMCO","SABIC","SWCC","NWC"]

#===================================================================PROPOSED_TABLE_OF_QTYTopFram=================================================
#PROPOSED_TABLE_OF_QTY_Page_title = Frame(PROPOSED_TABLE_OF_QTY, bd=16, width=1350, height=60, relief=RAISED)
#PROPOSED_TABLE_OF_QTY_Page_title.pack(side=TOP)
#PROPOSED_TABLE_OF_QTY_Page_Name = Label(PROPOSED_TABLE_OF_QTY_Page_title,font=('arial',40, 'bold'),text = "PROPOSED_TABLE_OF_QTY INFORMATION", bd=10)
#PROPOSED_TABLE_OF_QTY_Page_Name.pack()
#===================================================================PROPOSED_TABLE_OF_QTYBOTTOMFram=================================================
Proposed_Table_of_Qty_MainFrame = Frame(Proposed_Table_of_Qty, bd=16, width=1350, height=600, relief=RAISED)
Proposed_Table_of_Qty_MainFrame.grid(row=0, column=0)
#===================================================================Proposed_Table_of_Qty_Cost_Eng.=================================================
FRAM_Proposed_Table_of_Qty_Cost_Eng = Frame(PROPOSED_TABLE_OF_QTY_MainFrame, bd=16, width=700, height=600, relief=RIDGE )
FRAM_Proposed_Table_of_Qty_Cost_Eng.grid(row=0, column=0)

lbl_RFQ_No =             Label(Proposed_Table_of_Qty_MainFrame, font=('arial', 6, 'bold'),text="RFQ_No",         fg="black", bd=5).grid(row=0, column=0)
lbl_Item_Name =          Label(Proposed_Table_of_Qty_MainFrame, font=('arial', 6, 'bold'),text="Item_Name",      fg="black", bd=5).grid(row=1, column=0)
lbl_Item_type =          Label(Proposed_Table_of_Qty_MainFrame, font=('arial', 6, 'bold'),text="Item_type",      fg="black", bd=5).grid(row=2, column=0)
ENT_RFQ_No =             Entry(Proposed_Table_of_Qty_MainFrame, font=('arial', 6, 'bold'),text="RFQ_No",         fg="black", bd=5).grid(row=0, column=1)
ENT_Item_Name =          Entry(Proposed_Table_of_Qty_MainFrame, font=('arial', 6, 'bold'),text="Item_Name",      fg="black", bd=5).grid(row=1, column=1)
ENT_Item_type =          Entry(Proposed_Table_of_Qty_MainFrame, font=('arial', 6, 'bold'),text="Item_type",      fg="black", bd=5).grid(row=2, column=1)

lbl_Quantity =           Label(Proposed_Table_of_Qty_MainFrame, font=('arial', 6, 'bold'),text="Quantity",       fg="black", bd=5).grid(row=0, column=2)
lbl_Unit =               Label(Proposed_Table_of_Qty_MainFrame, font=('arial', 6, 'bold'),text="Unit",           fg="black", bd=5).grid(row=1, column=2)
lbl_Unit_price =         Label(Proposed_Table_of_Qty_MainFrame, font=('arial', 6, 'bold'),text="Unit_price",     fg="black", bd=5).grid(row=2, column=2)
ENT_Quantity =           Entry(Proposed_Table_of_Qty_MainFrame, font=('arial', 6, 'bold'),text="Quantity",       fg="black", bd=5).grid(row=0, column=3)
ENT_Unit =               Entry(Proposed_Table_of_Qty_MainFrame, font=('arial', 6, 'bold'),text="Unit",           fg="black", bd=5).grid(row=1, column=3)
ENT_Unit_price =         Entry(Proposed_Table_of_Qty_MainFrame, font=('arial', 6, 'bold'),text="Unit_price",     fg="black", bd=5).grid(row=2, column=3)

lbl_Total_price =        Label(Proposed_Table_of_Qty_MainFrame, font=('arial', 6, 'bold'),text="Total_price",    fg="black", bd=5).grid(row=0, column=4)
lbl_Tax =                Label(Proposed_Table_of_Qty_MainFrame, font=('arial', 6, 'bold'),text="Tax",            fg="black", bd=5).grid(row=1, column=4)
lbl_Total_Price_TAX =    Label(Proposed_Table_of_Qty_MainFrame, font=('arial', 6, 'bold'),text="Total_Price_TAX",fg="black", bd=5).grid(row=2, column=4)
ENT_Total_price =        Entry(Proposed_Table_of_Qty_MainFrame, font=('arial', 6, 'bold'),text="Total_price",    fg="black", bd=5).grid(row=0, column=5)
ENT_Tax =                Entry(Proposed_Table_of_Qty_MainFrame, font=('arial', 6, 'bold'),text="Tax",            fg="black", bd=5).grid(row=1, column=5)
ENT_Total_Price_TAX =    Entry(Proposed_Table_of_Qty_MainFrame, font=('arial', 6, 'bold'),text="Total_Price_TAX",fg="black", bd=5).grid(row=2, column=5)

lbl_Bid_Table =          Label(Proposed_Table_of_Qty_MainFrame, font=('arial', 6, 'bold'),text="Bid Table",      fg="black", bd=5).grid(row=0, column=6)
lbl_YES_No =             Label(Proposed_Table_of_Qty_MainFrame, font=('arial', 6, 'bold'),text="YES/No",         fg="black", bd=5).grid(row=1, column=6)
ENT_Bid_Table =          Entry(Proposed_Table_of_Qty_MainFrame, font=('arial', 6, 'bold'),text="Bid Table",      fg="black", bd=5).grid(row=0, column=7)
ENT_YES_No =             Entry(Proposed_Table_of_Qty_MainFrame, font=('arial', 6, 'bold'),text="YES/No",         fg="black", bd=5).grid(row=1, column=7)


PROPOSED_TABLE_OF_QTY.mainloop()

