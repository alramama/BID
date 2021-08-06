from tkinter import *
from tkinter import ttk

import tkinter.messagebox
import time
import datetime
import tempfile, os

Name = Tk()
Name.geometry("1500x500+0+0")
Name.title("NAME INFORMATION")
#Name_Type = ["Sales","Service","Contracts"]
#Customer = ["Gov","SEC","ARAMCO","SABIC","SWCC","NWC"]
#===================================================================NAMETopFram=================================================
NAME_Page_title = Frame(Name, bd=16, width=1000, height=60, relief=RIDGE)
NAME_Page_title.grid(row=0, column=0)
NAME_Page_Name = Label(NAME_Page_title,font=('arial',40, 'bold'),text = "NAME INFORMATION", bd=10)
NAME_Page_Name.grid(row=0, column=0)
#===================================================================NAMEBOTTOMFram=================================================
NAME_MainFrame =             Frame(Name, bd=16, width=1350, height=500, relief=RIDGE)
NAME_MainFrame.grid(row=1, column=0)

#===================================================================FRAM_Name_Emp_Info.=================================================
FRAM_Name_Emp_Info =         Frame(NAME_MainFrame, bd=16, width=70, height=60, relief=RIDGE)
FRAM_Name_Emp_Info.grid(row=1, column=0)
FRAM_Name_Emp_Info1 =         Frame(NAME_MainFrame, bd=16, width=70, height=60, relief=RIDGE)
FRAM_Name_Emp_Info1.grid(row=1, column=0)

lbl_ID =                     Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'),text="ID",                fg="black", bd=5).grid(row=1, column=0)
lbl_Name =                   Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'),text="NAME",              fg="black", bd=5).grid(row=2, column=0)
lbl_Job_Title =              Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'),text="Job Title",         fg="black", bd=5).grid(row=3, column=0)
lbl_Qualification =          Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'),text="Qualification",     fg="black", bd=5).grid(row=4, column=0)
lbl_Salary =                 Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Salary",           fg="black", bd=5).grid(row=5, column=0)
Are_you_Saudi =              Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Are_you_Saudi",    fg="black", bd=5).grid(row=6, column=0)
Are_you_marrid =             Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Are_you_marrid",   fg="black", bd=5).grid(row=7, column=0)


lbl_ID =                     Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'),text="ID",                fg="black", bd=5).grid(row=1, column=1)
lbl_Name =                   Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'),text="NAME",              fg="black", bd=5).grid(row=2, column=1)
lbl_Job_Title =              Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'),text="Job Title",         fg="black", bd=5).grid(row=3, column=1)
lbl_Qualification =          Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'),text="Qualification",     fg="black", bd=5).grid(row=4, column=1)
lbl_Salary =                 Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Salary",           fg="black", bd=5).grid(row=5, column=1)



def Nationalty(e):

    if Are_you_Saudi.get() == "Yes":

        lbl_Housing_allowance =     Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Housing allowance",    fg="black", bd=5).grid(row=1, column=2)
        lbl_Trans_allowance =       Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Trans allowance",      fg="black", bd=5).grid(row=2, column=2)
        lbl_Health_Insurance =      Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Health Insurance",     fg="black", bd=5).grid(row=3,column=2)
        lbl_Phone_Charge=           Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Phone Charge",         fg="black", bd=5).grid(row=4,column=2)
        lbl_SCE=                    Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="SCE",                  fg="black", bd=5).grid(row=5,column=2)
        lbl_GOSI=                   Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="GOSI",                 fg="black", bd=5).grid(row=6,column=2)

        lbl_Housing_allowance =     Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Housing allowance",    fg="black", bd=5).grid(row=1, column=3)
        lbl_Trans_allowance =       Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Trans allowance",      fg="black", bd=5).grid(row=2, column=3)
        lbl_Health_Insurance =      Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Health Insurance",     fg="black", bd=5).grid(row=3,column=3)
        lbl_Phone_Charge=           Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Phone Charge",         fg="black", bd=5).grid(row=4,column=3)
        lbl_SCE=                    Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="SCE",                  fg="black", bd=5).grid(row=5,column=3)
        lbl_GOSI=                   Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="GOSI",                 fg="black", bd=5).grid(row=6,column=3)

    else:
        lbl_Housing_allowance =     Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Housing allowance",    fg="black", bd=5).grid(row=1, column=2)
        lbl_Trans_allowance =       Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Trans allowance",      fg="black", bd=5).grid(row=2, column=2)
        lbl_Health_Insurance =      Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Health Insurance",     fg="black", bd=5).grid(row=3,column=2)
        lbl_Phone_Charge=           Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Phone Charge",         fg="black", bd=5).grid(row=4,column=2)
        lbl_SCE=                    Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="SCE",                  fg="black", bd=5).grid(row=5,column=2)
        lbl_GOSI=                   Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="GOSI",                 fg="black", bd=5).grid(row=6,column=2)

        lbl_Housing_allowance =     Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Housing allowance",    fg="black", bd=5).grid(row=1, column=3)
        lbl_Trans_allowance =       Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Trans allowance",      fg="black", bd=5).grid(row=2, column=3)
        lbl_Health_Insurance =      Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Health Insurance",     fg="black", bd=5).grid(row=3,column=3)
        lbl_Phone_Charge=           Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Phone Charge",         fg="black", bd=5).grid(row=4,column=3)
        lbl_SCE=                    Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="SCE",                  fg="black", bd=5).grid(row=5,column=3)
        lbl_GOSI=                   Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="GOSI",                 fg="black", bd=5).grid(row=6,column=3)

        lbl_Annual_Tickets =        Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Annual Tickets",     fg="black", bd=5).grid(row=7,column=2)
        lbl_Work_license=           Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Work license",       fg="black", bd=5).grid(row=8,column=2)
        lbl_Residence_permit=       Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Residence permit",   fg="black", bd=5).grid(row=9,column=2)

        lbl_Annual_Tickets =        Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Annual Tickets",     fg="black", bd=5).grid(row=7,column=3)
        lbl_Work_license=           Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Work license",       fg="black", bd=5).grid(row=8,column=3)
        lbl_Residence_permit=       Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Residence permit",   fg="black", bd=5).grid(row=9,column=3)



Are_you_Saudi = ttk.Combobox(FRAM_Name_Emp_Info1)
Are_you_Saudi['values'] = "Yes", "NO"
Are_you_Saudi.current()
Are_you_Saudi.bind('<<ComboboxSelected>>',Nationalty)
Are_you_Saudi.grid(row=6, column=1)

def marrid(e):
    if Are_you_Saudi.get() == "Yes":
        lbl_No_wife =        Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="No. Wife",      fg="black", bd=5).grid(row=10,column=2)
        lbl_No_Boy=           Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="No_Boy",       fg="black", bd=5).grid(row=11,column=2)
        lbl_No_Gril=       Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="No_Gril",         fg="black", bd=5).grid(row=12,column=2)

        lbl_Annual_Tickets =        Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Annual Tickets",     fg="black", bd=5).grid(row=10,column=3)
        lbl_Work_license=           Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Work license",       fg="black", bd=5).grid(row=11,column=3)
        lbl_Residence_permit=       Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Residence permit",   fg="black", bd=5).grid(row=12,column=3)



Are_you_marrid = ttk.Combobox(FRAM_Name_Emp_Info1)
Are_you_marrid['values'] = "Yes", "NO"
Are_you_marrid.current()
Are_you_marrid.bind('<<ComboboxSelected>>',marrid)
Are_you_marrid.grid(row=7, column=1)

Name.mainloop()

"""
ID = StringVar()
NAME = StringVar()
JobTitle = StringVar()
Nationality = StringVar()
Status_of_Social = StringVar()
Qualification = StringVar()
Salary = StringVar()
Housing_allowance = StringVar()
Trans_allowance = StringVar()
Health_Insurance = StringVar()
Annual_Tickets = StringVar()
Phone_Charge = StringVar()
Work_license = StringVar()
Residence_permit = StringVar()
SCE = StringVar()
GOSI = StringVar()
#====================================================
if Nationality not saudi:
  Annual_Tickets.insert(2000)
  Work_license
  Residence_permit
  GOSI
else:
  Annual_Tickets.insert(2000)
  Work_license
  Residence_permit
  GOSI
  

  
    

#=====================================================mysql.connector===============================================
import mysql.connector
conn = mysql.connector.connect(user = 'root',password= "", host = 'localhost',database = 'tender')
print(conn)
conn.close()
#=====================================================Mysql.Create table===============================================
import mysql.connector
conn = mysql.connector.connect(user = 'root',password= "12345678", host = 'localhost',database = 'tender')
mycursor = conn.cursor()
mycursor.execute("CREATE TABLE Name("
                 "ID VARCHAR(255),"
                 "NAME VARCHAR(255),"
                 "JobTitle VARCHAR(255),"
                 "Salary VARCHAR(255),"
                 "Housing_allowance VARCHAR(255),"
                 "Trans_allowance VARCHAR(255),"
                 "Health_Insurance VARCHAR(255),"
                 "Phone_Charge VARCHAR(255),"
                 "Work_license VARCHAR(255),"
                 "Residence_permit VARCHAR(255),
                "SCE VARCHAR(255),
                "GOSI VARCHAR(255))")
conn.close()
#====================================================================INSERT
def insert():
    sqlcon = mysql.connector.connect(host="localhost", user="root", password="12345678", database="naizak")
    cursor = sqlcon.cursor()
    cursor.execute("INSERT INTO BID VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                   (ID.get(),
                    NAME.get(),
                    Nationlty.get(),
                    JobTitle.get(),
                    Salary.get(),
                    Housing_allowance.get(),
                    Trans_allowance.get(),
                    Health_Insurance.get(),
                    Phone_Charge.get(),
                    Work_license.get(),
                   Residence_permit.get(),
                   SCE.get(),
                   GOSI.get()))
    sqlcon.commit()
    sqlcon.close()


conn.close()
#=====================================================Update
    def Update():
            sqlcon = mysql.connector.connect(host="localhost", user="root", password="12345678", database="naizak")
            cursor = sqlcon.cursor()
            cursor.execute("update BID set
                           ID=%s,
                           NAME=%s,
                           Nationlty=%s,
                           JobTitle=%s,
                           Salary=%s,
                           Housing_allowance=%s,
                           Trans_allowance=%s,
                           Health_Insurance=%s,
                           Phone_Charge=%s,
                           Work_license=%s,
                           Residence_permit=%s,
                           SCE=%s,
                           GOSI=%s"),
                           (ID.get(),
                            NAME.get(),
                            Nationlty.get(),
                            JobTitle.get(),
                            Salary.get(),
                            Housing_allowance.get(),
                            Trans_allowance.get(),
                            Health_Insurance.get(),
                            Phone_Charge.get(),
                            Work_license.get(),
                           Residence_permit.get(),
                           SCE.get(),
                           GOSI.get()))
            sqlcon.commit()
#======================================================search
        def search():
            sqlcon = mysql.connector.connect(host="localhost", user="root", password="12345678", database="naizak")
            cursor = sqlcon.cursor()
            cursor.execute("select * from Name where NAME='%s'" %NAME.get())
            row = cursor.fetchall()
            ID.set               (row[0])
            NAME.set             (row[1])
            Nationlty.set        (row[2])
            JobTitle.set         (row[3])
            Salary.set           (row[4])
            Housing_allowance.set(row[5])
            Trans_allowance.set  (row[6])
            Health_Insurance.set (row[7])
            Phone_Charge.set     (row[8])
            Work_license.set     (row[9])
            Residence_permit.set (row[10])
            SCE.set              (row[11])
            GOSI.set             (row[12])
            sqlcon.commit()
            sqlcon.close()
#=====================================================Combobox
NAME = mysql.connector.connect(host="localhost", user="root", password="12345678", database="naizak")
            cursor = sqlcon.cursor()
            cursor.execute("select * from Name where NAME='%s'" %NAME.get())
            row = cursor.fetchall()
            NAME.set             (row[1])
            sqlcon.commit()
            sqlcon.close()

#=====================================================mysql.connector===============================================
import mysql.connector
conn = mysql.connector.connect(user = 'root',password= "", host = 'localhost',database = 'tender')
print(conn)
conn.close()
"""
