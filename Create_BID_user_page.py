from tkinter import *
import tkinter.messagebox
import time
import datetime
import tempfile, os

BID = Tk()
BID.geometry("800x1000+0+0")
BID.title("BID INFORMATION")
Bid_Type = [Sales,Service,Contracts]
Customer = [Gov.,SEC,ARAMCO,SABIC,SWCC,NWC]

#===================================================================BIDTopFram=================================================
BID_Page_title = Frame(BID, bd=16, width=1350, height=60, relief=RAISED)
BID_Page_title.pack(side=TOP)
BID_Page_Name = Label(BID_Page_title,font=('arial',40, 'bold'),text = "BID INFORMATION", bd=10)
BID_Page_Name.pack()
#===================================================================BIDBOTTOMFram=================================================
BID_MainFrame = Frame(BID, bd=16, width=1350, height=600, relief=RAISED)
BID_MainFrame.pack(side=BOTTOM)

BID_information_LEFT = Frame(BID_MainFrame, bd=16, width=700, height=600, relief=RAISED)
BID_information_LEFT.pack(side=LEFT)
BID_information_LEFT = Frame(BID_MainFrame, bd=16, width=700, height=600, relief=RAISED)
BID_information_LEFT.pack(side=LEFT)
BID_information_LEFT = Frame(BID_MainFrame, bd=16, width=700, height=600, relief=RAISED)
BID_information_LEFT.pack(side=LEFT)



BID_information_RIGHT = Frame(BID_MainFrame, bd=16, width=700, height=600, relief=RAISED)
BID_information_RIGHT.pack(side=RIGHT)


#===================================================================Lable&Entry=================================================

lbl_WorkOrder =       Label(BID_information, font=('arial', 16, 'bold'), text="NAME",              fg="black", bd=20).grid(row=0, column=0)
lbl_ENG =             Label(BID_information, font=('arial', 16, 'bold'), text="NAME",              fg="black", bd=20).grid(row=0, column=0)

lbl_Customer =         Label(BID_information, font=('arial', 16, 'bold'), text="Execution_Time",    fg="black", bd=20).grid(row=12column=0)
lbl_RFQ_No =           Label(BID_information, font=('arial', 16, 'bold'), text="RFQ_No",            fg="black", bd=20).grid(row=1, column=0)
lbl_Tender_Name =      Label(BID_information, font=('arial', 16, 'bold'), text="Tender_Name",       fg="black", bd=20).grid(row=2, column=0)
lbl_Bid_Type =         Label(BID_information, font=('arial', 16, 'bold'), text="Bid_Type",          fg="black", bd=20).grid(row=4, column=0)

lbl_Received_Date =    Label(BID_information, font=('arial', 16, 'bold'), text="Received_Date",     fg="black", bd=20).grid(row=5, column=0)
lbl_Closing_Date =     Label(BID_information, font=('arial', 16, 'bold'), text="Closing_Date",      fg="black", bd=20).grid(row=6, column=0)
lbl_EvaluationDate =   Label(BID_information, font=('arial', 16, 'bold'), text="EvaluationDate",    fg="black", bd=20).grid(row=7, column=0)
lbl_Execution_Time =   Label(BID_information, font=('arial', 16, 'bold'), text="Execution_Time",    fg="black", bd=20).grid(row=11,column=0)

lbl_As_per_Standerd =  Label(BID_information, font=('arial', 16, 'bold'), text="As_per_Standerd",   fg="black", bd=20).grid(row=9, column=0)
lbl_Tender_documents = Label(BID_information, font=('arial', 16, 'bold'), text="Tender_documents",  fg="black", bd=20).grid(row=10,column=0)
lbl_Tender_Breakdowen= Label(BID_information, font=('arial', 16, 'bold'), text="Tender_documents",  fg="black", bd=20).grid(row=10,column=0)

lbl_Site_Location =    Label(BID_information, font=('arial', 16, 'bold'), text="Site_Location",     fg="black", bd=20).grid(row=8, column=0)



BID.mainloop()

"""EntName =             Entry(BID_information, font=('arial', 16, 'bold'), fg="black", bd=20).grid(row=0,column=1)

EntRFQ_No =           Entry(BID_information, font=('arial', 16, 'bold'), fg="black", bd=20).grid(row=1,column=1)
EntTender_Name =      Entry(BID_information, font=('arial', 16, 'bold'), fg="black", bd=20).grid(row=2,column=1)
EntTender_NO =        Entry(BID_information, font=('arial', 16, 'bold'), fg="black", bd=20).grid(row=3,column=1)
EntBid_Type =         Entry(BID_information, font=('arial', 16, 'bold'), fg="black", bd=20).grid(row=4,column=1)

EntReceived_Date =    Entry(BID_information, font=('arial', 16, 'bold'), fg="black", bd=20).grid(row=5,column=1)
EntClosing_Date =     Entry(BID_information, font=('arial', 16, 'bold'), fg="black", bd=20).grid(row=6,column=1)
EntEvaluationDate =   Entry(BID_information, font=('arial', 16, 'bold'), fg="black", bd=20).grid(row=7,column=1)
EntExecution_Time =   Entry(BID_information, font=('arial', 16, 'bold'), fg="black", bd=20).grid(row=11,column=1)

EntSite_Location =    Entry(BID_information, font=('arial', 16, 'bold'), fg="black", bd=20).grid(row=8,column=1)
EntAs_per_Standerd  = Entry(BID_information, font=('arial', 16, 'bold'), fg="black", bd=20).grid(row=9,column=1)
EntTender_documents = Entry(BID_information, font=('arial', 16, 'bold'), fg="black", bd=20).grid(row=10,column=1)
EntCustomer =         Entry(BID_information, font=('arial', 16, 'bold'), fg="black", bd=20).grid(row=12column=1)"""

