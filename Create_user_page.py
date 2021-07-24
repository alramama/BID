from tkinter import *
import tkinter.messagebox
import time
import datetime
import tempfile, os

root = Tk()
root.geometry("1350x650+0+0")
root.title("")

# ====================================================Frame===================================================================
TOP_Frame = Frame(root, bd=16, width=1350, height=50, relief=RAISED)
TOP_Frame.pack(side=TOP)
F1 = Frame(root, bd=16, width=600, height=600, relief=RAISED)
F1.pack(side=LEFT)
F2 = Frame(root, bd=16, width=300, height=600, relief=RAISED)
F2.pack(side=RIGHT)
F1a = Frame(F1, bd=16, width=600, height=200, relief=RAISED)
F1a.pack(side=TOP)
F1b = Frame(F1, bd=16, width=600, height=600, relief=RAISED)
F1b.pack(side=TOP)

# ================================================================MainLable============================================

lblMainTitel = Label(TOP_Frame, font=('arial', 60, 'bold'), text="Payment Mangmant System", bd=10)
lblMainTitel.grid(row=0, column=0)
# ==============================================================LableEntry==============================================

lblName = Label(F1a, font=('arial', 16, 'bold'), text="NAME", fg="black", bd=20).grid(row=0, column=0)
lblEmployer = Label(F1a, font=('arial', 16, 'bold'), text="Emplyer", fg="black", bd=20).grid(row=1, column=0)
lblHoursWorked = Label(F1a, font=('arial', 16, 'bold'), text="Hours Worked", fg="black", bd=20).grid(row=2, column=0)
lblBlack = Label(F1a, font=('arial', 16, 'bold'), text="Tax", fg="black", bd=20).grid(row=3, column=0)
lblGrossPay = Label(F1a, font=('arial', 16, 'bold'), text="Gross Pay", fg="black", bd=20).grid(row=4, column=0)

EntName = Entry(F1a, font=('arial', 16, 'bold'), text="NAME", textvariable=NAME, fg="black", bd=20).grid(row=0,
                                                                                                         column=1)
EntEmployer = Entry(F1a, font=('arial', 16, 'bold'), text="Emplyer", textvariable=Emplyer, fg="black", bd=20).grid(
    row=1, column=1)
EntHoursWorked = Entry(F1a, font=('arial', 16, 'bold'), text="Hours Worked", textvariable=HoursWorked, fg="black",
                       bd=20).grid(row=2, column=1)
EntBlack = Entry(F1a, font=('arial', 16, 'bold'), text="Tax", textvariable=Tax, fg="black", bd=20).grid(row=3, column=1)
EntGrossPay = Entry(F1a, font=('arial', 16, 'bold'), text="Gross Pay", textvariable=GrossPay, fg="black", bd=20).grid(
    row=4, column=1)

lblAddress = Label(F1a, font=('arial', 16, 'bold'), text="Address", fg="black", bd=20).grid(row=0, column=2)
lblNINumber = Label(F1a, font=('arial', 16, 'bold'), text="NI Number", fg="black", bd=20).grid(row=1, column=2)
lblHourlyRate = Label(F1a, font=('arial', 16, 'bold'), text="Hourly Rate", fg="black", bd=20).grid(row=2, column=2)
lblOverTime = Label(F1a, font=('arial', 16, 'bold'), text="Over Time", fg="black", bd=20).grid(row=3, column=2)
lblNetPay = Label(F1a, font=('arial', 16, 'bold'), text="Net Pay", fg="black", bd=20).grid(row=4, column=2)

lblAddress = Entry(F1a, font=('arial', 16, 'bold'), text="Address", textvariable=Address, fg="black", bd=20)
lblAddress.grid(row=0, column=3)
lblNINumber = Entry(F1a, font=('arial', 16, 'bold'), text="NI Number", textvariable=NINumber, fg="black", bd=20)
lblNINumber.grid(row=1, column=3)
lblHourlyRate = Entry(F1a, font=('arial', 16, 'bold'), text="Hourly Rate", textvariable=HourlyRate, fg="black", bd=20)
lblHourlyRate.grid(row=2, column=3)
lblOverTime = Entry(F1a, font=('arial', 16, 'bold'), text="Over Time", textvariable=OverTime, fg="black", bd=20)
lblOverTime.grid(row=3, column=3)
lblNetPay = Entry(F1a, font=('arial', 16, 'bold'), text="Net Pay", textvariable=NetPay, fg="black", bd=20)
lblNetPay.grid(row=4, column=3)
# =====================================================================TEXT===================================================================
lblPaySlip = Label(F2, font=('arial', 16, 'bold'), textvariable=DateOfOrder, fg="black", bd=20).grid(row=0, column=0)
EntryPaySlip = Text(F2, font=('arial', 16, 'bold'), bd=20, width=22, height=15)
EntryPaySlip.grid(row=2, column=0)

# ===============================================================Button=======================================================================
btnSalary = Button(F1b, text="Weekly Salary", padx=16, pady=16, bd=8, fg="black", font=('arial', 16, 'bold'), width=14,height=1, command = print).grid(row=0, column=0)
btnExit = Button(F1b, text="Exit System", padx=16, pady=16, bd=8, fg="black", font=('arial', 16, 'bold'), width=14,
                 height=1, command=Exit).grid(row=0, column=1)
btnPaySlip = Button(F1b, text="View Slip Pay ", padx=16, pady=16, bd=8, fg="black", font=('arial', 16, 'bold'),
                    width=14, height=1, command=EntryInfo).grid(row=0, column=2)
btnPayRest = Button(F1b, text="Rest", padx=16, pady=16, bd=8, fg="black", font=('arial', 16, 'bold',), width=14,
                    height=1, command=Rest).grid(row=0, column=3)



root.mainloop()

