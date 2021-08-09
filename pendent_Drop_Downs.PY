from tkinter import *
from tkinter import ttk

bid = Tk()
bid.geometry("400x400")

Braeker_type = ["ACB","MCB","MCCB",""]

ACB = ["1600","2500","1200","2000"]
MCCB = ["500","400","800","1000"]
MCB = ["100","50","40","30"]




def choess(e):
    if (list1.get() == "ACB"):
        list2.config(value =ACB)
    if (list1.get() == "MCB"):
        list2.config(value =MCB)
    if (list1.get() == "MCCB"):
        list2.config(value =MCCB)

list1 = ttk.Combobox(bid, value = Braeker_type)
list1.bind("<<ComboboxSelected>>", choess)
list1.pack()

list2 = ttk.Combobox(bid, value=ACB)
list2.pack()

listbox1 = Listbox(bid)
listbox1.pack()
listbox2 = Listbox(bid)
listbox2.pack()


def lisbox1(e):
    listbox2.delete(0,END)
    if listbox1.get(ANCHOR) == "ACB":
        for item1 in ACB:
            listbox2.insert(END, item1)
    if listbox1.get(ANCHOR) == "MCB":
        for item1 in MCB:
            listbox2.insert(END, item1)
    if listbox1.get(ANCHOR) == "MCCB":
       for item1 in MCCB:
            listbox2.insert(END, item1)


for item in Braeker_type:
    listbox1.insert(END,item)



listbox1.bind("<<ListboxSelect>>", lisbox1)



bid.mainloop()
