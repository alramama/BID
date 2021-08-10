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

typeOfworks = ["Construct" , "Supply" ,"installation","Testing","commissioning","Add","Preventive maintenance","Corrective maintenance","Maintenance","replace","check","Upgrade"]

Equipment = ["Generators","Transformers","Distribution_Panel","Medium voltage","Breakers","Cable","SCADA_System"]

Generators = ["Backup generators","prime generators","Mobil Generator"]
    KVA = Label(bid, text = "KVA").pack()
    V   = Label(bid, text = "V").pack()
    Phase =Label(bid, text = "Phase").pack()
    Hz = Label(bid, text = "Hz").pack()
    Sound_proof_mounted =Label(bid, text = "Sound_proof_mounted").pack()
    Indoor_outdoor =Label(bid, text = "Indoor_outdoor").pack()
    Water_cooled =Label(bid, text = "Water_cooled").pack()
    Floor_type =Label(bid, text = "Floor_type").pack()

Transformers = ["Power transformer","Startup transformer","Medium voltage transformer"]
    Rating = 
    Phase = 
    Hz = 
    Volts = 
    (No lode) = 
    Amps HV = 
    Amps LV = 
    Vector Group = 
    Impedance = 
    Max.Ambient Temp.(outdoor) = 
    Cooling type = 
    Floor type = 
Breakers = ["ACB","MCB","MCCB"]


Distribution_Panel = ["Main distribution panels","Sub-distribution panels"]

Medium_Voltage = ["Switch gear","Ring Main units"]

Cable = ["Medium voltage cables","Low voltage cables"]

SCADA_System = ["UPS","RTU","New Readings","Battery charge","Battery bank"]

Montring_System = ["PDM","DGA","WAMS"]


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

