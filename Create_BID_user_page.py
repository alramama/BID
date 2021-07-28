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
#=====================================================mysql.connector===============================================
import mysql.connector
conn = mysql.connector.connect(user = 'root',password= "", host = 'localhost',database = 'tender')
print(conn)
conn.close()
#=====================================================Mysql.Create table===============================================
import mysql.connector
conn = mysql.connector.connect(user = 'root',password= "12345678", host = 'localhost',database = 'tender')
mycursor = conn.cursor()
mycursor.execute("CREATE TABLE BID("
                 "Name VARCHAR(255),"
                 "Postion VARCHAR(255),"
                 "Nationlty VARCHAR(255),"
                 "Customer VARCHAR(255),"
                 "RFQ_No VARCHAR(255),"
                 "Tender_Name VARCHAR(255),"
                 "Bid_Type VARCHAR(255),"
                 "EvaluationDate VARCHAR(255),"
                 "Execution_Time VARCHAR(255),"
                 "As_per_Standerd VARCHAR(255))")
conn.close()
#====================================================================INSERT
def insert():
    sqlcon = mysql.connector.connect(host="localhost", user="root", password="12345678", database="naizak")
    cursor = sqlcon.cursor()
    cursor.execute("INSERT INTO nps_new VALUES (%s, %s, %s,%s,%s)",(ID.get(), NAME.get(), Eqamano.get(), BirthDay.get(), BloodGroup.get(),))
    sqlcon.commit()
    sqlcon.close()


conn.close()
#=====================================================Update
        def Update():
            sqlcon = mysql.connector.connect(host="localhost", user="root", password="12345678", database="naizak")
            cursor = sqlcon.cursor()
            cursor.execute("update nps_new set  NAME=%s, Eqamano=%s,Birthday=%s,BloodGroup=%s where ID=%s "
                           ,(NAME.get(),Eqamano.get(),BirthDay.get(),BloodGroup.get(),ID.get()))
            sqlcon.commit()
#======================================================search
        def search():
            sqlcon = mysql.connector.connect(host="localhost", user="root", password="12345678", database="naizak")
            cursor = sqlcon.cursor()
            cursor.execute("select * from nps_new where ID='%s'" %ID.get())

            row = cursor.fetchall()

            ID.set(row[0])
            NAME.set(row[1])
            Eqamano.set(row[2])
            BirthDay.set(row[3])
            BloodGroup.set(row[4])

            sqlcon.commit()
            sqlcon.close()
#=====================================================Combobox
NAME = []
Postion= []
Nationlty= []
Customer= []
RFQ_No= []
Tender_Name = []
Bid_Type = []
EvaluationDate = [] 
Execution_Time = []
As_per_Standerd = []
#===================================================================BIDTopFram=================================================
#BID_Page_title = Frame(BID, bd=16, width=1350, height=60, relief=RAISED)
#BID_Page_title.pack(side=TOP)
#BID_Page_Name = Label(BID_Page_title,font=('arial',40, 'bold'),text = "BID INFORMATION", bd=10)
#BID_Page_Name.pack()
#===================================================================BIDBOTTOMFram=================================================
BID_MainFrame = Frame(BID, bd=16, width=1350, height=600, relief=RAISED)
BID_MainFrame.grid(row=0, column=0)



#===================================================================Bid_Cost_Eng.=================================================
FRAM_Bid_Cost_Eng = Frame(BID_MainFrame, bd=16, width=700, height=600, relief=RIDGE )
FRAM_Bid_Cost_Eng.grid(row=0, column=0)

lbl_WorkOrder =             Label(FRAM_Bid_Cost_Eng, font=('arial', 6, 'bold'),text="WorkOrder",         fg="black", bd=5).grid(row=1, column=0)
lbl_ENG =                   Label(FRAM_Bid_Cost_Eng, font=('arial', 6, 'bold'),text="NAME",              fg="black", bd=5).grid(row=2, column=0)
lbl_Postion =               Label(FRAM_Bid_Cost_Eng, font=('arial', 6, 'bold'),text="Postion",           fg="black", bd=5).grid(row=3, column=0)
lbl_Nationlty =             Label(FRAM_Bid_Cost_Eng, font=('arial', 6, 'bold'),text="Nationlty",         fg="black", bd=5).grid(row=4, column=0)

ENT_WorkOrder =             Entry(FRAM_Bid_Cost_Eng, font=('arial', 6, 'bold'),text="WorkOrder",         fg="black", bd=5).grid(row=1, column=1)
ENT_ENG =                   Entry(FRAM_Bid_Cost_Eng, font=('arial', 6, 'bold'),text="NAME",              fg="black", bd=5).grid(row=2, column=1)
ENT_Postion =               Entry(FRAM_Bid_Cost_Eng, font=('arial', 6, 'bold'),text="Postion",           fg="black", bd=5).grid(row=3, column=1)
ENT_Nationlty =             Entry(FRAM_Bid_Cost_Eng, font=('arial', 6, 'bold'),text="Nationlty",         fg="black", bd=5).grid(row=4, column=1)


      #===================================================================Bid_information===========================================
FRAM_Bid_information = Frame(BID_MainFrame, bd=16, width=700, height=600, relief=RIDGE )
FRAM_Bid_information.grid(row=0, column=1)
lbl_Customer =         Label(FRAM_Bid_information, font=('arial', 6, 'bold'), text="Customer",            fg="black", bd=5).grid(row=1,column=0)
lbl_RFQ_No =           Label(FRAM_Bid_information, font=('arial', 6, 'bold'), text="RFQ_No",              fg="black", bd=5).grid(row=2, column=0)
lbl_Tender_Name =      Label(FRAM_Bid_information, font=('arial', 6, 'bold'), text="Tender_Name",         fg="black", bd=5).grid(row=3, column=0)
lbl_Bid_Type =         Label(FRAM_Bid_information, font=('arial', 6, 'bold'), text="Bid_Type",            fg="black", bd=5).grid(row=4, column=0)

ENT_Customer =         Entry(FRAM_Bid_information, font=('arial', 6, 'bold'),                             fg="black", bd=5).grid(row=1,column= 1)
ENT_RFQ_No =           Entry(FRAM_Bid_information, font=('arial', 6, 'bold'),                             fg="black", bd=5).grid(row=2, column=1)
ENT_Tender_Name =      Entry(FRAM_Bid_information, font=('arial', 6, 'bold'),                             fg="black", bd=5).grid(row=3, column=1)
ENT_Bid_Type =         Entry(FRAM_Bid_information, font=('arial', 6, 'bold'),                             fg="black", bd=5).grid(row=4, column=1)

lbl_Received_Date =    Label(FRAM_Bid_information, font=('arial', 6, 'bold'), text="Received_Date",     fg="black", bd=5).grid(row=1, column=2)
lbl_Closing_Date =     Label(FRAM_Bid_information, font=('arial', 6, 'bold'), text="Closing_Date",      fg="black", bd=5).grid(row=2, column=2)
lbl_EvaluationDate =   Label(FRAM_Bid_information, font=('arial', 6, 'bold'), text="EvaluationDate",    fg="black", bd=5).grid(row=3, column=2)
lbl_Execution_Time =   Label(FRAM_Bid_information, font=('arial', 6, 'bold'), text="Execution_Time",    fg="black", bd=5).grid(row=4,column=2)

ENT_Received_Date =    Entry(FRAM_Bid_information, font=('arial', 6, 'bold'), text="Received_Date",     fg="black", bd=5).grid(row=1, column=3)
ENT_Closing_Date =     Entry(FRAM_Bid_information, font=('arial', 6, 'bold'), text="Closing_Date",      fg="black", bd=5).grid(row=2, column=3)
ENT_EvaluationDate =   Entry(FRAM_Bid_information, font=('arial', 6, 'bold'), text="EvaluationDate",    fg="black", bd=5).grid(row=3, column=3)
ENT_Execution_Time =   Entry(FRAM_Bid_information, font=('arial', 6, 'bold'), text="Execution_Time",    fg="black", bd=5).grid(row=4,column=3)

lbl_As_per_Standerd =  Label(FRAM_Bid_information, font=('arial', 6, 'bold'), text="As_per_Standerd",   fg="black", bd=5).grid(row=1,column=4)
lbl_Tender_documents = Label(FRAM_Bid_information, font=('arial', 6, 'bold'), text="Tender_documents",  fg="black", bd=5).grid(row=2,column=4)
lbl_Tender_Breakdowen= Label(FRAM_Bid_information, font=('arial', 6, 'bold'), text="Tender_Breakdowen",  fg="black", bd=5).grid(row=3,column=4)
lbl_Tender_Breakdowen= Label(FRAM_Bid_information, font=('arial', 6, 'bold'), text="Tender_documents",  fg="black", bd=5).grid(row=4,column=4)

ENT_As_per_Standerd =  Entry(FRAM_Bid_information, font=('arial', 6, 'bold'), text="As_per_Standerd",   fg="black", bd=5).grid(row=1,column=5)
ENT_Tender_documents = Entry(FRAM_Bid_information, font=('arial', 6, 'bold'), text="Tender_documents",  fg="black", bd=5).grid(row=2,column=5)
ENT_Tender_Breakdowen= Entry(FRAM_Bid_information, font=('arial', 6, 'bold'), text="Tender_documents",  fg="black", bd=5).grid(row=3,column=5)
ENT_Tender_Breakdowen= Entry(FRAM_Bid_information, font=('arial', 6, 'bold'), text="Tender_documents",  fg="black", bd=5).grid(row=4,column=5)

BID.mainloop()


