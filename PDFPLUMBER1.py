import pdfplumber
import re
from tkinter import *
import mysql.connector
from tkinter import filedialog

root = Tk()

RFQ_no = StringVar()
Bid_open = StringVar()
Bid_close = StringVar()
Bayer_Name = StringVar()
Bayer_Telphone = StringVar()
Req_Unit = StringVar()
Req_Qty = StringVar()

Product_Name = StringVar()

Model = StringVar()
INTERNAL_MATERIALS = StringVar()
VOLTAGE = StringVar()
SIZE = StringVar()
CONNECTION = StringVar()
STANDARD_SPECIFICATION = StringVar()
ADDITIONAL_DATA = StringVar()
AMP_HOURS = StringVar()
GROUP_SIZE = StringVar()
CELLS = StringVar()

db = mysql.connector.connect(user='root', passwd='12345678', host='localhost', database='naizak')
cursor = db.cursor()
#cursor.execute('CREATE TABLE BATTERY (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,RFQ_no Varchar(255),Model Varchar(255),Bid_open Varchar(255),Bid_close Varchar(255),Bayer_Name Varchar(255),Bayer_telephone Varchar(255),Req_Unit Varchar(255),Req_Qty Varchar(255), Product_Name Varchar(255),INTERNAL_MATERIALS Varchar(255),VOLTAGE Varchar(255),SIZE Varchar(255),ADDITIONAL_DATA Varchar(255),CONNECTION Varchar(255),STANDARD_SPECIFICATION Varchar(255),AMP_HOURS Varchar(255),GROUP_SIZE Varchar(255),CELLS Varchar(255))')
cursor.close()
db.close()

MainFram00 = Frame(root, bd=5, width=16, bg="white",relief=RIDGE)
MainFram00.grid(row=0, column=0)
lbl_title = Label(MainFram00,font=('arial', 30, 'bold'), text="RFQ_DATA", fg="black", bd=15, width=20,bg="white",relief=RIDGE, justify='left').grid()

Fram00 = Frame(root, bd=5, width=16, bg="white",relief=RIDGE)
Fram00.grid(row=1, column=0)
mytext = Text(Fram00, height=40, width=100,bd=5, bg="white",relief=RIDGE)
mytext.grid()

Fram01 = Frame(root, bd=5, width=16, bg="white",relief=RIDGE)
Fram01.grid(row=1, column=1)


Fram02 = Frame(root, bd=5, width=16, bg="white",relief=RIDGE)
Fram02.grid(row=2, column=0)

def insert_file():
    openfile = filedialog.askopenfilename()
    with pdfplumber.open(openfile) as pdf:
        page = pdf.pages[0]
        text1 = page.extract_tables()
        text2 = page.extract_table()
        text3 = page.extract_text()
        Bid_information_1 = text2[1]
        RFQ_no1 = Bid_information_1[2]
        # (RFQ_no1)
        Bid_open1 = Bid_information_1[4]
        Bid_close1 = Bid_information_1[6]
        Bid_information_2 = text2[4]
        Bayer_Name1 = Bid_information_2[3]
        Bayer_Telphone1 = Bid_information_2[5]
        Bid_information_2 = text2[4]
        Bid_information_3 = ((text1[1]))
        Bid_information_4 = ((Bid_information_3[2]))
        Req_Unit1 = Bid_information_4[3]
        Req_Qty1 = Bid_information_4[4]

        b = text1[1]
        b1 = b[3]
        # print(str(b1).replace("\n","','"))

        a1 = (text3[531:822])

        mytext.insert("1.0", "Product Name:")
        mytext.insert("2.0", b1)

        def v():
            a0 = mytext.get("1.0", END)
            a1 = re.split("\n", a0)
            a2 = mytext.get("1.0", END)
            a3 = re.split("\n", a2)
            a4 = (a0.index("ADDITIONAL DATA:"))
            ADDITIONAL_DATA01 = (a0[a4:])

            # ****************************************
            # MEMO TO VENDOR:

            # print(a3)
            # print(len(a3))
            def Convert_dict(a):
                init = iter(list1)
                res_dct = dict(zip(init, init))
                return res_dct

            # Driver code
            list1 = a3
            new = Convert_dict(list1)
            f = (mytext.get("1.0", END))
            f0 = (f.replace("None", ""))
            f1 = re.split("\n", f0)
            # print(f1)
            f2 = (len(f1))
            # (f2)
            f3 = int(f2) - int(2)
            Model_type = (f1[int(f3)])

            lbl_RFQ_no = Label(Fram01, font=('arial', 12, 'bold'), text="RFQ_no", fg="black", bd=5, width=20,
                               bg="white", relief=RIDGE, justify='left')
            lbl_RFQ_no.grid(row=0, column=0)
            ent_RFQ_no = Entry(Fram01, font=('arial', 12, 'bold'), textvariable=RFQ_no, fg="black", bd=5, width=20,
                               bg="white", relief=RIDGE, justify='left')
            ent_RFQ_no.grid(row=0, column=1)
            ent_RFQ_no.insert(0, RFQ_no1)
            # (ent_RFQ_no.get())

            lbl_BID_OPEN = Label(Fram01, font=('arial', 12, 'bold'), text="BID_OPEN", fg="black", bd=5, width=20,
                                 bg="white", relief=RIDGE, justify='left')
            lbl_BID_OPEN.grid(row=1, column=0)
            ent_BID_OPEN = Entry(Fram01, font=('arial', 12, 'bold'), textvariable=Bid_open, fg="black", bd=5, width=20,
                                 bg="white", relief=RIDGE, justify='left')
            ent_BID_OPEN.grid(row=1, column=1)
            ent_BID_OPEN.insert(0, Bid_open1)
            # (ent_BID_OPEN.get())

            lbl_Bid_close = Label(Fram01, font=('arial', 12, 'bold'), text="Bid_close", fg="black", bd=5, width=20,
                                  bg="white", relief=RIDGE, justify='left')
            lbl_Bid_close.grid(row=2, column=0)
            ent_Bid_close = Entry(Fram01, font=('arial', 12, 'bold'), textvariable=Bid_close, fg="black", bd=5,
                                  width=20, bg="white", relief=RIDGE, justify='left')
            ent_Bid_close.grid(row=2, column=1)
            ent_Bid_close.insert(0, Bid_close1)
            # (ent_Bid_close.get())

            lbl_BAYER_NAME = Label(Fram01, font=('arial', 12, 'bold'), text="BAYER_NAME", fg="black", bd=5, width=20,
                                   bg="white", relief=RIDGE, justify='left')
            lbl_BAYER_NAME.grid(row=3, column=0)
            ent_BAYER_NAME = Entry(Fram01, font=('arial', 12, 'bold'), textvariable=Bayer_Name, fg="black", bd=5,
                                   width=20, bg="white", relief=RIDGE, justify='left')
            ent_BAYER_NAME.grid(row=3, column=1)
            ent_BAYER_NAME.insert(0, Bayer_Name1)
            # (ent_BAYER_NAME.get())

            lbl_BAYER_TELPHONE = Label(Fram01, font=('arial', 12, 'bold'), text="BAYER_TELPHONE", fg="black", bd=5,
                                       width=20, bg="white", relief=RIDGE, justify='left')
            lbl_BAYER_TELPHONE.grid(row=4, column=0)
            ent_BAYER_TELPHONE = Entry(Fram01, font=('arial', 12, 'bold'), textvariable=Bayer_Telphone, fg="black",
                                       bd=5, width=20, bg="white", relief=RIDGE, justify='left')
            ent_BAYER_TELPHONE.grid(row=4, column=1)
            ent_BAYER_TELPHONE.insert(0, Bayer_Telphone1)
            # (ent_BAYER_TELPHONE.get())

            lbl_REQ_UNIT = Label(Fram01, font=('arial', 12, 'bold'), text="REQ_UNIT", fg="black", bd=5, width=20,
                                 bg="white", relief=RIDGE, justify='left')
            lbl_REQ_UNIT.grid(row=5, column=0)
            ent_REQ_UNIT = Entry(Fram01, font=('arial', 12, 'bold'), textvariable=Req_Unit, fg="black", bd=5, width=20,
                                 bg="white", relief=RIDGE, justify='left')
            ent_REQ_UNIT.grid(row=5, column=1)
            ent_REQ_UNIT.insert(0, Req_Unit1)
            # (ent_REQ_UNIT.get())

            lbl_REQ_QTY = Label(Fram01, font=('arial', 12, 'bold'), text="REQ_QTY", fg="black", bd=5, width=20,
                                bg="white", relief=RIDGE, justify='left')
            lbl_REQ_QTY.grid(row=6, column=0)
            ent_REQ_QTY = Entry(Fram01, font=('arial', 12, 'bold'), textvariable=Req_Qty, fg="black", bd=5, width=20,
                                bg="white", relief=RIDGE, justify='left')
            ent_REQ_QTY.grid(row=6, column=1)
            ent_REQ_QTY.insert(0, Req_Qty1)
            # (ent_REQ_QTY.get())
            # (type(ent_REQ_QTY.get()))

            lbl_Product_Name = Label(Fram01, font=('arial', 12, 'bold'), text="Product_Name", fg="black", bd=5,
                                     width=20, bg="white", relief=RIDGE)
            lbl_Product_Name.grid(row=7, column=0)
            ent_Product_Name = Entry(Fram01, font=('arial', 12, 'bold'), textvariable=Product_Name, fg="black", bd=5,
                                     width=40, bg="white", relief=RIDGE)
            ent_Product_Name.grid(row=7, column=1)
            a0 = (new.get("Product Name:"))
            ent_Product_Name.insert(0, a0)
            # (ent_Product_Name.get())
            lbl_Model1 = Label(Fram01, font=('arial', 12, 'bold'), text="Model", fg="black", bd=5, width=20, bg="white",
                               relief=RIDGE, justify='left')
            lbl_Model1.grid(row=8, column=0)
            ent_Model1 = Entry(Fram01, font=('arial', 12, 'bold'), textvariable=Model, fg="black", bd=5, width=40,
                               bg="white", relief=RIDGE, justify='left')
            ent_Model1.grid(row=8, column=1)
            ent_Model1.insert(0, Model_type)
            # (ent_Model1.get())
            for i in new:
                if i == "INTERNAL MATERIAL/S:":
                    lbl_INTERNAL_MATERIALS = Label(Fram01, font=('arial', 12, 'bold'), text="INTERNAL_MATERIALS",
                                                   fg="black", bd=5, width=20, bg="white", relief=RIDGE)
                    lbl_INTERNAL_MATERIALS.grid(row=9, column=0)
                    ent_INTERNAL_MATERIALS = Entry(Fram01, font=('arial', 12, 'bold'), textvariable=INTERNAL_MATERIALS,
                                                   fg="black", bd=5, width=40, bg="white", relief=RIDGE)
                    ent_INTERNAL_MATERIALS.grid(row=9, column=1)
                    a0 = (new.get("INTERNAL MATERIAL/S:"))
                    ent_INTERNAL_MATERIALS.insert(0, a0)

                    # (ent_INTERNAL_MATERIALS.get())
                elif i == "CONNECTION:":
                    lbl_CONNECTION = Label(Fram01, font=('arial', 12, 'bold'), text="CONNECTION", fg="black", bd=5,
                                           width=20, bg="white", relief=RIDGE, justify='left')
                    lbl_CONNECTION.grid(row=10, column=0)
                    ent_CONNECTION = Entry(Fram01, font=('arial', 12, 'bold'), textvariable=CONNECTION, fg="black",
                                           bd=5,
                                           width=40, bg="white", relief=RIDGE, justify='left')
                    ent_CONNECTION.grid(row=10, column=1)
                    a0 = (new.get("CONNECTION:"))
                    ent_CONNECTION.insert(0, a0)
                    # (ent_CONNECTION.get())
                elif i == "VOLTAGE:":
                    lbl_VOLTAGE = Label(Fram01, font=('arial', 12, 'bold'), text="VOLTAGE", fg="black", bd=5, width=20,
                                        bg="white", relief=RIDGE, justify='left')
                    lbl_VOLTAGE.grid(row=11, column=0)
                    ent_VOLTAGE = Entry(Fram01, font=('arial', 12, 'bold'), textvariable=VOLTAGE, fg="black", bd=5,
                                        width=40, bg="white", relief=RIDGE, justify='left')
                    ent_VOLTAGE.grid(row=11, column=1)
                    a0 = (new.get("VOLTAGE:"))
                    ent_VOLTAGE.insert(0, a0)
                    # (ent_VOLTAGE.get())
                elif i == "STANDARD/SPECIFICATION:":
                    lbl_STANDARD_SPECIFICATION = Label(Fram01, font=('arial', 12, 'bold'),
                                                       text="STANDARD_SPECIFICATION",
                                                       fg="black", bd=5, width=20, bg="white", relief=RIDGE,
                                                       justify='left')
                    lbl_STANDARD_SPECIFICATION.grid(row=12, column=0)
                    ent_STANDARD_SPECIFICATION = Entry(Fram01, font=('arial', 12, 'bold'),
                                                       textvariable=STANDARD_SPECIFICATION, fg="black", bd=5, width=40,
                                                       bg="white", relief=RIDGE, justify='left')
                    ent_STANDARD_SPECIFICATION.grid(row=12, column=1)
                    a0 = (new.get("STANDARD/SPECIFICATION:"))
                    ent_STANDARD_SPECIFICATION.insert(0, a0)
                    # (ent_STANDARD_SPECIFICATION.get())
                elif i == "SIZE:":
                    lbl_SIZE = Label(Fram01, font=('arial', 12, 'bold'), text="SIZE", fg="black", bd=5, width=20,
                                     bg="white", relief=RIDGE, justify='left')
                    lbl_SIZE.grid(row=13, column=0)
                    ent_SIZE = Entry(Fram01, font=('arial', 12, 'bold'), textvariable=SIZE, fg="black", bd=5, width=40,
                                     bg="white", relief=RIDGE, justify='left')
                    ent_SIZE.grid(row=13, column=1)
                    a0 = (new.get("SIZE:"))
                    ent_SIZE.insert(0, a0)
                    # (ent_SIZE.get())
                elif i == "AMP HOURS:":
                    lbl_AMP_HOURS = Label(Fram01, font=('arial', 12, 'bold'), text="AMP_HOURS", fg="black", bd=5,
                                          width=20,
                                          bg="white", relief=RIDGE, justify='left')
                    lbl_AMP_HOURS.grid(row=14, column=0)
                    ent_AMP_HOURS = Entry(Fram01, font=('arial', 12, 'bold'), textvariable=AMP_HOURS, fg="black", bd=5,
                                          width=40, bg="white", relief=RIDGE, justify='left')
                    ent_AMP_HOURS.grid(row=14, column=1)
                    a0 = (new.get("AMP HOURS:"))
                    ent_AMP_HOURS.insert(0, a0)
                    # (type(ent_AMP_HOURS.get()))
                elif i == "GROUP SIZE:":
                    lbl_GROUP_SIZE = Label(Fram01, font=('arial', 12, 'bold'), text="GROUP_SIZE", fg="black", bd=5,
                                           width=20, bg="white", relief=RIDGE, justify='left')
                    lbl_GROUP_SIZE.grid(row=15, column=0)
                    ent_GROUP_SIZE = Entry(Fram01, font=('arial', 12, 'bold'), textvariable=GROUP_SIZE, fg="black",
                                           bd=5,
                                           width=40, bg="white", relief=RIDGE, justify='left')
                    ent_GROUP_SIZE.grid(row=15, column=1)
                    a0 = (new.get("GROUP SIZE:"))
                    ent_GROUP_SIZE.insert(0, a0)
                    # (ent_GROUP_SIZE.get())
                elif i == "CELLS:":
                    lbl_CELLS = Label(Fram01, font=('arial', 12, 'bold'), text="CELLS", fg="black", bd=5, width=20,
                                      bg="white", relief=RIDGE, justify='left')
                    lbl_CELLS.grid(row=16, column=0)
                    ent_CELLS = Entry(Fram01, font=('arial', 12, 'bold'), textvariable=CELLS, fg="black", bd=5,
                                      width=40, bg="white", relief=RIDGE, justify='left')
                    ent_CELLS.grid(row=16, column=1)
                    a0 = (new.get("CELLS:"))
                    ent_CELLS.insert(0, a0)

                    # (ent_CELLS.get())
                elif i == "ADDITIONAL DATA:":
                    lbl_ADDITIONAL_DATA = Label(Fram01, font=('arial', 12, 'bold'), text="ADDITIONAL_DATA", fg="black",
                                                bd=5, width=20, bg="white", relief=RIDGE, justify='left')
                    lbl_ADDITIONAL_DATA.grid(row=17, column=0)
                    ent_ADDITIONAL_DATA = Entry(Fram01, font=('arial', 12, 'bold'), textvariable=ADDITIONAL_DATA,
                                                fg="black", bd=5, width=40, relief=RIDGE, bg="white", justify='left')
                    ent_ADDITIONAL_DATA.grid(row=17, column=1)
                    # a0 = (new.get("ADDITIONAL DATA:"))
                    ent_ADDITIONAL_DATA.insert(0, ADDITIONAL_DATA01)

        btn = Button(Fram02, font=('arial', 12, 'bold'), text="Insert to Tkinter", fg="black", bd=5, width=20,bg="white", relief=RIDGE, justify='left', command=v)
        btn.grid(row=0, column=1)




btn1 = Button(Fram02,font=('arial', 12, 'bold'), text="Insert to MySql", fg="black", bd=5, width=20, bg="white",relief=RIDGE, justify='left',command=insert_file)
btn1.grid(row=0, column=2)


def delete():
    Entry.delete(0,END)


btn = Button(Fram02, font=('arial', 12, 'bold'), text="DELETE", fg="black", bd=5,
             width=20, bg="white", relief=RIDGE, justify='left', command=delete)
btn.grid(row=0, column=3)

root.mainloop()



