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
NAME_Page_title = Frame(Name, bd=16, width=1350, height=60, relief=RAISED)
NAME_Page_title.grid(row=0, column=0)
NAME_Page_Name = Label(NAME_Page_title,font=('arial',40, 'bold'),text = "NAME INFORMATION", bd=10)
NAME_Page_Name.grid(row=0, column=0)
#===================================================================NAMEBOTTOMFram=================================================
NAME_MainFrame =             Frame(Name, bd=16, width=1350, height=600, relief=RAISED)
NAME_MainFrame.grid(row=0, column=0)
#===================================================================FRAM_Name_Emp_Info.=================================================
FRAM_Name_Emp_Info =         Frame(NAME_MainFrame, bd=16, width=70, height=60, relief=RAISED)
FRAM_Name_Emp_Info.grid(row=0, column=0)
FRAM_Name_Emp_Info1 =         Frame(NAME_MainFrame, bd=16, width=70, height=60, relief=RAISED)
FRAM_Name_Emp_Info1.grid(row=0, column=0)
lbl_ID =                     Label(FRAM_Name_Emp_Info1, font=('arial', 6, 'bold'),text="ID",                  fg="black", bd=5).grid(row=1, column=0)
lbl_Name =                   Label(FRAM_Name_Emp_Info1, font=('arial', 6, 'bold'),text="NAME",                fg="black", bd=5).grid(row=2, column=0)
lbl_Job_Title =              Label(FRAM_Name_Emp_Info1, font=('arial', 6, 'bold'),text="Job Title",           fg="black", bd=5).grid(row=3, column=0)
lbl_Qualification =          Label(FRAM_Name_Emp_Info1, font=('arial', 6, 'bold'),text="Qualification",       fg="black", bd=5).grid(row=4, column=0)

lbl_ID =                     Entry(FRAM_Name_Emp_Info1, font=('arial', 6, 'bold'),text="ID",                  fg="black", bd=5).grid(row=1, column=1)
lbl_Name =                   Entry(FRAM_Name_Emp_Info1, font=('arial', 6, 'bold'),text="NAME",                fg="black", bd=5).grid(row=2, column=1)
lbl_Job_Title =              Entry(FRAM_Name_Emp_Info1, font=('arial', 6, 'bold'),text="Job Title",           fg="black", bd=5).grid(row=3, column=1)
lbl_Qualification =          Entry(FRAM_Name_Emp_Info1, font=('arial', 6, 'bold'),text="Qualification",       fg="black", bd=5).grid(row=4, column=1)

lbl_Salary =                Label(FRAM_Name_Emp_Info1, font=('arial', 6, 'bold'), text="Salary",                  fg="black", bd=5).grid(row=1, column=2)
lbl_Housing_allowance =     Label(FRAM_Name_Emp_Info1, font=('arial', 6, 'bold'), text="Housing allowance",       fg="black", bd=5).grid(row=2, column=2)
lbl_Trans_allowance =       Label(FRAM_Name_Emp_Info1, font=('arial', 6, 'bold'), text="Trans allowance",         fg="black", bd=5).grid(row=3, column=2)
lbl_Salary =                Entry(FRAM_Name_Emp_Info1, font=('arial', 6, 'bold'), text="Salary",                  fg="black", bd=5).grid(row=1, column=3)
lbl_Housing_allowance =     Entry(FRAM_Name_Emp_Info1, font=('arial', 6, 'bold'), text="Housing allowance",       fg="black", bd=5).grid(row=2, column=3)
lbl_Trans_allowance =       Entry(FRAM_Name_Emp_Info1, font=('arial', 6, 'bold'), text="Trans allowance",         fg="black", bd=5).grid(row=3, column=3)


#===================================================================FRAM_Name_Gov_Fees====================================
FRAM_Name_Gov_Fees =        Frame(NAME_MainFrame, bd=16, width=70, height=60, relief=RAISED)
FRAM_Name_Gov_Fees.grid(row=1, column=1)

FRAM_Name_Gov_Fees1 =        Frame(NAME_MainFrame, bd=16, width=70, height=60, relief=RAISED)
FRAM_Name_Gov_Fees1.grid(row=1, column=1)

lbl_Health_Insurance =      Label(FRAM_Name_Gov_Fees1, font=('arial', 6, 'bold'), text="Health Insurance",   fg="black", bd=5).grid(row=1,column=0)
lbl_Annual_Tickets =        Label(FRAM_Name_Gov_Fees1, font=('arial', 6, 'bold'), text="Annual Tickets",     fg="black", bd=5).grid(row=2,column=0)
lbl_Phone_Charge=           Label(FRAM_Name_Gov_Fees1, font=('arial', 6, 'bold'), text="Phone Charge",       fg="black", bd=5).grid(row=3,column=0)
lbl_Health_Insurance =      Entry(FRAM_Name_Gov_Fees1, font=('arial', 6, 'bold'), text="Health Insurance",   fg="black", bd=5).grid(row=1,column=1)
lbl_Annual_Tickets =        Entry(FRAM_Name_Gov_Fees1, font=('arial', 6, 'bold'), text="Annual Tickets",     fg="black", bd=5).grid(row=2,column=1)
lbl_Phone_Charge=           Entry(FRAM_Name_Gov_Fees1, font=('arial', 6, 'bold'), text="Phone Charge",       fg="black", bd=5).grid(row=3,column=1)

lbl_Work_license=           Label(FRAM_Name_Gov_Fees1, font=('arial', 6, 'bold'), text="Work license",       fg="black", bd=5).grid(row=1,column=2)
lbl_Residence_permit=       Label(FRAM_Name_Gov_Fees1, font=('arial', 6, 'bold'), text="Residence permit",   fg="black", bd=5).grid(row=2,column=2)
lbl_SCE=                    Label(FRAM_Name_Gov_Fees1, font=('arial', 6, 'bold'), text="SCE",                fg="black", bd=5).grid(row=3,column=2)
lbl_Work_license=           Entry(FRAM_Name_Gov_Fees1, font=('arial', 6, 'bold'), text="Work license",       fg="black", bd=5).grid(row=1,column=3)
lbl_Residence_permit=       Entry(FRAM_Name_Gov_Fees1, font=('arial', 6, 'bold'), text="Residence permit",   fg="black", bd=5).grid(row=2,column=3)
lbl_SCE=                    Entry(FRAM_Name_Gov_Fees1, font=('arial', 6, 'bold'), text="SCE",                fg="black", bd=5).grid(row=3,column=3)

lbl_GOSI=                   Label(FRAM_Name_Gov_Fees1, font=('arial', 6, 'bold'), text="GOSI",               fg="black", bd=5).grid(row=4,column=0)
lbl_GOSI=                   Entry(FRAM_Name_Gov_Fees1, font=('arial', 6, 'bold'), text="GOSI",               fg="black", bd=5).grid(row=4,column=1)



                  #===================================================================Location===================================

NAME.mainloop()
