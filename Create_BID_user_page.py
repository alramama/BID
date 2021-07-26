from tkinter import *
import tkinter.messagebox
import time
import datetime
import tempfile, os

BID = Tk()
BID.geometry("800x1000+0+0")
BID.title("BID INFORMATION")
#Bid_Type = ["Sales","Service","Contracts"]
#Customer = ["Gov","SEC","ARAMCO","SABIC","SWCC","NWC"]

#===================================================================BIDTopFram=================================================
#BID_Page_title = Frame(BID, bd=16, width=1350, height=60, relief=RAISED)
#BID_Page_title.pack(side=TOP)
#BID_Page_Name = Label(BID_Page_title,font=('arial',40, 'bold'),text = "BID INFORMATION", bd=10)
#BID_Page_Name.pack()
#===================================================================BIDBOTTOMFram=================================================
BID_MainFrame = Frame(BID, bd=16, width=1350, height=600, relief=RAISED)
BID_MainFrame.grid(row=0, column=0)



#===================================================================Bid_Cost_Eng.=================================================
FRAM_Bid_Cost_Eng = Frame(BID_MainFrame, bd=16, width=700, height=600, relief=RAISED)
FRAM_Bid_Cost_Eng.grid(row=0, column=0)
lbl_WorkOrder =             Label(FRAM_Bid_Cost_Eng, font=('arial', 6, 'bold'),text="WorkOrder",         fg="black", bd=20).grid(row=1, column=0)
lbl_ENG =                   Label(FRAM_Bid_Cost_Eng, font=('arial', 6, 'bold'),text="NAME",              fg="black", bd=20).grid(row=2, column=0)
lbl_Postion =               Label(FRAM_Bid_Cost_Eng, font=('arial', 6, 'bold'),text="Postion",           fg="black", bd=20).grid(row=3, column=0)
lbl_Nationlty =             Label(FRAM_Bid_Cost_Eng, font=('arial', 6, 'bold'),text="Nationlty",         fg="black", bd=20).grid(row=4, column=0)

ENT_WorkOrder =             Entry(FRAM_Bid_Cost_Eng, font=('arial', 6, 'bold'),text="WorkOrder",         fg="black", bd=20).grid(row=1, column=1)
ENT_ENG =                   Entry(FRAM_Bid_Cost_Eng, font=('arial', 6, 'bold'),text="NAME",              fg="black", bd=20).grid(row=2, column=1)
ENT_Postion =               Entry(FRAM_Bid_Cost_Eng, font=('arial', 6, 'bold'),text="Postion",           fg="black", bd=20).grid(row=3, column=1)
ENT_Nationlty =             Entry(FRAM_Bid_Cost_Eng, font=('arial', 6, 'bold'),text="Nationlty",         fg="black", bd=20).grid(row=4, column=1)


      #===================================================================Bid_information===========================================
FRAM_Bid_information = Frame(BID_MainFrame, bd=16, width=700, height=600, relief=RAISED)
FRAM_Bid_information.grid(row=0, column=1)
lbl_Customer =         Label(FRAM_Bid_information, font=('arial', 6, 'bold'), text="Customer",            fg="black", bd=20).grid(row=1,column=0)
lbl_RFQ_No =           Label(FRAM_Bid_information, font=('arial', 6, 'bold'), text="RFQ_No",              fg="black", bd=20).grid(row=2, column=0)
lbl_Tender_Name =      Label(FRAM_Bid_information, font=('arial', 6, 'bold'), text="Tender_Name",         fg="black", bd=20).grid(row=3, column=0)
lbl_Bid_Type =         Label(FRAM_Bid_information, font=('arial', 6, 'bold'), text="Bid_Type",            fg="black", bd=20).grid(row=4, column=0)

ENT_Customer =         Entry(FRAM_Bid_information, font=('arial', 6, 'bold'),                             fg="black", bd=20).grid(row=1,column= 1)
ENT_RFQ_No =           Entry(FRAM_Bid_information, font=('arial', 6, 'bold'),                             fg="black", bd=20).grid(row=2, column=1)
ENT_Tender_Name =      Entry(FRAM_Bid_information, font=('arial', 6, 'bold'),                             fg="black", bd=20).grid(row=3, column=1)
ENT_Bid_Type =         Entry(FRAM_Bid_information, font=('arial', 6, 'bold'),                             fg="black", bd=20).grid(row=4, column=1)

            #===================================================================Bid_Date=======================================
FRAM_Bid_Date = Frame(BID_MainFrame, bd=16, width=700, height=600, relief=RAISED)
FRAM_Bid_Date.grid(row=1, column=0)
lbl_Received_Date =    Label(FRAM_Bid_Date, font=('arial', 6, 'bold'), text="Received_Date",     fg="black", bd=5).grid(row=1, column=0)
lbl_Closing_Date =     Label(FRAM_Bid_Date, font=('arial', 6, 'bold'), text="Closing_Date",      fg="black", bd=5).grid(row=2, column=0)
lbl_EvaluationDate =   Label(FRAM_Bid_Date, font=('arial', 6, 'bold'), text="EvaluationDate",    fg="black", bd=5).grid(row=3, column=0)
lbl_Execution_Time =   Label(FRAM_Bid_Date, font=('arial', 6, 'bold'), text="Execution_Time",    fg="black", bd=5).grid(row=4,column=0)

ENT_Received_Date =    Entry(FRAM_Bid_Date, font=('arial', 6, 'bold'), text="Received_Date",     fg="black", bd=5).grid(row=1, column=1)
ENT_Closing_Date =     Entry(FRAM_Bid_Date, font=('arial', 6, 'bold'), text="Closing_Date",      fg="black", bd=5).grid(row=2, column=1)
ENT_EvaluationDate =   Entry(FRAM_Bid_Date, font=('arial', 6, 'bold'), text="EvaluationDate",    fg="black", bd=5).grid(row=3, column=1)
ENT_Execution_Time =   Entry(FRAM_Bid_Date, font=('arial', 6, 'bold'), text="Execution_Time",    fg="black", bd=5).grid(row=4,column=1)

             #===================================================================Bid_Documnets====================================
FRAM_Bid_Documnets = Frame(BID_MainFrame, bd=16, width=700, height=600, relief=RAISED)
FRAM_Bid_Documnets.grid(row=1, column=1)

lbl_As_per_Standerd =  Label(FRAM_Bid_Documnets, font=('arial', 6, 'bold'), text="As_per_Standerd",   fg="black", bd=5).grid(row=1,column=0)
lbl_Tender_documents = Label(FRAM_Bid_Documnets, font=('arial', 6, 'bold'), text="Tender_documents",  fg="black", bd=5).grid(row=2,column=0)
lbl_Tender_Breakdowen= Label(FRAM_Bid_Documnets, font=('arial', 6, 'bold'), text="Tender_Breakdowen",  fg="black", bd=5).grid(row=3,column=0)
lbl_Tender_Breakdowen= Label(FRAM_Bid_Documnets, font=('arial', 6, 'bold'), text="Tender_documents",  fg="black", bd=5).grid(row=4,column=0)

ENT_As_per_Standerd =  Entry(FRAM_Bid_Documnets, font=('arial', 6, 'bold'), text="As_per_Standerd",   fg="black", bd=5).grid(row=1,column=1)
ENT_Tender_documents = Entry(FRAM_Bid_Documnets, font=('arial', 6, 'bold'), text="Tender_documents",  fg="black", bd=5).grid(row=2,column=1)
ENT_Tender_Breakdowen= Entry(FRAM_Bid_Documnets, font=('arial', 6, 'bold'), text="Tender_documents",  fg="black", bd=5).grid(row=3,column=1)
ENT_Tender_Breakdowen= Entry(FRAM_Bid_Documnets, font=('arial', 6, 'bold'), text="Tender_documents",  fg="black", bd=5).grid(row=4,column=1)


                  #===================================================================Location===================================
FRAM_Bid_Location = Frame(BID_MainFrame, bd=16, width=700, height=600, relief=RAISED)
FRAM_Bid_Location.grid(row=1, column=2)
lbl_Site_Location =    Label(FRAM_Bid_Location, font=('arial', 16, 'bold'), text="Site_Location",     fg="black", bd=20).grid(row=8, column=0)

BID.mainloop()


