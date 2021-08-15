from tkinter import *
import tkinter.messagebox
import time
import datetime
import tempfile, os
import self as self
from tkinter import filedialog
import PyPDF2

1 - MOUNT:PAD;
2 - KVA RATING:1500 KVA;
3 - PHASE:3 PH;
4 - APPLICATION PRIMARY VOLT:34500 V AC;
5 - ACTUAL PRIMARY VOLT:34.5K V AC;
6 - SECONDARY VOLT:4160/480 V AC;
7 - FREQUENCY:60 HZ;
8 - PRIMARY BIL RATING:150 KV;
9 - SECONDARY BIL RATINGS:30 KV;
10 - VECTOR GROUP:YYYN0;
11 - PRIMARY BUSHINGS:(3) LOAD BREAK BUSHING INSERT;
12 - SECONDARY BUSHINGS:(3) LOAD BREAK BUSHING INSERT FOR 4160 V, (4) ENCLOSED 4-HOLES SPADE TERMINATIONS FOR 480 V;
13 - PRIMARY CONNECTIONS:LOADBREAK ELBOW TERMINATION;
14 - SECONDARY CONNECTIONS:LOAD BREAK BUSHING INSERT (FOR 4160 V),ENCLOSED SPADE TERMINALS;
15 - STANDARD/SPECIFICATION:51-SMSS-6;
16 - ADDITIONAL DATA:RADIAL FEED, SAMPLE SER NO TBT 7525-0102
17 - WESTINGHOUSE (FM):P/N#RSL/34500 V
18 - APPLICATOIN:INSTALLED AT 31CC IN JUBAIL INDUSTRIAL CITY IN MDNOD NORTH AREA.

1 = BREAKER: CIRCUIT GAS
2 = AMPERAGE: 2500 A;
3 = CONNECTION: DRAWABLE;
4 = INTERRUPTING CAPACITY:31.5 KA;
5 = KV RATING: 33 KV;
6 = PHASE:3 PHASE;
7 = STANDARD/SPECIFICATION:IEC 56;
8 = ADDITIONAL DATA:ITEM ADDITIONAL DESCRIPTION: ACCESSORIES: SYSTEM PARENT EQUIPMENT INFORMATION:
9 = SCHNEIDER (LM/FM):V3SE0118021
    
1 = SWITCHGEAR:METAL CLAD
2 = CONFIGURATION: RMU,OUTDOOR,2 LBS PLUS 1 CB TEE-OFF;
3 = INSULATION:SF6;
4 = NOMINAL VOLTAGE:13.8 KV;
5 = PHASE:3;
6 = FREQUENCY:60 HZ;
7 = CONTINUOUS CURRENT:630/400;
8 = INTERRUPTING CAPACITY:20 KA;
9 = BIL RATING:95;
10  = VOLTAGE CLASS:15 KV;
11 =  CONNECTIONS:BOLT LUG;
12 =  MOUNTING:PAD;
13 = STANDARD/SPECIFICATION:IEC 62271,01-SDMS-01, 32-SDMS-01;
14 = ADDITIONAL DATA:
15 = Note to vendor's:
    
BID = Tk()
BID.geometry("1500x1000+0+0")
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
Transformers = ["Power transformer","Startup transformer","Medium voltage transformer"]
Breakers = ["ACB","MCB","MCCB"]


Distribution_Panel = ["Main distribution panels","Sub-distribution panels"]

Medium_Voltage = ["Switch gear","Ring Main units"]

Cable = ["Medium voltage cables","Low voltage cables"]

SCADA_System = ["UPS","RTU","New Readings","Battery charge","Battery bank"]

Montring_System = ["PDM","DGA","WAMS"]


lbl_work_Order =    Label(FRAM_BID_Emp_Info, font=('arial', 20, 'bold'), text="Work_Order",   fg="black", bd=5).grid(row=1, column=0, sticky=W)
lbl_rfq_no =        Label(FRAM_BID_Emp_Info, font=('arial', 20, 'bold'), text="RFQ_No",       fg="black", bd=5).grid(row=2, column=0, sticky=W)
lbl_work_Order =    Entry(FRAM_BID_Emp_Info, font=('arial', 22, 'bold'), textvariable=Work_Order,   fg="black", bd=5).grid(row=1, column=1, sticky=W)
lbl_rfq_no =        Entry(FRAM_BID_Emp_Info, font=('arial', 22, 'bold'), textvariable=RFQ_No,       fg="black", bd=5).grid(row=2, column=1, sticky=W)

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
lbl_standerd =            Entry(FRAM_BID_Emp_Info3, font=('arial', 23, 'bold'), textvariable=Standerd,         fg="black", bd=5).grid(row=11, column=1, sticky=W)
lbl_tender_documents =    Entry(FRAM_BID_Emp_Info3, font=('arial', 23, 'bold'), textvariable=Tender_documents, fg="black", bd=5).grid(row=12, column=1, sticky=W)

#FRAM_BID_Emp_Info4 = Frame(BID_MainFrame, bd=16, width=100, height=80, relief=RIDGE)
#FRAM_BID_Emp_Info4.grid(row=3, column=0)

#lbl_SOW = Label(FRAM_BID_Emp_Info4, font=('arial', 20, 'bold'), text="SOW",       fg="black", bd=5).grid(row=7, column=0, sticky=W)
#ent_SOW = Listbox(FRAM_BID_Emp_Info4, font=('arial', 20, 'bold'),       fg="black", bd=5).grid(row=7, column=1, sticky=W)

BID_MainFrame1 = Frame(BID, bd=16, width=1350, height=600, relief=RIDGE)
BID_MainFrame1.grid(row=1, column=0)

lbl_SOW = Label(BID_MainFrame1, font=('arial', 20, 'bold'), text="Full tender",       fg="black", bd=5).grid(row=7, column=0, sticky=W)
ent_SOW = Text(BID_MainFrame1, font=('arial', 20, 'bold'), width= 63,height=15, fg="black", bd=5)
ent_SOW.grid(row=7, column=1, sticky=W)

def insert_sow():

    open_file = filedialog.askopenfilename()
    if open_file:
        pdf_file = PyPDF2.PdfFileReader(open_file)
        page = pdf_file.getPage(0)
        page_stuff = page.extractText()
        ent_SOW.insert(1.0,page_stuff)

BID_MainFrame2 = Frame(BID, bd=16, width=1350, height=600, relief=RIDGE)
BID_MainFrame2.grid(row=2, column=0)

btn = Button(BID_MainFrame2,bd = 8 , pady = 8 , fg = "black", font = ('arial',16, 'bold'), width =11, text = "insert_sow", bg = "white",command = insert_sow)
btn.grid(row = 0 , column = 0)


BID.mainloop()
