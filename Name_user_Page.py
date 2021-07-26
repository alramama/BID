from tkinter import *
import tkinter.messagebox
import time
import datetime
import tempfile, os

Name = Tk()
Name.geometry("800x1000+0+0")
Name.title("NAME INFORMATION")
#Name_Type = ["Sales","Service","Contracts"]
#Customer = ["Gov","SEC","ARAMCO","SABIC","SWCC","NWC"]

#===================================================================NAMETopFram=================================================
#NAME_Page_title = Frame(NAME, bd=16, width=1350, height=60, relief=RAISED)
#NAME_Page_title.pack(side=TOP)
#NAME_Page_Name = Label(NAME_Page_title,font=('arial',40, 'bold'),text = "NAME INFORMATION", bd=10)
#NAME_Page_Name.pack()
#===================================================================NAMEBOTTOMFram=================================================
NAME_MainFrame =             Frame(NAME, bd=16, width=1350, height=600, relief=RAISED)
NAME_MainFrame.grid(row=0, column=0)



#===================================================================Name_Cost_Eng.=================================================
FRAM_Name_Emp_Info =         Frame(NAME_MainFrame, bd=16, width=700, height=600, relief=RAISED)
FRAM_Name_Emp_Info.grid(row=0, column=0)
lbl_ID =                     Label(FRAM_Name_Emp_Info, font=('arial', 6, 'bold'),text="ID",                  fg="black", bd=20).grid(row=1, column=0)
lbl_Name =                   Label(FRAM_Name_Emp_Info, font=('arial', 6, 'bold'),text="NAME",                fg="black", bd=20).grid(row=2, column=0)
lbl_Job_Title =              Label(FRAM_Name_Emp_Info, font=('arial', 6, 'bold'),text="Job_Title",           fg="black", bd=20).grid(row=3, column=0)
lbl_Qualification =          Label(FRAM_Name_Emp_Info, font=('arial', 6, 'bold'),text="Qualification",       fg="black", bd=20).grid(row=4, column=0)


      #===================================================================Name_information===========================================
FRAM_Name_information =     Frame(NAME_MainFrame, bd=16, width=700, height=600, relief=RAISED)
FRAM_Name_information.grid(row=0, column=1)
lbl_Customer =              Label(FRAM_Name_information, font=('arial', 6, 'bold'), text="Customer",         fg="black", bd=20).grid(row=1,column=0)
lbl_RFQ_No =                Label(FRAM_Name_information, font=('arial', 6, 'bold'), text="RFQ_No",           fg="black", bd=20).grid(row=2, column=0)
lbl_Tender_Name =           Label(FRAM_Name_information, font=('arial', 6, 'bold'), text="Tender_Name",      fg="black", bd=20).grid(row=3, column=0)
lbl_Name_Type =             Label(FRAM_Name_information, font=('arial', 6, 'bold'), text="Name_Type",        fg="black", bd=20).grid(row=4, column=0)


            #===================================================================Name_Date=======================================
FRAM_Name_Emp_Salary =      Frame(NAME_MainFrame, bd=16, width=700, height=600, relief=RAISED)
FRAM_Name_Emp_Salary.grid(row=1, column=0)
lbl_Salary =                Label(FRAM_Name_Emp_Salary, font=('arial', 6, 'bold'), text="Salary",                  fg="black", bd=5).grid(row=1, column=0)
lbl_Housing_allowance =     Label(FRAM_Name_Emp_Salary, font=('arial', 6, 'bold'), text="Housing_allowance",       fg="black", bd=5).grid(row=2, column=0)
lbl_Trans_allowance =       Label(FRAM_Name_Emp_Salary, font=('arial', 6, 'bold'), text="Trans_allowance",         fg="black", bd=5).grid(row=3, column=0)

             #===================================================================Name_Documnets====================================
FRAM_Name_Gov_Fees =        Frame(NAME_MainFrame, bd=16, width=700, height=600, relief=RAISED)
FRAM_Name_Gov_Fees.grid(row=1, column=1)

lbl_Health_Insurance =      Label(FRAM_Name_Gov_Fees, font=('arial', 6, 'bold'), text="Health_Insurance",   fg="black", bd=5).grid(row=1,column=0)
lbl_Annual_Tickets =        Label(FRAM_Name_Gov_Fees, font=('arial', 6, 'bold'), text="Annual_Tickets",     fg="black", bd=5).grid(row=2,column=0)
lbl_Phone Charge=           Label(FRAM_Name_Gov_Fees, font=('arial', 6, 'bold'), text="Phone Charge",       fg="black", bd=5).grid(row=3,column=0)
lbl_Work_license=           Label(FRAM_Name_Gov_Fees, font=('arial', 6, 'bold'), text="Work_license",       fg="black", bd=5).grid(row=4,column=0)
lbl_Residence_permit=       Label(FRAM_Name_Gov_Fees, font=('arial', 6, 'bold'), text="Residence_permit",   fg="black", bd=5).grid(row=4,column=0)
lbl_SCE=                    Label(FRAM_Name_Gov_Fees, font=('arial', 6, 'bold'), text="SCE",                fg="black", bd=5).grid(row=4,column=0)
lbl_GOSI=                   Label(FRAM_Name_Gov_Fees, font=('arial', 6, 'bold'), text="GOSI",               fg="black", bd=5).grid(row=4,column=0)



                  #===================================================================Location===================================
FRAM_Name_Location = Frame(NAME_MainFrame, bd=16, width=700, height=600, relief=RAISED)
FRAM_Name_Location.grid(row=1, column=2)
lbl_Site_Location =        Label(FRAM_Name_Location, font=('arial', 16, 'bold'), text="Site_Location",     fg="black", bd=20).grid(row=8, column=0)

NAME.mainloop()
