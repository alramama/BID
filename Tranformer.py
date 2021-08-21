from tkinter import *
import tkinter.messagebox
import time
import datetime
import tempfile, os
import self as self
from tkinter import filedialog
import PyPDF2
from PyDictionary import PyDictionary
import json


BID = Tk()
BID.geometry("1500x700+0+0")
BID.title("BID INFORMATION")


MOUNT = StringVar()
KVA_RATING = StringVar()
PHASE = StringVar()
APPLICATION_PRIMARY_VOLT = StringVar()
ACTUAL_PRIMARY_VOLT = StringVar()
SECONDARY_VOLT = StringVar()
PRIMARY_BIL_RATING = StringVar()
SECONDARY_BIL_RATINGS = StringVar()
VECTOR_GROUP = StringVar()
PRIMARY_BUSHINGS = StringVar()
SECONDARY_BUSHINGS = StringVar()
PRIMARY_CONNECTIONS = StringVar()
SECONDARY_CONNECTIONS = StringVar()
STANDARD_SPECIFICATION = StringVar()

BID_MainFrame = Frame(BID, bd=16, width=1350, height=600, relief=RIDGE)
BID_MainFrame.grid(row=0, column=0)
"""
data =MOUNT:
PAD;
KVA RATING:
1500 KVA;
PHASE:
3 PH;
APPLICATION PRIMARY VOLT:
34500 V AC;
ACTUAL PRIMARY VOLT:
34.5K V AC;
SECONDARY VOLT:
4160/480 V AC;
FREQUENCY:
60 HZ;
PRIMARY BIL RATING:
150 KV;
SECONDARY BIL RATINGS:
30 KV;
VECTOR GROUP:
YYYN0;
PRIMARY BUSHINGS:
(3) LOAD BREAK BUSHING INSERT;
SECONDARY BUSHINGS:
(3) LOAD BREAK BUSHING INSERT FOR 4160 V, (4) ENCLOSED 4-HOLES SPADE TERMINATI ONS FOR 480 V;

clean1 = data.replace(";","")
clean2 = clean1.replace(":"," ")
clean3 = clean2.replace(","," ")
#clean4 = clean3.strip()
clean4 = clean3.split("\n")
"""
FRAM_BID_Emp_Ent = Frame(BID_MainFrame, bd=16, width=100, height=80, relief=RIDGE)
FRAM_BID_Emp_Ent.grid(row=1, column=0)

lbl_MOUNT =                     Label(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text="MOUNT",                     fg="black", bd=5).grid(row=0, column=0, sticky=W)
lbl_KVA_RATING =                Label(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text="KVA_RATING",                fg="black", bd=5).grid(row=1, column=0, sticky=W)
lbl_PHASE =                     Label(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text="PHASE",                     fg="black", bd=5).grid(row=2, column=0, sticky=W)
lbl_APPLICATION_PRIMARY_VOLT =  Label(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text="APPLICATION_PRIMARY_VOLT",  fg="black", bd=5).grid(row=3, column=0, sticky=W)
lbl_ACTUAL_PRIMARY_VOLT =       Label(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text="ACTUAL_PRIMARY_VOLT",       fg="black", bd=5).grid(row=4, column=0, sticky=W)
lbl_SECONDARY_VOLT =            Label(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text="SECONDARY_VOLT",            fg="black", bd=5).grid(row=5, column=0, sticky=W)
lbl_PRIMARY_BIL_RATING =        Label(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text="PRIMARY_BIL_RATING",        fg="black", bd=5).grid(row=6, column=0, sticky=W)
lbl_SECONDARY_BIL_RATINGS =     Label(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text="SECONDARY_BIL_RATINGS",     fg="black", bd=5).grid(row=7, column=0, sticky=W)
lbl_VECTOR_GROUP =              Label(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text="VECTOR_GROUP",              fg="black", bd=5).grid(row=8, column=0, sticky=W)
lbl_PRIMARY_BUSHINGS =          Label(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text="PRIMARY_BUSHINGS",          fg="black", bd=5).grid(row=9, column=0, sticky=W)
lbl_SECONDARY_BUSHINGS =        Label(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text="SECONDARY_BUSHINGS",        fg="black", bd=5).grid(row=10, column=0, sticky=W)
lbl_PRIMARY_CONNECTIONS =       Label(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text="PRIMARY_CONNECTIONS",       fg="black", bd=5).grid(row=11, column=0, sticky=W)
lbl_SECONDARY_CONNECTIONS =     Label(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text="SECONDARY_CONNECTIONS",     fg="black", bd=5).grid(row=12, column=0, sticky=W)
lbl_STANDARD_SPECIFICATION =    Label(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text="STANDARD_SPECIFICATION",    fg="black", bd=5).grid(row=13, column=0, sticky=W)

ent_MOUNT =                     Entry(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text=MOUNT,                     fg="black", bd=5)
ent_MOUNT.grid(row=0, column=1, sticky=W)
ent_KVA_RATING =                Entry(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text=KVA_RATING,                fg="black", bd=5)
ent_KVA_RATING.grid(row=1, column=1, sticky=W)
ent_PHASE =                     Entry(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text=PHASE,                     fg="black", bd=5)
ent_PHASE.grid(row=2, column=1, sticky=W)
ent_APPLICATION_PRIMARY_VOLT =  Entry(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text=APPLICATION_PRIMARY_VOLT,  fg="black", bd=5)
ent_APPLICATION_PRIMARY_VOLT.grid(row=3, column=1, sticky=W)
ent_ACTUAL_PRIMARY_VOLT =       Entry(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text=ACTUAL_PRIMARY_VOLT,       fg="black", bd=5)
ent_ACTUAL_PRIMARY_VOLT.grid(row=4, column=1, sticky=W)
ent_SECONDARY_VOLT =            Entry(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text=SECONDARY_VOLT,            fg="black", bd=5)
ent_SECONDARY_VOLT.grid(row=5, column=1, sticky=W)
ent_PRIMARY_BIL_RATING =        Entry(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text=PRIMARY_BIL_RATING,        fg="black", bd=5)
ent_PRIMARY_BIL_RATING.grid(row=6, column=1, sticky=W)
ent_SECONDARY_BIL_RATINGS =     Entry(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text=SECONDARY_BIL_RATINGS,     fg="black", bd=5)
ent_SECONDARY_BIL_RATINGS.grid(row=7, column=1, sticky=W)
ent_VECTOR_GROUP =              Entry(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text=VECTOR_GROUP,              fg="black", bd=5)
ent_VECTOR_GROUP.grid(row=8, column=1, sticky=W)
ent_PRIMARY_BUSHINGS =          Entry(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text=PRIMARY_BUSHINGS,          fg="black", bd=5)
ent_PRIMARY_BUSHINGS.grid(row=9, column=1, sticky=W)
ent_SECONDARY_BUSHINGS =        Entry(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text=SECONDARY_BUSHINGS,        fg="black", bd=5)
ent_SECONDARY_BUSHINGS.grid(row=10, column=1, sticky=W)
ent_PRIMARY_CONNECTIONS =       Entry(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text=PRIMARY_CONNECTIONS,       fg="black", bd=5)
ent_PRIMARY_CONNECTIONS.grid(row=11, column=1, sticky=W)
ent_SECONDARY_CONNECTIONS =     Entry(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text=SECONDARY_CONNECTIONS,     fg="black", bd=5)
ent_SECONDARY_CONNECTIONS.grid(row=12, column=1, sticky=W)
ent_STANDARD_SPECIFICATION =    Entry(FRAM_BID_Emp_Ent, font=('arial', 12, 'bold'), text=STANDARD_SPECIFICATION,    fg="black", bd=5)
ent_STANDARD_SPECIFICATION.grid(row=13, column=1, sticky=W)


FRAM_BID_Emp_text = Frame(BID_MainFrame, bd=16, width=100, height=80, relief=RIDGE)
FRAM_BID_Emp_text.grid(row=1, column=1)
ent_SOW_list = Text(FRAM_BID_Emp_text, font=('arial', 12, 'bold'), width= 50,height=30, fg="black", bd=5)
ent_SOW_list.grid(row=6, column=1, sticky=W)
#ent_SOW_list.insert("1.0",clean4)
ent_SOW_dict = Text(FRAM_BID_Emp_text, font=('arial', 12, 'bold'), width= 50,height=30, fg="black", bd=5)
ent_SOW_dict.grid(row=6, column=2, sticky=W)

def get():
    #A = '{ "name":"John", "age":30, "city":"New York"}'
    '''
    A = ent_SOW_list.get("1.0",END)
    clean1 = A.replace(";", "")
    clean2 = clean1.replace(":", " ")
    clean3 = clean2.replace(",", " ")
    clean4 = clean3.split("\n")
    print(clean4)
    '''
    A = ent_SOW_list.get("1.0",END)
    clean2 = A.replace(":", " ")
    clean0 = clean2.splitlines()
    print(clean0)
    #clean2 = clean1.replace(":", " ")
    #clean3 = clean2.replace(",", " ")
    #print(clean4)


    def Convert(lst):
        res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
        return res_dct

    lst = clean0
    Z = (Convert(lst))
    print(Z)
    print((Z.keys()))
    MOUNT = Z["MOUNT "]
    KVA_RATING = Z["KVA RATING "]
    PHASE = Z["PHASE "]
    APPLICATION_PRIMARY_VOLT = Z["APPLICATION PRIMARY VOLT "]
    ACTUAL_PRIMARY_VOLT = Z["ACTUAL PRIMARY VOLT "]
    SECONDARY_VOLT = Z["SECONDARY VOLT "]

    ent_MOUNT.insert(END, MOUNT)
    ent_KVA_RATING.insert(END, KVA_RATING)
    ent_PHASE.insert(END, PHASE)
    ent_APPLICATION_PRIMARY_VOLT.insert(END, APPLICATION_PRIMARY_VOLT)
    ent_ACTUAL_PRIMARY_VOLT.insert(END, ACTUAL_PRIMARY_VOLT)
    ent_SECONDARY_VOLT.insert(END, SECONDARY_VOLT)

    #b = A(["brand"])
    #print(str(b))

    #C = type(A)
    #print(C)

"""
def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct
def clean():
    clean0 = ent_SOW_list.get("1.0", END)
    clean1 = clean0.replace(";", "")
    clean2 = clean1.replace(":", " ")
    clean3 = clean2.replace(",", " ")
    clean4 = clean3.replace("}", "")
    clean5 = clean4.replace("{","")
    clean6 = clean5.split("\n")
    clean7 = ent_SOW_dict.insert("1.0", clean6)
    lst = ent_SOW_dict.get("1.0",END)
    Z = (Convert(lst))
    print(Z)
"""





'''
MOUNT = Z["MOUNT "]
KVA_RATING = Z["KVA RATING "]
PHASE= Z["PHASE "]
APPLICATION_PRIMARY_VOLT= Z["APPLICATION PRIMARY VOLT "]
ACTUAL_PRIMARY_VOLT= Z["ACTUAL PRIMARY VOLT "]
SECONDARY_VOLT= Z["SECONDARY VOLT "]
#FREQUENCY= Z["FREQUENCY "]
PRIMARY_BIL_RATING= Z["PRIMARY BIL RATING "]
SECONDARY_BIL_RATINGS= Z["SECONDARY BIL RATINGS "]
VECTOR_GROUP= Z["VECTOR GROUP "]
PRIMARY_BUSHINGS= Z["PRIMARY BUSHINGS "]
SECONDARY_BUSHINGS= Z["SECONDARY BUSHINGS "]

ent_MOUNT.insert(END,MOUNT)
ent_KVA_RATING.insert(END,KVA_RATING)
ent_PHASE.insert(END,PHASE)
ent_APPLICATION_PRIMARY_VOLT.insert(END,APPLICATION_PRIMARY_VOLT)
ent_ACTUAL_PRIMARY_VOLT.insert(END,ACTUAL_PRIMARY_VOLT)
ent_SECONDARY_VOLT.insert(END,SECONDARY_VOLT)
ent_PRIMARY_BIL_RATING.insert(END,PRIMARY_BIL_RATING)
ent_SECONDARY_BIL_RATINGS.insert(END,SECONDARY_BIL_RATINGS)
ent_VECTOR_GROUP.insert(END,VECTOR_GROUP)
ent_PRIMARY_BUSHINGS.insert(END,PRIMARY_BUSHINGS)
'''

FRAM_BID_Emp_BTN = Frame(BID_MainFrame, bd=16, width=100, height=80, relief=RIDGE)
FRAM_BID_Emp_BTN.grid(row=3, column=0)
#btn = Button(FRAM_BID_Emp_BTN,bd = 8 , pady = 8 , fg = "black", font = ('arial',16, 'bold'), width =11, text = "insert_sow", bg = "white", command = insert)
#btn.grid(row = 0 , column = 0)
btn = Button(FRAM_BID_Emp_BTN,bd = 8 , pady = 8 , fg = "black", font = ('arial',16, 'bold'), width =11, text = "get", bg = "white", command = get)
btn.grid(row = 0 , column = 0)

btn = Button(FRAM_BID_Emp_BTN,bd = 8 , pady = 8 , fg = "black", font = ('arial',16, 'bold'), width =11, text = "convert", bg = "white")
btn.grid(row = 0 , column = 1)


BID.mainloop()
