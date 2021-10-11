import pdfplumber
import re
from tkinter import *
import mysql.connector

root = Tk()



INTERNAL_MATERIALS = StringVar()
Product_Name = StringVar()
VOLTAGE = StringVar()
SIZE = StringVar()
CONNECTION = StringVar()
STANDARD_SPECIFICATION = StringVar()
ADDITIONAL_DATA = StringVar()
RFQ_no = StringVar()
Bid_open = StringVar()
Bid_close = StringVar()
Bayer_Name = StringVar()
Bayer_Telphone = StringVar()
Req_Unit = StringVar()
Req_Qty = StringVar()

db = mysql.connector.connect(user='root',passwd='12345678',host='localhost',database='naizak')
cursor = db.cursor()
#cursor.execute('CREATE TABLE BATTERY7 (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, Product_Name Varchar(255),INTERNAL_MATERIALS Varchar(255),VOLTAGE Varchar(255),SIZE Varchar(255),ADDITIONAL_DATA Varchar(255),CONNECTION Varchar(255),STANDARD_SPECIFICATION Varchar(255))')
cursor.close()
db.close()


Fram00 = Frame(root,  bd=20, width=16, bg="white")
Fram00.grid(row=0, column=0)

Fram01 = Frame(root,  bd=20, width=16, bg="white")
Fram01.grid(row=0, column=1)

Fram02 = Frame(root,  bd=20, width=16, bg="white")
Fram02.grid(row=1, column=0)



with pdfplumber.open("2.pdf") as pdf:
  page = pdf.pages[0]
  text1 = page.extract_tables()
  text2 = page.extract_table()
  text3 = page.extract_text()
  Bid_information_1 = text2[1]
  RFQ_no = Bid_information_1[2]
  Bid_open = Bid_information_1[4]
  Bid_close = Bid_information_1[6]
  Bid_information_2 = text2[4]
  Bayer_Name = Bid_information_2[3]
  Bayer_Telphone = Bid_information_2[5]
  Bid_information_2 = text2[4]
  Bid_information_3 = ((text1[1]))
  Bid_information_4 = ((Bid_information_3[2]))
  Req_Unit = Bid_information_4[2]
  Req_Qty =  Bid_information_4[3]

  b = text1[1]
  b1 =b[3]
  #print(str(b1).replace("\n","','"))

  a1 = (text3[531:822])

  mytext = Text(Fram00, height = 40)
  mytext.grid()
  mytext.insert("1.0",b1)


  def v():
      a0 = mytext.get("1.0", END)
      a1 = re.split("\n", a0)
      a2 = mytext.get("1.0", END)
      a3 = re.split("\n", a2)

      # print(a3)
      # print(len(a3))
      def Convert_dict(a):
          init = iter(list1)
          res_dct = dict(zip(init, init))
          return res_dct

      # Driver code
      list1 = a3
      new = Convert_dict(list1)

      lbl_RFQ_NO = Label(Fram01, font=('arial', 12, 'bold'), text="RFQ_NO", fg="black", bd=20, width=16, bg="white",justify='left')
      lbl_RFQ_NO.grid(row=1, column=0)
      ent_RFQ_NO = Entry(Fram01, font=('arial', 12, 'bold'), textvariable=RFQ_no, fg="black", bd=20, width=40,bg="white", justify='left')
      ent_RFQ_NO.grid(row=1, column=1)
      ent_RFQ_NO.insert(0, RFQ_no)
      print(ent_RFQ_NO.get())

      lbl_BID_OPEN = Label(Fram01, font=('arial', 12, 'bold'), text="BID_OPEN", fg="black", bd=20, width=40,bg="white", justify='left')
      lbl_BID_OPEN.grid(row=2, column=0)
      ent_BID_OPEN = Entry(Fram01, font=('arial', 12, 'bold'), textvariable=Bid_open, fg="black", bd=20, width=40,
                           bg="white", justify='left')
      ent_BID_OPEN.grid(row=2, column=1)
      ent_BID_OPEN.insert(0, Bid_close)
      print(ent_BID_OPEN.get())

      lbl_BAYER_NAME = Label(Fram01, font=('arial', 12, 'bold'), text="BAYER_NAME", fg="black", bd=20, width=40,
                             bg="white", justify='left')
      lbl_BAYER_NAME.grid(row=3, column=0)
      ent_BAYER_NAME = Entry(Fram01, font=('arial', 12, 'bold'), textvariable=Bayer_Name, fg="black", bd=20, width=40,
                             bg="white", justify='left')
      ent_BAYER_NAME.grid(row=3, column=1)
      ent_BAYER_NAME.insert(0, Bayer_Name)
      print(ent_BAYER_NAME.get())

      lbl_BAYER_TELPHONE = Label(Fram01, font=('arial', 12, 'bold'), text="BAYER_TELPHONE", fg="black", bd=20,
                                 width=40, bg="white", justify='left')
      lbl_BAYER_TELPHONE.grid(row=4, column=0)
      ent_BAYER_TELPHONE = Entry(Fram01, font=('arial', 12, 'bold'), textvariable=Bayer_Telphone, fg="black", bd=20,
                                 width=40, bg="white", justify='left')
      ent_BAYER_TELPHONE.grid(row=4, column=1)
      ent_BAYER_TELPHONE.insert(0, Bayer_Telphone)
      print(ent_BAYER_TELPHONE.get())

      lbl_REQ_UNIT = Label(Fram01, font=('arial', 12, 'bold'), text="REQ_UNIT", fg="black", bd=20, width=40,
                           bg="white", justify='left')
      lbl_REQ_UNIT.grid(row=5, column=0)
      ent_REQ_UNIT = Entry(Fram01, font=('arial', 12, 'bold'), textvariable=Req_Unit, fg="black", bd=20, width=40,
                           bg="white", justify='left')
      ent_REQ_UNIT.grid(row=5, column=1)
      ent_REQ_UNIT.insert(0, Req_Unit)
      print(ent_REQ_UNIT.get())

      lbl_REQ_QTY = Label(Fram01, font=('arial', 12, 'bold'), text="REQ_QTY", fg="black", bd=20, width=40, bg="white",
                          justify='left')
      lbl_REQ_QTY.grid(row=6, column=0)
      ent_REQ_QTY = Entry(Fram01, font=('arial', 12, 'bold'), textvariable=Req_Qty, fg="black", bd=20, width=40,
                          bg="white", justify='left')
      ent_REQ_QTY.grid(row=6, column=1)
      ent_REQ_QTY.insert(0, Req_Qty)
      print(ent_REQ_QTY.get())

      # ---------------------------------------------INTERNAL_MATERIALS
      # 01
      lbl_INTERNAL_MATERIALS = Label(Fram01, font=('arial', 12, 'bold'), text="INTERNAL_MATERIALS", fg="black", bd=20,
                                     width=40, bg="white", justify='left')
      lbl_INTERNAL_MATERIALS.grid(row=7, column=0)
      ent_INTERNAL_MATERIALS = Entry(Fram01, font=('arial', 12, 'bold'), textvariable=INTERNAL_MATERIALS, fg="black",
                                     bd=20, width=40, bg="white", justify='left')
      ent_INTERNAL_MATERIALS.grid(row=7, column=1)
      a0 = (new.get("INTERNAL MATERIAL/S:"))
      ent_INTERNAL_MATERIALS.insert(0, a0)
      print(ent_INTERNAL_MATERIALS.get())

      # 02
      lbl_VOLTAGE = Label(Fram01, font=('arial', 12, 'bold'), text="VOLTAGE", fg="black", bd=20, width=40, bg="white",
                          justify='left')
      lbl_VOLTAGE.grid(row=8, column=0)
      ent_VOLTAGE = Entry(Fram01, font=('arial', 12, 'bold'), textvariable=VOLTAGE, fg="black", bd=20, width=40,
                          bg="white", justify='left')
      ent_VOLTAGE.grid(row=8, column=1)
      a0 = (new.get("VOLTAGE:"))
      ent_VOLTAGE.insert(0, a0)
      print(ent_VOLTAGE.get())
      # 03
      lbl_SIZE = Label(Fram01, font=('arial', 12, 'bold'), text="SIZE", fg="black", bd=20, width=40, bg="white",
                       justify='left')
      lbl_SIZE.grid(row=9, column=0)
      ent_SIZE = Entry(Fram01, font=('arial', 12, 'bold'), textvariable=SIZE, fg="black", bd=20, width=40, bg="white",
                       justify='left')
      ent_SIZE.grid(row=9, column=1)
      a0 = (new.get("SIZE:"))
      ent_SIZE.insert(0, a0)
      print(ent_SIZE.get())
      # 04
      lbl_CONNECTION = Label(Fram01, font=('arial', 12, 'bold'), text="CONNECTION", fg="black", bd=20, width=40,
                             bg="white", justify='left')
      lbl_CONNECTION.grid(row=10, column=0)
      ent_CONNECTION = Entry(Fram01, font=('arial', 12, 'bold'), textvariable=CONNECTION, fg="black", bd=20, width=40,
                             bg="white", justify='left')
      ent_CONNECTION.grid(row=10, column=1)
      a0 = (new.get("CONNECTION:"))
      ent_CONNECTION.insert(0, a0)
      print(ent_CONNECTION.get())
      # 05
      lbl_STANDARD_SPECIFICATION = Label(Fram01, font=('arial', 12, 'bold'), text="STANDARD_SPECIFICATION", fg="black",
                                         bd=20, width=40, bg="white", justify='left')
      lbl_STANDARD_SPECIFICATION.grid(row=11, column=0)
      ent_STANDARD_SPECIFICATION = Entry(Fram01, font=('arial', 12, 'bold'), textvariable=STANDARD_SPECIFICATION,
                                         fg="black", bd=20, width=40, bg="white", justify='left')
      ent_STANDARD_SPECIFICATION.grid(row=11, column=1)
      a0 = (new.get("STANDARD/SPECIFICATION:"))
      ent_STANDARD_SPECIFICATION.insert(0, a0)
      print(ent_STANDARD_SPECIFICATION.get())
      # 06
      lbl_ADDITIONAL_DATA = Label(Fram01, font=('arial', 12, 'bold'), text="ADDITIONAL_DATA", fg="black", bd=20,
                                  width=40, bg="white", justify='left')
      lbl_ADDITIONAL_DATA.grid(row=12, column=0)
      ent_ADDITIONAL_DATA = Entry(Fram01, font=('arial', 12, 'bold'), textvariable=ADDITIONAL_DATA, fg="black", bd=20,
                                  width=40, bg="white", justify='left')
      ent_ADDITIONAL_DATA.grid(row=12, column=1)
      a0 = (new.get("ADDITIONAL DATA:"))
      ent_ADDITIONAL_DATA.insert(0, a0)
      print(ent_ADDITIONAL_DATA.get())

      lbl_ADDITIONAL_DATA = Label(Fram01, font=('arial', 12, 'bold'), text="ADDITIONAL_DATA", fg="black", bd=20,
                                  width=40, bg="white", justify='left')
      lbl_ADDITIONAL_DATA.grid(row=12, column=0)
      ent_ADDITIONAL_DATA = Entry(Fram01, font=('arial', 12, 'bold'), textvariable=Product_Name, fg="black", bd=20,
                                  width=40, bg="white", justify='left')
      ent_ADDITIONAL_DATA.grid(row=12, column=1)
      a0 = (new.get("ADDITIONAL DATA:"))
      ent_ADDITIONAL_DATA.insert(0, a0)
      print(ent_ADDITIONAL_DATA.get())




  #btn = Button(Fram01, text="doit", command=v)
  btn = Button(Fram02, font=('arial', 12, 'bold'), text="INSERT", fg="black", bd=20,width=40, bg="white", justify='left',command =v )
  btn.grid(row=0, column=1)


  def insert():
      db = mysql.connector.connect(user='root', passwd='12345678', host='localhost', database='naizak')
      cursor = db.cursor()
      #sql = 'INSERT INTO BATTERY (Product_Name, INTERNAL_MATERIALS, VOLTAGE,SIZE, COLD_CRANK_AMP,CONNECTION, STANDARD_SPECIFICATION, ADDITIONAL_DATA) values (%s, %s, %s, %s, %s, %s,%s)  '
      #val = (Product_Name.get(), INTERNAL_MATERIALS.get(), VOLTAGE.get(), SIZE.get(), CONNECTION.get(),STANDARD_SPECIFICATION.get(), ADDITIONAL_DATA.get())

      sql = 'INSERT INTO BATTERY7 (Product_Name,INTERNAL_MATERIALS,  VOLTAGE,SIZE, CONNECTION, STANDARD_SPECIFICATION, ADDITIONAL_DATA) values ( %s, %s, %s, %s, %s,%s,%s)  '
      val = (Product_Name.get(),INTERNAL_MATERIALS.get(),VOLTAGE.get(), SIZE.get(), CONNECTION.get(),STANDARD_SPECIFICATION.get(), ADDITIONAL_DATA.get())


      # cursor.execute('INSERT INTO BATTERY (Product_Name) values ( %s )',(Product_Name.get()))
      # sql = """INSERT INTO BATTERY (Product_Name, INTERNAL_MATERIAL_S) VALUES (%s, %s) """
      # val = (Product_Name.get(), INTERNAL_MATERIALS.get())
      cursor.execute(sql, val)

      db.commit()
      print(cursor.rowcount, 'record(s) inserted')
      cursor.close()
      db.close()


  btn1 = Button(Fram02, font=('arial', 20, 'bold'), fg="black", bd=7, text="insert_Data", command=insert)
  btn1.grid(row=0, column=2)

  Fram01.mainloop()

