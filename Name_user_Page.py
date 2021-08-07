from tkinter import *
from tkinter import ttk

import tkinter.messagebox
import time
import datetime
import tempfile, os

Name = Tk()
Name.geometry("1300x700+0+0")
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
No_wife = StringVar()
No_BOY = StringVar()
No_GIRL = StringVar()

Salary.set("0")
Housing_allowance.set("0")
Trans_allowance.set("0")
Health_Insurance.set("75")
Annual_Tickets.set("150")
Phone_Charge.set("200")
Work_license.set("950")
Residence_permit.set("65")
SCE.set("0")
GOSI.set("0")
End_services.set("0.0")


def call():
    a = float(Salary.get())
    b = float(Housing_allowance.get())
    c = float(Trans_allowance.get())
    d = float(Work_license.get())
    e = float(Residence_permit.get())
    f = float(SCE.get())
    g = float(Annual_Tickets.get())
    h = float(Phone_Charge.get())
    i = float(GOSI.get())
    # j = float(Phone_Charge.get())
    # k = float(Phone_Charge.get())
    total_cost1 = float(a + b + c + e + d + f + g + h + i)
    Total_cost.set(total_cost1)



# ===================================================================NAMETopFram=================================================
NAME_Page_title = Frame(Name, bd=16, width=1000, height=60, relief=RIDGE)
NAME_Page_title.grid(row=0, column=0)
NAME_Page_Name = Label(NAME_Page_title, font=('arial', 40, 'bold'), text="NAME INFORMATION", bd=10)
NAME_Page_Name.grid(row=0, column=0)
# ===================================================================NAMEBOTTOMFram=================================================
NAME_MainFrame = Frame(Name, bd=16, width=1350, height=500, relief=RIDGE)
NAME_MainFrame.grid(row=1, column=0)

# ===================================================================FRAM_Name_Emp_Info.=================================================
FRAM_Name_Emp_Info = Frame(NAME_MainFrame, bd=16, width=70, height=60, relief=RIDGE)
FRAM_Name_Emp_Info.grid(row=1, column=0)
FRAM_Name_Emp_Info1 = Frame(NAME_MainFrame, bd=16, width=70, height=60, relief=RIDGE)
FRAM_Name_Emp_Info1.grid(row=1, column=0)

lbl_ID = Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="ID", fg="black", bd=5).grid(row=1, column=0)
lbl_Name = Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="NAME", fg="black", bd=5).grid(row=2, column=0)
lbl_Job_Title = Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="Job Title", fg="black", bd=5).grid(row=3,
                                                                                                                column=0)
lbl_Qualification = Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="Qualification", fg="black", bd=5).grid(
    row=4, column=0)
lbl_Salary = Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="Salary", fg="black", bd=5).grid(row=5,
                                                                                                          column=0)
lbl_Total_cost = Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="Total Cost", fg="black", bd=5).grid(row=6,
                                                                                                                  column=0)
lbl_id = Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), textvariable=ID, fg="black", bd=5).grid(row=1, column=1)
lbl_name = Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), textvariable=NAME, fg="black", bd=5).grid(row=2,
                                                                                                            column=1)
lbl_job_title = Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), textvariable=JobTitle, fg="black", bd=5).grid(
    row=3, column=1)
# lbl_Qualification =          Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'),textvariable=Qualification,     fg="black", bd=5).grid(row=4, column=1)
ent_salary = Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), textvariable=Salary, fg="black", bd=5)
ent_salary.grid(row=5, column=1)
ent_Total_cost = Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), textvariable=Total_cost, fg="black", bd=5)
ent_Total_cost.grid(row=6, column=1)

are_you_saudi = Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="Are_you_Saudi", fg="black", bd=5).grid(
    row=7, column=0)
MMM = Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="Are_you_marrid", fg="black", bd=5).grid(row=8,
                                                                                                           column=0)


def nationalty(e):
    if are_you_saudi.get() == "Yes":

        lbl_housing_allowance = Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="Housing allowance",
                                      fg="black", bd=5).grid(row=1, column=2)
        lbl_trans_allowance = Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="Trans allowance", fg="black",
                                    bd=5).grid(row=2, column=2)
        lbl_health_insurance = Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="Health Insurance",
                                     fg="black", bd=5).grid(row=3, column=2)
        lbl_phone_charge = Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="Phone Charge", fg="black",
                                 bd=5).grid(row=4, column=2)
        lbl_sce = Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="SCE", fg="black", bd=5).grid(row=5,
                                                                                                            column=2)
        lbl_gosi = Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="GOSI", fg="black", bd=5).grid(row=6,
                                                                                                              column=2)
        lbl_end_services = Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="End_services", fg="black",
                                 bd=5).grid(row=7, column=2)

        lbl_housing_allowance = Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), textvariable=Housing_allowance,
                                      fg="black", bd=5).grid(row=1, column=3)
        lbl_trans_allowance = Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), textvariable=Trans_allowance,
                                    fg="black", bd=5).grid(row=2, column=3)
        lbl_health_insurance = Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), textvariable=Health_Insurance,
                                     fg="black", bd=5).grid(row=3, column=3)
        lbl_phone_charge = Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), textvariable=Phone_Charge, fg="black",
                                 bd=5).grid(row=4, column=3)
        lbl_sce = Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), textvariable=SCE, fg="black", bd=5).grid(row=5,
                                                                                                                  column=3)
        lbl_gosi = Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), textvariable=GOSI, fg="black", bd=5).grid(
            row=6, column=3)
        lbl_end_services = Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), textvariable=End_services, fg="black",
                                 bd=5).grid(row=7, column=3)

        housing_allowance1 = float(Salary.get())
        housing_allowance2 = float(0.25)
        housing_allowance3 = str(housing_allowance1 * housing_allowance2)
        Housing_allowance.set(housing_allowance3)
        gosi1: float = float(Salary.get())
        gosi2 = float(Housing_allowance.get())
        gosi3 = float(0.12)
        gosi4 = str((gosi1 + gosi2) * gosi3)
        GOSI.set(gosi4)
        gosi5 = str(gosi1 + gosi2)

        end1: float = float(Salary.get())
        end2 = float(Housing_allowance.get())
        end3 = float(12)
        end4 = str((end1 + end2) / end3)
        End_services.set(end4)

        trans_allowance1 = float(Salary.get())
        trans_allowance2 = float(0.10)
        trans_allowance3 = str(trans_allowance1 * trans_allowance2)
        Trans_allowance.set(trans_allowance3)




    else:
        lbl_housing_allowance = Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="Housing allowance",
                                      fg="black", bd=5).grid(row=1, column=2)
        lbl_trans_allowance = Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="Trans allowance", fg="black",
                                    bd=5).grid(row=2, column=2)
        lbl_health_insurance = Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="Health Insurance",
                                     fg="black", bd=5).grid(row=3, column=2)
        lbl_phone_charge = Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="Phone Charge", fg="black",
                                 bd=5).grid(row=4, column=2)
        lbl_sec = Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="SCE", fg="black", bd=5).grid(row=5,
                                                                                                            column=2)
        lbl_gosi = Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="GOSI", fg="black", bd=5).grid(row=6,
                                                                                                              column=2)

        lbl_housing_allowance = Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), textvariable=Housing_allowance,
                                      fg="black", bd=5).grid(row=1, column=3)
        lbl_trans_allowance = Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), textvariable=Trans_allowance,
                                    fg="black", bd=5).grid(row=2, column=3)
        lbl_health_insurance = Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), textvariable=Health_Insurance,
                                     fg="black", bd=5).grid(row=3, column=3)
        lbl_phone_charge = Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), textvariable=Phone_Charge, fg="black",
                                 bd=5).grid(row=4, column=3)
        lbl_sec = Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), textvariable=SCE, fg="black", bd=5).grid(row=5,
                                                                                                                  column=3)
        lbl_gosi = Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), textvariable=GOSI, fg="black", bd=5).grid(
            row=6, column=3)

        lbl_annual_tickets = Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="Annual Tickets", fg="black",
                                   bd=5).grid(row=7, column=2)
        lbl_work_license = Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="Work license", fg="black",
                                 bd=5).grid(row=8, column=2)
        lbl_residence_permit = Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="Residence permit",
                                     fg="black", bd=5).grid(row=9, column=2)
        lbl_end_services = Label(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), text="End_services", fg="black",
                                 bd=5).grid(row=10, column=2)

        lbl_annual_tickets = Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), textvariable=Annual_Tickets,
                                   fg="black", bd=5).grid(row=7, column=3)
        lbl_work_license = Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), textvariable=Work_license, fg="black",
                                 bd=5).grid(row=8, column=3)
        lbl_residence_permit = Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), textvariable=Residence_permit,
                                     fg="black", bd=5).grid(row=9, column=3)
        lbl_end_services = Entry(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'), textvariable=End_services, fg="black",
                                 bd=5).grid(row=10, column=3)

        housing_allowance1 = float(Salary.get())
        housing_allowance2 = float(0.25)
        housing_allowance3 = str(housing_allowance1 * housing_allowance2)
        Housing_allowance.set(housing_allowance3)

        gosi1: float = float(Salary.get())
        gosi2 = float(Housing_allowance.get())
        gosi3 = float(0.02)
        gosi4 = str((gosi1 + gosi2) * gosi3)
        GOSI.set(gosi4)

        end1: float = float(Salary.get())
        end2 = float(Housing_allowance.get())
        end3 = float(12)
        end4 = str((end1 + end2) / end3)
        End_services.set(end4)

        trans_allowance1 = float(Salary.get())
        trans_allowance2 = float(0.10)
        trans_allowance3 = str(trans_allowance1 * trans_allowance2)
        Trans_allowance.set(trans_allowance3)


are_you_saudi = ttk.Combobox(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'))
are_you_saudi['values'] = "Yes", "NO"
are_you_saudi.current()
are_you_saudi.bind('<<ComboboxSelected>>', nationalty)
are_you_saudi.grid(row=7, column=1)

FRAM_Name_Emp_marriage = Frame(NAME_MainFrame, bd=16, width=70, height=60, relief=RIDGE)
FRAM_Name_Emp_marriage.grid(row=2, column=0)


def marriage(e):
    if MMM.get() == "Yes":
        lbl_no_wife = Label(FRAM_Name_Emp_marriage, font=('arial', 20, 'bold'), text="No. Wife", fg="black", bd=5)
        lbl_no_wife.grid(row=10, column=2)
        lbl_no_boy = Label(FRAM_Name_Emp_marriage, font=('arial', 20, 'bold'), text="No_Boy", fg="black", bd=5)
        lbl_no_boy.grid(row=11, column=2)
        lbl_no_grail = Label(FRAM_Name_Emp_marriage, font=('arial', 20, 'bold'), text="No_Gril", fg="black", bd=5)
        lbl_no_grail.grid(row=12, column=2)

        ent_no_wife = Entry(FRAM_Name_Emp_marriage, font=('arial', 20, 'bold'), textvariable=No_wife, fg="black", bd=5)
        ent_no_wife.grid(row=10, column=3)
        ent_no_boy = Entry(FRAM_Name_Emp_marriage, font=('arial', 20, 'bold'), textvariable=No_BOY, fg="black", bd=5)
        ent_no_boy.grid(row=11, column=3)
        ent_no_gril = Entry(FRAM_Name_Emp_marriage, font=('arial', 20, 'bold'), textvariable=No_GIRL, fg="black", bd=5)
        ent_no_gril.grid(row=12, column=3)

        health_insurance_wife = float(170)
        health_insurance_boy = float(45)
        health_insurance_girl = float(60)
        no_wife = float(No_wife.get())
        no_boy = float(No_wife.get())
        no_girl = float(No_wife.get())

        wife_cost = str(health_insurance_wife * no_wife)
        boy_cost = str(health_insurance_boy * no_boy)
        girl_cost = str(health_insurance_girl * no_girl)

        health_insurance_total_cost = str(wife_cost + boy_cost + girl_cost)
        Health_Insurance.set(health_insurance_total_cost)

        annual_tickets_wife = float(125)
        annual_tickets_boy = float(125)
        annual_tickets_girl = float(125)

        wife_cost1 = float(annual_tickets_wife) * float(No_wife.get())
        boy_cost1 = float(annual_tickets_boy) * float(No_BOY.get())
        girl_cost1 = float(annual_tickets_girl) * float(No_GIRL.get())

        annual_tickets_total_cost = str(wife_cost1 + boy_cost1 + girl_cost1)
        Annual_Tickets.set(annual_tickets_total_cost)


MMM = ttk.Combobox(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'))
MMM['values'] = "Yes"
MMM.bind('<<ComboboxSelected>>', marriage)
MMM.grid(row=8, column=1)


def Qualification1(e):
    if Qualification.get() == "Eng":
        SCE.set("100")
    if Qualification.get() == "Tech":
        SCE.set("60")
    if Qualification.get() == "Admin":
        SCE.set("00")


Qualification = ttk.Combobox(FRAM_Name_Emp_Info1, font=('arial', 20, 'bold'))
Qualification['values'] = "Eng", "Tech", "Admin"
Qualification.current()
Qualification.bind('<<ComboboxSelected>>', Qualification1)
Qualification.grid(row=4, column=1)

BTN_MainFrame = Frame(Name, bd=16, width=600, height=50, relief=RIDGE)
BTN_MainFrame.grid(row=2, column=0)
BtnTotalCost = Button(BTN_MainFrame, bd=8, pady=8, fg="black", font=('arial', 16, 'bold'), width=11, text="Total Cost",
                      bg="white", command=call).grid(row=0, column=0)

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
