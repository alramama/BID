from tkinter import *
import tkinter.messagebox
import time
import datetime
import tempfile, os

Vendor = Tk()
Vendor.geometry("800x1000+0+0")
Vendor.title("VENDOR INFORMATION")
#Vendor_Type = ["Sales","Service","Contracts"]
#Customer = ["Gov","SEC","ARAMCO","SABIC","SWCC","NWC"]

#===================================================================VENDORTopFram=================================================
#VENDOR_Page_title = Frame(VENDOR, bd=16, width=1350, height=60, relief=RAISED)
#VENDOR_Page_title.pack(side=TOP)
#VENDOR_Page_Name = Label(VENDOR_Page_title,font=('arial',40, 'bold'),text = "VENDOR INFORMATION", bd=10)
#VENDOR_Page_Name.pack()
#===================================================================VENDORBOTTOMFram=================================================
Vendor_MainFrame = Frame(Vendor, bd=16, width=1350, height=600, relief=RIDGE)
Vendor_MainFrame.grid(row=0, column=0)

lbl_RFQ_No =                      Label(Vendor_MainFrame, font=('arial', 6, 'bold'),text="RFQ_No",                  fg="black", bd=5).grid(row=0, column=0)
lbl_Item_Name =                   Label(Vendor_MainFrame, font=('arial', 6, 'bold'),text="Item_Name",               fg="black", bd=5).grid(row=1, column=0)
lbl_Type_of_work =                Label(Vendor_MainFrame, font=('arial', 6, 'bold'),text="Type of work",            fg="black", bd=5).grid(row=2, column=0)
ENT_RFQ_No =                      Entry(Vendor_MainFrame, font=('arial', 6, 'bold'),text="RFQ_No",                  fg="black", bd=5).grid(row=0, column=1)
ENT_Item_Name =                   Entry(Vendor_MainFrame, font=('arial', 6, 'bold'),text="Item_Name",               fg="black", bd=5).grid(row=1, column=1)
ENT_Type of_work =                Entry(Vendor_MainFrame, font=('arial', 6, 'bold'),text="Type of work",            fg="black", bd=5).grid(row=2, column=1)

lbl_Supplirs_Name =               Label(Vendor_MainFrame, font=('arial', 6, 'bold'),text="Supplirs_Name",           fg="black", bd=5).grid(row=0, column=2)
lbl_Qoutation_no =                Label(Vendor_MainFrame, font=('arial', 6, 'bold'),text="Qoutation_no",            fg="black", bd=5).grid(row=1, column=2)
lbl_Qoutation_valdity =           Label(Vendor_MainFrame, font=('arial', 6, 'bold'),text="Qoutation valdity",       fg="black", bd=5).grid(row=2, column=2)
lbl_Qoutation_Copy =              Label(Vendor_MainFrame, font=('arial', 6, 'bold'),text="Qoutation_Copy",          fg="black", bd=5).grid(row=3, column=2)
ENT_Supplirs_Name =               Entry(Vendor_MainFrame, font=('arial', 6, 'bold'),text="Supplirs_Name",           fg="black", bd=5).grid(row=0, column=3)
ENT_Qoutation_no =                Entry(Vendor_MainFrame, font=('arial', 6, 'bold'),text="Qoutation_no",            fg="black", bd=5).grid(row=1, column=3)
ENT_Qoutation_valdity =           Entry(Vendor_MainFrame, font=('arial', 6, 'bold'),text="Qoutation valdity",       fg="black", bd=5).grid(row=2, column=3)
ENT_Qoutation_Copy =              Entry(Vendor_MainFrame, font=('arial', 6, 'bold'),text="Qoutation_Copy",          fg="black", bd=5).grid(row=3, column=3)

lbl_CONTACT_INFO_Email =          Label(Vendor_MainFrame, font=('arial', 6, 'bold'),text="CONTACT_INFO_Email",      fg="black", bd=5).grid(row=0, column=4)
lbl_CONTACT_INFO_Mob =            Label(Vendor_MainFrame, font=('arial', 6, 'bold'),text="CONTACT_INFO_Mob",        fg="black", bd=5).grid(row=1, column=4)
lbl_CONTACT_INFO_Tel =            Label(Vendor_MainFrame, font=('arial', 6, 'bold'),text="CONTACT_INFO_Tel",        fg="black", bd=5).grid(row=2, column=4)
ENT_CONTACT_INFO_Email =          Entry(Vendor_MainFrame, font=('arial', 6, 'bold'),text="CONTACT_INFO_Email",      fg="black", bd=5).grid(row=0, column=5)
ENT_CONTACT_INFO_Mob =            Entry(Vendor_MainFrame, font=('arial', 6, 'bold'),text="CONTACT_INFO_Mob",        fg="black", bd=5).grid(row=1, column=5)
ENT_CONTACT_INFO_Tel =            Entry(Vendor_MainFrame, font=('arial', 6, 'bold'),text="CONTACT_INFO_Tel",        fg="black", bd=5).grid(row=2, column=5)

Vendor.mainloop()


