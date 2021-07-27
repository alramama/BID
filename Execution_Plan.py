from tkinter import *
import tkinter.messagebox
import time
import datetime
import tempfile, os

Execution_Plan = Tk()
Execution_Plan.geometry("800x1000+0+0")
Execution_Plan.title("EXECUTION PLAN INFORMATION")
#Execution Plan_Type = ["Sales","Service","Contracts"]
#Customer = ["Gov","SEC","ARAMCO","SABIC","SWCC","NWC"]

#===================================================================EXECUTION PLANTopFram=================================================
#EXECUTION PLAN_Page_title = Frame(EXECUTION PLAN, bd=16, width=1350, height=60, relief=RAISED)
#EXECUTION PLAN_Page_title.pack(side=TOP)
#EXECUTION PLAN_Page_Name = Label(EXECUTION PLAN_Page_title,font=('arial',40, 'bold'),text = "EXECUTION PLAN INFORMATION", bd=10)
#EXECUTION PLAN_Page_Name.pack()
#===================================================================EXECUTION PLANBOTTOMFram=================================================
Execution_Plan_MainFrame1 = Frame(Execution_Plan, bd=16, width=1350, height=600, relief=RIDGE)
Execution_Plan_MainFrame1.grid(row=0, column=0)
#===================================================================Execution Plan_Cost_Eng.=================================================
Execution_Plan_MainFrame = Frame(Execution_Plan_MainFrame1, bd=16, width=700, height=600, relief=RIDGE )
Execution_Plan_MainFrame.grid(row=0, column=0)

lbl_RFQ_No =             Label(Execution_Plan_MainFrame, font=('arial', 6, 'bold'),text="RFQ_No",         fg="black", bd=5).grid(row=0, column=0)
lbl_Item_Name =          Label(Execution_Plan_MainFrame, font=('arial', 6, 'bold'),text="Item_Name",      fg="black", bd=5).grid(row=1, column=0)
lbl_Item_type =          Label(Execution_Plan_MainFrame, font=('arial', 6, 'bold'),text="Item_type",      fg="black", bd=5).grid(row=2, column=0)
ENT_RFQ_No =             Entry(Execution_Plan_MainFrame, font=('arial', 6, 'bold'),text="RFQ_No",         fg="black", bd=5).grid(row=0, column=1)
ENT_Item_Name =          Entry(Execution_Plan_MainFrame, font=('arial', 6, 'bold'),text="Item_Name",      fg="black", bd=5).grid(row=1, column=1)
ENT_Item_type =          Entry(Execution_Plan_MainFrame, font=('arial', 6, 'bold'),text="Item_type",      fg="black", bd=5).grid(row=2, column=1)

lbl_Quantity =           Label(Execution_Plan_MainFrame, font=('arial', 6, 'bold'),text="Quantity",       fg="black", bd=5).grid(row=0, column=2)
lbl_Start_date =         Label(Execution_Plan_MainFrame, font=('arial', 6, 'bold'),text="Start_date",     fg="black", bd=5).grid(row=1, column=2)
lbl_END_date =           Label(Execution_Plan_MainFrame, font=('arial', 6, 'bold'),text="END_date",       fg="black", bd=5).grid(row=2, column=2)
ENT_Quantity =           Entry(Execution_Plan_MainFrame, font=('arial', 6, 'bold'),text="Quantity",       fg="black", bd=5).grid(row=0, column=3)
ENT_Start_date =         Entry(Execution_Plan_MainFrame, font=('arial', 6, 'bold'),text="Unit",           fg="black", bd=5).grid(row=1, column=3)
ENT_END_date =           Entry(Execution_Plan_MainFrame, font=('arial', 6, 'bold'),text="Unit_price",     fg="black", bd=5).grid(row=2, column=3)

lbl_Duration =           Label(Execution_Plan_MainFrame, font=('arial', 6, 'bold'),text="Duration",       fg="black", bd=5).grid(row=0, column=4)
lbl_Engineers =          Label(Execution_Plan_MainFrame, font=('arial', 6, 'bold'),text="Engineers",      fg="black", bd=5).grid(row=1, column=4)
lbl_Tech =               Label(Execution_Plan_MainFrame, font=('arial', 6, 'bold'),text="Tech",           fg="black", bd=5).grid(row=2, column=4)
ENT_Duration =           Entry(Execution_Plan_MainFrame, font=('arial', 6, 'bold'),text="Duration",       fg="black", bd=5).grid(row=0, column=5)
ENT_Engineers =          Entry(Execution_Plan_MainFrame, font=('arial', 6, 'bold'),text="Engineers",      fg="black", bd=5).grid(row=1, column=5)
ENT_Tech =               Entry(Execution_Plan_MainFrame, font=('arial', 6, 'bold'),text="Tech",           fg="black", bd=5).grid(row=2, column=5)

lbl_Day_Cost =           Label(Execution_Plan_MainFrame, font=('arial', 6, 'bold'),text="Day_Cost",      fg="black", bd=5).grid(row=0, column=6)
ENT_Day_Cost =           Entry(Execution_Plan_MainFrame, font=('arial', 6, 'bold'),text="Bid Table",      fg="black", bd=5).grid(row=0, column=7)


Execution_Plan.mainloop()
