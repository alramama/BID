from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import random
import time
import datetime

root = Tk()
root.geometry("1350x650+0+0")
root.title("Online Ordaring System")
root.configure(background= 'black')


def Iexit():
    Iexit = tkinter.messagebox.askyesno("Ordaring System", "do you want exit this System")
    if Iexit > 0:
        root.destroy()
        return

CustomerRef = StringVar()
Tax = StringVar()
Subtotal = StringVar()
TotalCost = StringVar()
CostWhiteWine = StringVar()
CostRedWine = StringVar()
CostofOtherWine = StringVar()
CostOfDelivery = StringVar()
CustomerName = StringVar()
CustomerPhone = StringVar()
CustomerEmail = StringVar()
TimeOfOrder = StringVar()
DateOfOrder = StringVar()
Discount = StringVar()
ItemOrder = StringVar()
CostWhiteWine = StringVar()
CostRedWine = StringVar()
CostofOtherWine = StringVar()
UnitPriceWhiteWine = StringVar()
UnitPriceRedWine = StringVar()
UnitPriceOtherWine = StringVar()
QtyWhiteWine = StringVar()
QtyPriceRedWine = StringVar()
QtyPriceOtherWine = StringVar()
Discount = StringVar()

CustomerRef.set("")
Tax.set("0")
Subtotal.set("0")
TotalCost.set("0")
CostWhiteWine.set("")
CostRedWine.set("")
CostofOtherWine.set("")
CostOfDelivery.set("")
CustomerName.set("")
CustomerPhone.set("")
CustomerEmail.set("")
TimeOfOrder.set(time.strftime("%H:%M:%S"))
DateOfOrder.set(time.strftime("%d/%m/%Y"))
Discount.set("0")
ItemOrder.set("")
CostWhiteWine.set("0")
CostRedWine.set("0")
CostofOtherWine.set("0")
UnitPriceWhiteWine.set("0")
UnitPriceRedWine.set("0")
UnitPriceOtherWine.set("0")
QtyWhiteWine.set("0")
QtyPriceRedWine.set("0")
QtyPriceOtherWine.set("0")
Discount.set("0")

#=====================================================SET==================================================
def Rest():
    CustomerRef.set("")
    Tax.set("0")
    Subtotal.set("0")
    TotalCost.set("0")
    CostWhiteWine.set("")
    CostRedWine.set("")
    CostofOtherWine.set("")
    CostOfDelivery = StringVar()
    CustomerName.set("")
    CustomerPhone.set("")
    CustomerEmail.set("")
    TimeOfOrder.set("")
    DateOfOrder.set("")
    Discount.set("0")
    ItemOrder.set("")
    CostWhiteWine.set("0")
    CostRedWine.set("0")
    CostofOtherWine.set("0")
    UnitPriceWhiteWine.set("0")
    UnitPriceRedWine.set("0")
    UnitPriceOtherWine.set("0")
    QtyWhiteWine.set("0")
    QtyPriceRedWine.set("0")
    QtyPriceOtherWine.set("0")
    Discount.set("0")
def OrderRef():
    RefPay = random.randint(1,100)
    RefPaid = ("NPS_" + str(RefPay))
    CustomerRef.set(RefPaid)
def CostOfOrder():
    Qty1 = float(QtyWhiteWine.get())
    Qty2 = float(QtyPriceRedWine.get())
    Qty3 = float(QtyPriceOtherWine.get())
    Unt1 = float(UnitPriceWhiteWine.get())
    Unt2 = float(UnitPriceRedWine.get())
    Unt3 = float(UnitPriceOtherWine.get())

    CostWhiteWine1 = str(Qty1 *Unt1)
    CostRedWine2 = str(Qty2 * Unt2)
    CostOtherWine3 = str(Qty3 * Unt3)

    CostWhiteWine.set(CostWhiteWine1)
    CostRedWine.set(CostRedWine2)
    CostofOtherWine.set(CostOtherWine3)

    CostWhiteWine1 = (Qty1 * Unt1)
    CostRedWine2 = (Qty2 * Unt2)
    CostOtherWine3 = (Qty3 * Unt3)

    AllCost = float((Qty1*Unt1)+(Qty2*Unt2) + (Qty3 * Unt3))
    TaxAll = "SAR",(AllCost) * 0.15
    Tax.set(TaxAll)
    Subtotal.set(AllCost)
    ToatalCosting = float((AllCost) + (AllCost) * 0.15)
    TotalCost.set(ToatalCosting)
#=====================================================SET==================================================


Tops = Frame(root, bd=16, width=1350, height=50, relief=RAISED)
Tops.pack(side = TOP)

LF = Frame(root, bd=16, width=700, height=650, relief=RAISED)
LF.pack(side = LEFT)

RF = Frame(root, bd=16, width=600, height=650, relief=RAISED)
RF.pack(side = RIGHT)

Left_IN_Side_TP = Frame(LF, bd=8, width=700, height=100, relief=RAISED)
Left_IN_Side_TP.pack(side=TOP)

Left_IN_Side_LF = Frame(LF, bd=8, width=700, height=400, relief=RAISED)
Left_IN_Side_LF.pack(side=LEFT)

Right_IN_Side_TP = Frame(RF, bd=8, width=640, height=200, relief=RAISED)
Right_IN_Side_TP.pack(side=TOP)

Right_IN_Side_LF = Frame(RF, bd=8, width=306, height=400, relief=RAISED)
Right_IN_Side_LF.pack(side=LEFT)

Right_IN_Side_RF = Frame(RF, bd=8, width=300, height=400, relief=RAISED)
Right_IN_Side_RF.pack(side=RIGHT)

lbltitle = Label(Tops, font=('arial', 50, 'bold'), text="           Online Ordaring System                ", bd=10)
lbltitle.grid(row=0, column=0)
#=============================================================== Button Left Frame==============================
lblItemOrder= Label(Left_IN_Side_LF, font = ('arial',12, 'bold'), text= "Item Order", fg = "black", bd = 20 )
lblItemOrder.grid(row = 0 , column = 0)
lblItemOrder= Label(Left_IN_Side_LF, font = ('arial',12, 'bold'), text= "Qty", fg = "black", bd = 20 )
lblItemOrder.grid(row = 0 , column = 1)
lblItemOrder= Label(Left_IN_Side_LF, font = ('arial',12, 'bold'), text= "Unit Price", fg = "black", bd = 20 )
lblItemOrder.grid(row = 0 , column = 2)
lblItemOrder= Label(Left_IN_Side_LF, font = ('arial',12, 'bold'), text= "Cost Of Item", fg = "black", bd = 20 )
lblItemOrder.grid(row = 0 , column = 3)
#================================

lblCostWhiteWine= Label(Left_IN_Side_LF, font = ('arial',12, 'bold'), text= "WhiteWine", fg = "black", bd = 20 )
lblCostWhiteWine.grid(row = 1 , column = 0)
lblCostRedWine= Label(Left_IN_Side_LF, font = ('arial',12, 'bold'), text= "RedWine", fg = "black", bd = 20 )
lblCostRedWine.grid(row = 2 , column = 0)
lblCostofOtherWine= Label(Left_IN_Side_LF, font = ('arial',12, 'bold'), text= "OtherWine", fg = "black", bd = 20 )
lblCostofOtherWine.grid(row = 3 , column = 0)

#==================================
lblQtyWhiteWine= Entry(Left_IN_Side_LF, font = ('arial',12, 'bold'), textvariable= QtyWhiteWine, fg = "black", bd = 20,  width = 16, bg = "white",justify = 'left'  )
lblQtyWhiteWine.grid(row = 1 , column = 1)
lblQtyPriceRedWine= Entry(Left_IN_Side_LF, font = ('arial',12, 'bold'), textvariable= QtyPriceRedWine, fg = "black", bd = 20,  width = 16, bg = "white",justify = 'left'  )
lblQtyPriceRedWine.grid(row = 2 , column = 1)
lblQtyPriceOtherWine= Entry(Left_IN_Side_LF, font = ('arial',12, 'bold'), textvariable= QtyPriceOtherWine, fg = "black", bd = 20,  width = 16, bg = "white",justify = 'left'  )
lblQtyPriceOtherWine.grid(row = 3 , column = 1)

#=======================================

lblUnitPriceWhiteWine= Entry(Left_IN_Side_LF, font = ('arial',12, 'bold'), textvariable= UnitPriceWhiteWine, fg = "black", bd = 20,  width = 16, bg = "white",justify = 'left'  )
lblUnitPriceWhiteWine.grid(row = 1 , column = 2)
lblUnitPriceRedWine= Entry(Left_IN_Side_LF, font = ('arial',12, 'bold'), textvariable= UnitPriceRedWine, fg = "black", bd = 20,  width = 16, bg = "white",justify = 'left'  )
lblUnitPriceRedWine.grid(row = 2 , column = 2)
lblUnitPriceOtherWine= Entry(Left_IN_Side_LF, font = ('arial',12, 'bold'), textvariable= UnitPriceOtherWine, fg = "black", bd = 20,  width = 16, bg = "white",justify = 'left'  )
lblUnitPriceOtherWine.grid(row = 3 , column = 2)

#===========================================

lblCostWhiteWine= Entry(Left_IN_Side_LF, font = ('arial',12, 'bold'), textvariable= CostWhiteWine, fg = "black", bd = 20,  width = 16, bg = "white",justify = 'left'  )
lblCostWhiteWine.grid(row = 1 , column = 3)
lblCostRedWine= Entry(Left_IN_Side_LF, font = ('arial',12, 'bold'), textvariable= CostRedWine, fg = "black", bd = 20,  width = 16, bg = "white",justify = 'left'  )
lblCostRedWine.grid(row = 2 , column = 3)
lblCostofOtherWine= Entry(Left_IN_Side_LF, font = ('arial',12, 'bold'), textvariable= CostofOtherWine, fg = "black", bd = 20,  width = 16, bg = "white",justify = 'left'  )
lblCostofOtherWine.grid(row = 3 , column = 3)





#=============================================================== Top Left Frame==============================
lblCustomerName= Label(Left_IN_Side_TP, font = ('arial',12, 'bold'), text= "Customer Name", fg = "black", bd = 10, anchor = "w" )
lblCustomerName.grid(row = 0 , column = 0)
lblCustomerName= Label(Left_IN_Side_TP, font = ('arial',12, 'bold'), text= "Customer Name", fg = "black", bd = 10, anchor = "w" )
lblCustomerName.grid(row = 0 , column = 0)

lblDateOfOrder= Entry(Left_IN_Side_TP, font = ('arial',14, 'bold'), textvariable= CustomerName, fg = "black", bd = 20,  width = 43, bg = "white",justify = 'left'  )
lblDateOfOrder.grid(row = 0 , column = 1)

lblCustomerPhone= Label(Left_IN_Side_TP, font = ('arial',12, 'bold'), text= "Customer Phone", fg = "black", bd = 10, anchor = "w" )
lblCustomerPhone.grid(row = 1 , column = 0)
lblCustomerPhone= Entry(Left_IN_Side_TP, font = ('arial',14, 'bold'), textvariable= CustomerPhone, fg = "black", bd = 20,  width = 43, bg = "white",justify = 'left'  )
lblCustomerPhone.grid(row = 1 , column = 1)

lblCustomerEmail= Label(Left_IN_Side_TP, font = ('arial',12, 'bold'), text= "Customer Email", fg = "black", bd = 10, anchor = "w" )
lblCustomerEmail.grid(row = 2 , column = 0)
lblCustomerEmail= Entry(Left_IN_Side_TP, font = ('arial',14, 'bold'), textvariable= CustomerEmail, fg = "black", bd = 20,  width = 43, bg = "white",justify = 'left'  )
lblCustomerEmail.grid(row = 2 , column = 1)



#=============================================================== Top Right Frame==============================
lblDateOfOrder= Label(Right_IN_Side_TP, font = ('arial',12, 'bold'), text= "Date of Order", fg = "black", bd = 10, anchor = "w" )
lblDateOfOrder.grid(row = 0 , column = 0)
lblDateOfOrder= Entry(Right_IN_Side_TP, font = ('arial',12, 'bold'), textvariable= DateOfOrder, fg = "black", bd = 20,  width = 43, bg = "white",justify = 'left'  )
lblDateOfOrder.grid(row = 0 , column = 1)

lblTimeOfOrder= Label(Right_IN_Side_TP, font = ('arial',12, 'bold'), text= "Time Of Order", fg = "black", bd = 10, anchor = "w" )
lblTimeOfOrder.grid(row = 1 , column = 0)
lblTimeOfOrder= Entry(Right_IN_Side_TP, font = ('arial',12, 'bold'), textvariable= TimeOfOrder, fg = "black", bd = 20,  width = 43, bg = "white",justify = 'left'  )
lblTimeOfOrder.grid(row = 1 , column = 1)

lblCustomerRef= Label(Right_IN_Side_TP, font = ('arial',12, 'bold'), text= "Customer Ref", fg = "black", bd = 10, anchor = "w" )
lblCustomerRef.grid(row = 2 , column = 0)
lblCustomerRef= Entry(Right_IN_Side_TP, font = ('arial',12, 'bold'), textvariable= CustomerRef, fg = "black", bd = 20,  width = 43, bg = "white",justify = 'left'  )
lblCustomerRef.grid(row = 2 , column = 1)

#=============================================================== Right Frame==============================

lblMethodOfPayment= Label(Right_IN_Side_LF, font = ('arial',12, 'bold'), text= "MethodOfPayment", fg = "black", bd = 16, anchor = "w" )
lblMethodOfPayment.grid(row = 0 , column = 0)
cmdMethodOfPayment = ttk.Combobox(Right_IN_Side_LF,font = ('arial',12, 'bold'))
cmdMethodOfPayment ['value'] = ('','Cash','Depit Card','Visa Card','Master card')
cmdMethodOfPayment.grid(row = 0, column = 1)

lblMethodOfPayment= Label(Right_IN_Side_LF, font = ('arial',12, 'bold'), text= "Discount", fg = "black", bd = 16, anchor = "w" )
lblMethodOfPayment.grid(row = 1 , column = 0)
lblTax= Label(Right_IN_Side_LF, font = ('arial',12, 'bold'), text= "Tax", fg = "black", bd = 16, anchor = "w" )
lblTax.grid(row = 2 , column = 0)
lblSubTotal= Label(Right_IN_Side_LF, font = ('arial',12, 'bold'), text= "Sub Total", fg = "black", bd = 16, anchor = "w" )
lblSubTotal.grid(row = 3 , column = 0)
lblTotalcost= Label(Right_IN_Side_LF, font = ('arial',12, 'bold'), text= "Total cost", fg = "black", bd = 16, anchor = "w" )
lblTotalcost.grid(row = 4 , column = 0)

#================================================================Entry Right Frame================================================================

ENTDiscount= Entry(Right_IN_Side_LF, font = ('arial',12, 'bold'), textvariable= Discount, bd = 16, justify = 'left', bg = "white" )
ENTDiscount.grid(row = 1 , column = 1)
ENTTax= Entry(Right_IN_Side_LF, font = ('arial',12, 'bold'), textvariable= Tax, bd = 16, justify = 'left', bg = "white" )
ENTTax.grid(row = 2 , column = 1)
ENTSubTotal= Entry(Right_IN_Side_LF, font = ('arial',12, 'bold'), textvariable= Subtotal, bd = 16, justify = 'left', bg = "white" )
ENTSubTotal.grid(row = 3 , column = 1)
ENTTotalCost= Entry(Right_IN_Side_LF, font = ('arial',12, 'bold'), textvariable= TotalCost, bd = 16, justify = 'left', bg = "white" )
ENTTotalCost.grid(row = 4 , column = 1)

#===============================================================Button Right Frame==============================

BtnTotalCost = Button(Right_IN_Side_RF, bd = 8 , pady = 8 , fg = "black", font = ('arial',16, 'bold'), width =11, text = "Total Cost", bg = "white",command = CostOfOrder).grid(row = 0 , column = 0)
BtnRest = Button(Right_IN_Side_RF, bd = 8 , pady = 8 , fg = "black", font = ('arial',16, 'bold'), width =11, text = "Rest", bg = "white", command = Rest).grid(row = 1 , column = 0)
BtnOrderRef = Button(Right_IN_Side_RF, bd = 8 , pady = 8 , fg = "black", font = ('arial',16, 'bold'), width =11, text = "Order Ref", bg = "white", command = OrderRef).grid(row = 2 , column = 0)
BtnTotalCost = Button(Right_IN_Side_RF, bd = 8 , pady = 8 , fg = "black", font = ('arial',16, 'bold'), width =11, text = "Exit", bg = "white", command = Iexit).grid(row = 3 , column = 0)


root.mainloop()
