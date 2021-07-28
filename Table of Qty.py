from tkinter import *
import tkinter.messagebox
import time
import datetime
import tempfile, os

Table_of_Qty = Tk()
Table_of_Qty.geometry("800x1000+0+0")
Table_of_Qty.title("TABLE_OF_QTY INFORMATION")
#Table_of_Qty_Type = ["Sales","Service","Contracts"]
#Customer = ["Gov","SEC","ARAMCO","SABIC","SWCC","NWC"]
#=====================================================mysql.connector===============================================
import mysql.connector
conn = mysql.connector.connect(user = 'root',password= "", host = 'localhost',database = 'tender')
print(conn)
conn.close()
#===================================================================Mysql.Create table===============================================
import mysql.connector
conn = mysql.connector.connect(user = 'root',password= "", host = 'localhost',database = 'tender')
mycursor = conn.cursor()
mycursor.execute("CREATE TABLE Table_of_Qty (name VARCHAR(255), address VARCHAR(255))")
RFQ_No
Item_Name
Item_type
Quantity
Unit
Unit_price
Total_price
Tax
Total_Price_TAX
Bid_Table
YES_No
conn.close()
#=======================================================================Combobox========================================================
RFQ_No = []
#===================================================================TABLE_OF_QTYTopFram=================================================
#TABLE_OF_QTY_Page_title = Frame(TABLE_OF_QTY, bd=16, width=1350, height=60, relief=RAISED)
#TABLE_OF_QTY_Page_title.pack(side=TOP)
#TABLE_OF_QTY_Page_Name = Label(TABLE_OF_QTY_Page_title,font=('arial',40, 'bold'),text = "TABLE_OF_QTY INFORMATION", bd=10)
#TABLE_OF_QTY_Page_Name.pack()
#===================================================================TABLE_OF_QTYBOTTOMFram=================================================
Table_of_Qty_MainFrame = Frame(Table_of_Qty, bd=16, width=1350, height=600, relief=RAISED)
Table_of_Qty_MainFrame.grid(row=0, column=0)
#===================================================================Table_of_Qty_Cost_Eng.=================================================
FRAM_Table_of_Qty_Cost_Eng = Frame(TABLE_OF_QTY_MainFrame, bd=16, width=700, height=600, relief=RIDGE )
FRAM_Table_of_Qty_Cost_Eng.grid(row=0, column=0)

lbl_RFQ_No =             Label(Table_of_Qty_MainFrame, font=('arial', 6, 'bold'),text="RFQ_No",         fg="black", bd=5).grid(row=0, column=0)
lbl_Item_Name =          Label(Table_of_Qty_MainFrame, font=('arial', 6, 'bold'),text="Item_Name",      fg="black", bd=5).grid(row=1, column=0)
lbl_Item_type =          Label(Table_of_Qty_MainFrame, font=('arial', 6, 'bold'),text="Item_type",      fg="black", bd=5).grid(row=2, column=0)
ENT_RFQ_No =             Entry(Table_of_Qty_MainFrame, font=('arial', 6, 'bold'),text="RFQ_No",         fg="black", bd=5).grid(row=0, column=1)
ENT_Item_Name =          Entry(Table_of_Qty_MainFrame, font=('arial', 6, 'bold'),text="Item_Name",      fg="black", bd=5).grid(row=1, column=1)
ENT_Item_type =          Entry(Table_of_Qty_MainFrame, font=('arial', 6, 'bold'),text="Item_type",      fg="black", bd=5).grid(row=2, column=1)

lbl_Quantity =           Label(Table_of_Qty_MainFrame, font=('arial', 6, 'bold'),text="Quantity",       fg="black", bd=5).grid(row=0, column=2)
lbl_Unit =               Label(Table_of_Qty_MainFrame, font=('arial', 6, 'bold'),text="Unit",           fg="black", bd=5).grid(row=1, column=2)
lbl_Unit_price =         Label(Table_of_Qty_MainFrame, font=('arial', 6, 'bold'),text="Unit_price",     fg="black", bd=5).grid(row=2, column=2)
ENT_Quantity =           Entry(Table_of_Qty_MainFrame, font=('arial', 6, 'bold'),text="Quantity",       fg="black", bd=5).grid(row=0, column=3)
ENT_Unit =               Entry(Table_of_Qty_MainFrame, font=('arial', 6, 'bold'),text="Unit",           fg="black", bd=5).grid(row=1, column=3)
ENT_Unit_price =         Entry(Table_of_Qty_MainFrame, font=('arial', 6, 'bold'),text="Unit_price",     fg="black", bd=5).grid(row=2, column=3)

lbl_Total_price =        Label(Table_of_Qty_MainFrame, font=('arial', 6, 'bold'),text="Total_price",    fg="black", bd=5).grid(row=0, column=4)
lbl_Tax =                Label(Table_of_Qty_MainFrame, font=('arial', 6, 'bold'),text="Tax",            fg="black", bd=5).grid(row=1, column=4)
lbl_Total_Price_TAX =    Label(Table_of_Qty_MainFrame, font=('arial', 6, 'bold'),text="Total_Price_TAX",fg="black", bd=5).grid(row=2, column=4)
ENT_Total_price =        Entry(Table_of_Qty_MainFrame, font=('arial', 6, 'bold'),text="Total_price",    fg="black", bd=5).grid(row=0, column=5)
ENT_Tax =                Entry(Table_of_Qty_MainFrame, font=('arial', 6, 'bold'),text="Tax",            fg="black", bd=5).grid(row=1, column=5)
ENT_Total_Price_TAX =    Entry(Table_of_Qty_MainFrame, font=('arial', 6, 'bold'),text="Total_Price_TAX",fg="black", bd=5).grid(row=2, column=5)

lbl_Bid_Table =          Label(Table_of_Qty_MainFrame, font=('arial', 6, 'bold'),text="Bid Table",      fg="black", bd=5).grid(row=0, column=6)
lbl_YES_No =             Label(Table_of_Qty_MainFrame, font=('arial', 6, 'bold'),text="YES/No",         fg="black", bd=5).grid(row=1, column=6)
ENT_Bid_Table =          Entry(Table_of_Qty_MainFrame, font=('arial', 6, 'bold'),text="Bid Table",      fg="black", bd=5).grid(row=0, column=7)
ENT_YES_No =             Entry(Table_of_Qty_MainFrame, font=('arial', 6, 'bold'),text="YES/No",         fg="black", bd=5).grid(row=1, column=7)


TABLE_OF_QTY.mainloop()
