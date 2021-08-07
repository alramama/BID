from tkinter import *
import tkinter.messagebox
import time
import datetime
import tempfile, os
import self as self
BID = Tk()
BID.geometry("800x800+0+0")
BID.title("BID INFORMATION")

Work_Order = StringVar()
RFQ_No = StringVar()

Customer_name = StringVar()
Tender_Name = StringVar()
Tender_NO = StringVar()
Bid_Type = StringVar()

SOW = StringVar()
Received_Date = StringVar()
Closing_Date = StringVar()
Evaluation_Completion_date = StringVar()
Execution_Time = StringVar()

Standerd = StringVar()
Tender_documents = StringVar()

BID_MainFrame = Frame(BID, bd=16, width=1350, height=600, relief=RIDGE)
BID_MainFrame.grid(row=0, column=0)

FRAM_BID_Emp_Info = Frame(BID_MainFrame, bd=16, width=100, height=80, relief=RIDGE)
FRAM_BID_Emp_Info.grid(row=1, column=0)

lbl_work_Order =    Label(FRAM_BID_Emp_Info, font=('arial', 20, 'bold'), text="Work_Order",   fg="black", bd=5).grid(row=1, column=0, sticky=W)
lbl_rfq_no =        Label(FRAM_BID_Emp_Info, font=('arial', 20, 'bold'), text="RFQ_No",       fg="black", bd=5).grid(row=2, column=0, sticky=W)
lbl_work_Order =    Entry(FRAM_BID_Emp_Info, font=('arial', 20, 'bold'), textvariable=Work_Order,   fg="black", bd=5).grid(row=1, column=1, sticky=W)
lbl_rfq_no =        Entry(FRAM_BID_Emp_Info, font=('arial', 20, 'bold'), textvariable=RFQ_No,       fg="black", bd=5).grid(row=2, column=1, sticky=W)

FRAM_BID_Emp_Info1 = Frame(BID_MainFrame, bd=16, width=100, height=80, relief=RIDGE)
FRAM_BID_Emp_Info1.grid(row=2, column=0)

lbl_customer_name = Label(FRAM_BID_Emp_Info1, font=('arial', 20, 'bold'), text="Customer",  fg="black", bd=5).grid(row=3, column=0, sticky=W)
lbl_tender_Name =   Label(FRAM_BID_Emp_Info1, font=('arial', 20, 'bold'), text="Tender_Name",    fg="black", bd=5).grid(row=4, column=0, sticky=W)
lbl_tender_NO =     Label(FRAM_BID_Emp_Info1, font=('arial', 20, 'bold'), text="Tender_NO",      fg="black", bd=5).grid(row=5, column=0, sticky=W)
lbl_bid_Type =      Label(FRAM_BID_Emp_Info1, font=('arial', 20, 'bold'), text="Bid_Type",       fg="black", bd=5).grid(row=6, column=0, sticky=W)
lbl_customer_name = Entry(FRAM_BID_Emp_Info1, font=('arial', 20, 'bold'), textvariable=Customer_name,  fg="black", bd=5).grid(row=3, column=1, sticky=W)
lbl_tender_Name =   Entry(FRAM_BID_Emp_Info1, font=('arial', 20, 'bold'), textvariable=Tender_Name,    fg="black", bd=5).grid(row=4, column=1, sticky=W)
lbl_tender_NO =     Entry(FRAM_BID_Emp_Info1, font=('arial', 20, 'bold'), textvariable=Tender_NO,      fg="black", bd=5).grid(row=5, column=1, sticky=W)
lbl_bid_Type =      Entry(FRAM_BID_Emp_Info1, font=('arial', 20, 'bold'), textvariable=Bid_Type,       fg="black", bd=5).grid(row=6, column=1, sticky=W)



FRAM_BID_Emp_Info2 = Frame(BID_MainFrame, bd=16, width=100, height=80, relief=RIDGE)
FRAM_BID_Emp_Info2.grid(row=2, column=1)

lbl_received_Date =                 Label(FRAM_BID_Emp_Info2, font=('arial', 20, 'bold'), text="Received_Date",              fg="black", bd=5).grid(row=7, column=0, sticky=W)
lbl_closing_Date =                  Label(FRAM_BID_Emp_Info2, font=('arial', 20, 'bold'), text="Closing_Date",               fg="black", bd=5).grid(row=8, column=0, sticky=W)
lbl_execution_Time =                Label(FRAM_BID_Emp_Info2, font=('arial', 20, 'bold'), text="Execution_Time",             fg="black", bd=5).grid(row=9, column=0, sticky=W)
lbl_evaluation_Completion_date =    Label(FRAM_BID_Emp_Info2, font=('arial', 20, 'bold'), text="Evaluation date", fg="black", bd=5).grid(row=10, column=0, sticky=W)
lbl_received_Date =                 Entry(FRAM_BID_Emp_Info2, font=('arial', 20, 'bold'), textvariable=Received_Date,              fg="black", bd=5).grid(row=7, column=1, sticky=W)
lbl_closing_Date =                  Entry(FRAM_BID_Emp_Info2, font=('arial', 20, 'bold'), textvariable=Closing_Date,               fg="black", bd=5).grid(row=8, column=1, sticky=W)
lbl_execution_Time =                Entry(FRAM_BID_Emp_Info2, font=('arial', 20, 'bold'), textvariable=Execution_Time,             fg="black", bd=5).grid(row=9, column=1, sticky=W)
lbl_evaluation_Completion_date =    Entry(FRAM_BID_Emp_Info2, font=('arial', 20, 'bold'), textvariable=Evaluation_Completion_date, fg="black", bd=5).grid(row=10, column=1, sticky=W)

FRAM_BID_Emp_Info3 = Frame(BID_MainFrame, bd=16, width=100, height=80, relief=RIDGE)
FRAM_BID_Emp_Info3.grid(row=1, column=1)

lbl_standerd =            Label(FRAM_BID_Emp_Info3, font=('arial', 20, 'bold'), text="Standerd",         fg="black", bd=5).grid(row=11, column=0, sticky=W)
lbl_tender_documents =    Label(FRAM_BID_Emp_Info3, font=('arial', 20, 'bold'), text="Tender_doc.", fg="black", bd=5).grid(row=12, column=0, sticky=W)
lbl_standerd =            Entry(FRAM_BID_Emp_Info3, font=('arial', 20, 'bold'), textvariable=Standerd,         fg="black", bd=5).grid(row=11, column=1, sticky=W)
lbl_tender_documents =    Entry(FRAM_BID_Emp_Info3, font=('arial', 20, 'bold'), textvariable=Tender_documents, fg="black", bd=5).grid(row=12, column=1, sticky=W)

FRAM_BID_Emp_Info4 = Frame(BID_MainFrame, bd=16, width=100, height=80, relief=RIDGE)
FRAM_BID_Emp_Info4.grid(row=3, column=0)

lbl_SOW = Label(FRAM_BID_Emp_Info4, font=('arial', 20, 'bold'), text="SOW",       fg="black", bd=5).grid(row=7, column=0, sticky=W)
ent_SOW = Listbox(FRAM_BID_Emp_Info4, font=('arial', 20, 'bold'),       fg="black", bd=5).grid(row=7, column=1, sticky=W)


BID.mainloop()

