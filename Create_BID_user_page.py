from tkinter import *
import tkinter.messagebox
import time
import datetime
import tempfile, os
import self as self


class Name1:

    def __init__(self, root):
        self.Name = Tk()
        self.Name.geometry("1350x300+0+0")
        self.Name.title("NAME INFORMATION")
        #Name_Type = ["Sales","Service","Contracts"]
        #Customer = ["Gov","SEC","ARAMCO","SABIC","SWCC","NWC"]
        
        ID = StringVar()
        NAME = StringVar()
        JobTitle = StringVar()
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
        
        #(ID, NAME, JobTitle, Qualification, Salary, Housing_allowance, Health_Insurance, Trans_allowance, Annual_Tickets,Phone_Charge, Work_license, SCE, GOSI)
        #(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        #(ID.get(), NAME.get(), JobTitle.get(), Qualification.get(), Salary.get(), Housing_allowance.get(), Health_Insurance.get(), Trans_allowance.get(), Annual_Tickets.get(),Phone_Charge.get(), Work_license.get(), SCE.get(), GOSI.get())
        
        self.NAME_MainFrame = Frame(self.Name, bd=16, width=1350, height=600, relief=RIDGE)
        self.NAME_MainFrame.grid(row=0, column=0)
        self.FRAM_Name_Emp_Info = Frame(self.NAME_MainFrame, bd=16, width=70, height=60, relief=RIDGE)
        self.FRAM_Name_Emp_Info.grid(row=1, column=0)
        self.FRAM_Name_Emp_Info1 = Frame(self.NAME_MainFrame, bd=16, width=70, height=60, relief=RIDGE)
        self.FRAM_Name_Emp_Info1.grid(row=1, column=0)

        self.lbl_ID =               Label(self.FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="ID", fg="black", bd=5).grid(row=1, column=0)
        self.lbl_Name =             Label(self.FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="NAME", fg="black", bd=5).grid(row=2, column=0)
        self.lbl_Job_Title =        Label(self.FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Job Title", fg="black",bd=5).grid(row=3, column=0)
        self.lbl_Qualification =    Label(self.FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Qualification",fg="black", bd=5).grid(row=4, column=0)

        self.ENT_ID =                       Entry(self.FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), textvariable=ID, fg="black", bd=5)
        self.ENT_ID.grid(row=1, column=1)
        self.ENT_Name =                     Entry(self.FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), textvariable=NAME, fg="black", bd=5)
        self.ENT_Name.grid(row=2, column=1)
        self.ENT_Job_Title =                Entry(self.FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), textvariable=JobTitle,fg="black", bd=5)
        self.ENT_Job_Title.grid(row=3, column=1)
        self.ENT_Qualification =            Entry(self.FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), textvariable= Qualification,fg="black", bd=5)
        self.ENT_Qualification.grid(row=4, column=1)

        self.lbl_Salary =               Label(self.FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Salary", fg="black",bd=5).grid(row=1, column=2)
        self.lbl_Housing_allowance =    Label(self.FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'),text="Housing allowance", fg="black", bd=5).grid(row=2, column=2)
        self.lbl_Trans_allowance =      Label(self.FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Trans allowance",fg="black", bd=5).grid(row=3, column=2)

        self.ENT_Salary =                       Entry(self.FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), textvariable=Salary, fg="black",bd=5)
        self.ENT_Salary.            grid(row=1, column=3)
        self.ENT_Housing_allowance =            Entry(self.FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'),textvariable=Housing_allowance, fg="black", bd=5)
        self.ENT_Housing_allowance. grid(row=2, column=3)
        self.ENT_Trans_allowance =              Entry(self.FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'),textvariable=Trans_allowance, fg="black", bd=5)
        self.ENT_Trans_allowance.   grid(row=3, column=3)

        self.lbl_Health_Insurance = Label(self.FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Health Insurance",fg="black", bd=5).grid(row=1, column=4)
        self.lbl_Annual_Tickets =   Label(self.FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Annual Tickets",fg="black", bd=5).grid(row=2, column=4)
        self.lbl_Phone_Charge =     Label(self.FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Phone Charge",fg="black", bd=5).grid(row=3, column=4)

        self.ENT_Health_Insurance =                     Entry(self.FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'),textvariable=Health_Insurance, fg="black", bd=5)
        self.ENT_Health_Insurance.grid(row=1, column=5)
        self.ENT_Annual_Tickets =                       Entry(self.FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'),textvariable=Annual_Tickets, fg="black", bd=5)
        self.ENT_Annual_Tickets.grid(row=2, column=5)
        self.ENT_Phone_Charge =                         Entry(self.FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), textvariable=Phone_Charge,fg="black", bd=5)
        self.ENT_Phone_Charge.grid(row=3, column=5)

        self.lbl_Work_license =     Label(self.FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Work license",fg="black", bd=5).grid(row=1, column=6)
        self.lbl_Residence_permit = Label(self.FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Residence permit",fg="black", bd=5).grid(row=2, column=6)
        self.lbl_SCE =              Label(self.FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="SCE", fg="black", bd=5).grid(row=3, column=6)

        self.ENT_Work_license =                         Entry(self.FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), textvariable=Work_license,fg="black", bd=5)
        self.ENT_Work_license.grid(row=1, column=7)
        self.ENT_Residence_permit =                     Entry(self.FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'),textvariable=Residence_permit, fg="black", bd=5)
        self.ENT_Residence_permit.grid(row=2, column=7)
        self.ENT_SCE =                                  Entry(self.FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), textvariable=SCE, fg="black", bd=5)
        self.ENT_SCE.grid(row=3, column=7)
        self.lbl_GOSI =                                 Label(self.FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="GOSI", fg="black", bd=5)
        self.lbl_GOSI.grid(row=1, column=8)
        self.ENT_GOSI =                                 Entry(self.FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), textvariable=GOSI, fg="black", bd=5)
        self.ENT_GOSI.grid(row=1, column=9)
        # =====================================================mysql.connector===============================================
        self.NAME_ButtomFrame =         Frame(self.Name, bd=16, width=1350, height=40, relief=RIDGE)
        self.NAME_ButtomFrame.grid(row=1, column=0)
        self.Insert_Button =            Button(self.NAME_ButtomFrame, font=('arial', 20, 'bold'), text="Insert", command=insert,fg="black", bd=5).grid(row=1, column=0)


if __name__ == '__main__':
    Name = Tk()
    application = Name1(Name)
    Name.mainloop()
