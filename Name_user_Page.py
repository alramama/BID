from tkinter import *
from tkinter import ttk

import tkinter.messagebox
import time
import datetime
import tempfile, os

Name = Tk()
Name.geometry("1300x1000+0+0")
Name.title("NAME INFORMATION")

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
End_services = StringVar()
Total_cost = StringVar()

Salary.set("0")
Housing_allowance.set("0")
Trans_allowance.set("0")
Health_Insurance.set("0")
Annual_Tickets.set("0")
Phone_Charge.set("0")
Work_license.set("0")
Residence_permit.set("0")
SCE.set("0")
GOSI.set("0")



def call():
    A = float(Salary.get())
    B = float(Housing_allowance.get())
    C = float(Trans_allowance.get())
    D = float(Work_license.get())
    E = float(Residence_permit.get())
    F = float(SCE.get())
    Total_cost1 = float(A+B+C+E+D+E+F)
    Total_cost.set(Total_cost1)

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

lbl_ID =                     Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'),text="ID",                fg="black", bd=5).grid(row=1, column=0)
lbl_Name =                   Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'),text="NAME",              fg="black", bd=5).grid(row=2, column=0)
lbl_Job_Title =              Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'),text="Job Title",         fg="black", bd=5).grid(row=3, column=0)
lbl_Qualification =          Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'),text="Qualification",     fg="black", bd=5).grid(row=4, column=0)
lbl_Salary =                 Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="Salary",           fg="black", bd=5).grid(row=5, column=0)
lbl_Total_cost =             Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="Total Cost",   fg="black", bd=5).grid(row=6, column=0)
Are_you_Saudi =              Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="Are_you_Saudi",    fg="black", bd=5).grid(row=7, column=0)
Are_you_marrid =             Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="Are_you_marrid",   fg="black", bd=5).grid(row=8, column=0)


lbl_ID =                     Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'),textvariable=ID,                fg="black", bd=5).grid(row=1, column=1)
lbl_Name =                   Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'),textvariable=NAME,              fg="black", bd=5).grid(row=2, column=1)
lbl_Job_Title =              Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'),textvariable=JobTitle,         fg="black", bd=5).grid(row=3, column=1)
#lbl_Qualification =          Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'),textvariable=Qualification,     fg="black", bd=5).grid(row=4, column=1)
ENT_Salary =                 Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), textvariable=Salary,           fg="black", bd=5)
ENT_Salary.grid(row=5, column=1)
ENT_Total_cost =             Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), textvariable=Total_cost,           fg="black", bd=5)
ENT_Total_cost.grid(row=6, column=1)




def Nationalty(e):

    if Are_you_Saudi.get() == "Yes":

        lbl_Housing_allowance =     Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="Housing allowance",    fg="black", bd=5).grid(row=1, column=2)
        lbl_Trans_allowance =       Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="Trans allowance",      fg="black", bd=5).grid(row=2, column=2)
        lbl_Health_Insurance =      Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="Health Insurance",     fg="black", bd=5).grid(row=3,column=2)
        lbl_Phone_Charge=           Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="Phone Charge",         fg="black", bd=5).grid(row=4,column=2)
        lbl_SCE=                    Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="SCE",                  fg="black", bd=5).grid(row=5,column=2)
        lbl_GOSI=                   Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="GOSI",                 fg="black", bd=5).grid(row=6,column=2)

        lbl_Housing_allowance =     Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), textvariable= Housing_allowance,    fg="black", bd=5).grid(row=1, column=3)
        lbl_Trans_allowance =       Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), textvariable=Trans_allowance,      fg="black", bd=5).grid(row=2, column=3)
        lbl_Health_Insurance =      Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), textvariable=Health_Insurance,     fg="black", bd=5).grid(row=3,column=3)
        lbl_Phone_Charge=           Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), textvariable=Phone_Charge,         fg="black", bd=5).grid(row=4,column=3)
        lbl_SCE=                    Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), textvariable=SCE,                  fg="black", bd=5).grid(row=5,column=3)
        lbl_GOSI=                   Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), textvariable=GOSI,                 fg="black", bd=5).grid(row=6,column=3)
        GOSI1 = float(Salary.get())
        GOSI2 = float(0.12)
        GOSI3 = str(GOSI1 * GOSI2)
        GOSI.set(GOSI3)
        Work_license.set("950")
        Residence_permit.set("65")
        Housing_allowance1 = float(Salary.get())
        Housing_allowance2 = float(0.25)
        Housing_allowance3 = str(Housing_allowance1 * Housing_allowance2)
        Housing_allowance.set(Housing_allowance3)

        Trans_allowance1 = float(Salary.get())
        Trans_allowance2 = float(0.10)
        Trans_allowance3 = str(Trans_allowance1 * Trans_allowance2)
        Trans_allowance.set(Trans_allowance3)

        


    else:
        lbl_Housing_allowance =     Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="Housing allowance",    fg="black", bd=5).grid(row=1, column=2)
        lbl_Trans_allowance =       Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="Trans allowance",      fg="black", bd=5).grid(row=2, column=2)
        lbl_Health_Insurance =      Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="Health Insurance",     fg="black", bd=5).grid(row=3,column=2)
        lbl_Phone_Charge=           Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="Phone Charge",         fg="black", bd=5).grid(row=4,column=2)
        lbl_SCE=                    Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="SCE",                  fg="black", bd=5).grid(row=5,column=2)
        lbl_GOSI=                   Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="GOSI",                 fg="black", bd=5).grid(row=6,column=2)

        lbl_Housing_allowance =     Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), textvariable=Housing_allowance,    fg="black", bd=5).grid(row=1, column=3)
        lbl_Trans_allowance =       Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), textvariable=Trans_allowance,      fg="black", bd=5).grid(row=2, column=3)
        lbl_Health_Insurance =      Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), textvariable=Health_Insurance,     fg="black", bd=5).grid(row=3,column=3)
        lbl_Phone_Charge=           Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), textvariable=Phone_Charge,         fg="black", bd=5).grid(row=4,column=3)
        lbl_SCE=                    Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), textvariable=SCE,                  fg="black", bd=5).grid(row=5,column=3)
        lbl_GOSI=                   Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), textvariable=GOSI,                 fg="black", bd=5).grid(row=6,column=3)

        lbl_Annual_Tickets =        Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="Annual Tickets",     fg="black", bd=5).grid(row=7,column=2)
        lbl_Work_license=           Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="Work license",       fg="black", bd=5).grid(row=8,column=2)
        lbl_Residence_permit=       Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="Residence permit",   fg="black", bd=5).grid(row=9,column=2)

        lbl_Annual_Tickets =        Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), textvariable=Annual_Tickets,     fg="black", bd=5).grid(row=7,column=3)
        lbl_Work_license=           Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), textvariable=Work_license,       fg="black", bd=5).grid(row=8,column=3)
        lbl_Residence_permit=       Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), textvariable=Residence_permit,   fg="black", bd=5).grid(row=9,column=3)
        GOSI1 = float(Salary.get())
        GOSI2 = float(0.02)
        GOSI3 = str(GOSI1 * GOSI2)
        GOSI.set(GOSI3)
        Work_license.set("950")
        Residence_permit.set("65")
        Housing_allowance1 = float(Salary.get())
        Housing_allowance2 = float(0.25)
        Housing_allowance3 = str(Housing_allowance1 * Housing_allowance2)
        Housing_allowance.set(Housing_allowance3)

        Trans_allowance1 = float(Salary.get())
        Trans_allowance2 = float(0.10)
        Trans_allowance3 = str(Trans_allowance1 * Trans_allowance2)
        Trans_allowance.set(Trans_allowance3)




Are_you_Saudi = ttk.Combobox(FRAM_Name_Emp_Info1)
Are_you_Saudi['values'] = "Yes", "NO"
Are_you_Saudi.current()
Are_you_Saudi.bind('<<ComboboxSelected>>',Nationalty)
Are_you_Saudi.grid(row=7, column=1)

def marrid(e):
    if Are_you_Saudi.get() == "Yes":
        lbl_No_wife =        Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="No. Wife",      fg="black", bd=5).grid(row=10,column=2)
        lbl_No_Boy=           Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="No_Boy",       fg="black", bd=5).grid(row=11,column=2)
        lbl_No_Gril=       Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="No_Gril",         fg="black", bd=5).grid(row=12,column=2)

        lbl_No_wife =        Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="Annual Tickets",     fg="black", bd=5).grid(row=10,column=3)
        lbl_Work_license=           Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="Work license",       fg="black", bd=5).grid(row=11,column=3)
        lbl_Residence_permit=       Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="Residence permit",   fg="black", bd=5).grid(row=12,column=3)



Are_you_marrid = ttk.Combobox(FRAM_Name_Emp_Info1)
Are_you_marrid['values'] = "Yes"
Are_you_marrid.current()
Are_you_marrid.bind('<<ComboboxSelected>>',marrid)
Are_you_marrid.grid(row=8, column=1)

def Qualification1(e):
    if Qualification.get() == "Eng":
        SCE.set("1300")
    if Qualification.get() == "Tech":
        SCE.set("700")
    if Qualification.get() == "Admin":
        SCE.set("00")


Qualification = ttk.Combobox(FRAM_Name_Emp_Info1)
Qualification['values'] = "Eng", "Tech", "Admin"
Qualification.current()
Qualification.bind('<<ComboboxSelected>>', Qualification1)
Qualification.grid(row=4, column=1)



#Housing_allowance.set("00")
Trans_allowance.set("00")
Health_Insurance.set("00")
Annual_Tickets.set("00")
Phone_Charge.set("00")
Work_license.set("00")
Residence_permit.set("00")
SCE.set("00")
GOSI.set("00")

BTN_MainFrame =             Frame(Name, bd=16, width=600, height=50, relief=RIDGE)
BTN_MainFrame.grid(row=2, column=0)
BtnTotalCost = Button(BTN_MainFrame, bd = 8 , pady = 8 , fg = "black", font = ('arial',16, 'bold'), width =11, text = "Total Cost", bg = "white",command = call).grid(row = 0 , column = 0)



Name.mainloop()






Name.mainloop()

  
    

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
