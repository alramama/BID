import requests
import pdfplumber
import re
from tkinter import *

root = Tk()
INTERNALMATERIALS = StringVar()
VOLTAGE = StringVar()
SIZE = StringVar()
CONNECTION = StringVar()
STANDARD_SPECIFICATION = StringVar()
ADDITIONAL_DATA = StringVar()

  with pdfplumber.open("c.pdf") as pdf:
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
  b1 =b[5]
  #print(str(b1).replace("\n","','")) 

  a1 = (text3[531:822])

  mytext = Text(root, height = 10)
  mytext.pack()
  mytext.insert("1.0",b1)
  ent = Entry(root)
  ent.pack()



  def deleted():
    mytext.delete("1.0","1.100")
  def v():
    a0 = mytext.get("1.0", END)
    a1 = re.split("\n",a0)
    a2 = mytext.get("1.0",END)
    a3 = re.split("\n",a2)
    #print(a3)
    #print(len(a3))
    def Convert_dict(a):
      init = iter(list1)  
      res_dct = dict(zip(init, init))  
      return res_dct
  
  
# Driver code  
    list1 = a3  
    new = Convert_dict(list1)
    
    lbl_RFQ_NO= Entry(Frame01, font = ('arial',12, 'bold'), text= "RFQ_NO", fg = "black", bd = 20,  width = 16, bg = "white" , justify = 'left'  )
    lbl__RFQ_NO.grid(row = 1 , column = 1)
    ent_RFQ_NO= Entry(Frame01, font = ('arial',12, 'bold'), textvariable= RFQ_NO, fg = "black", bd = 20,  width = 16, bg = "white", justify = 'left'  )
    ent__RFQ_NO.grid(row = 1 , column = 1)
    a0 = (new.get("INTERNAL MATERIAL/S:"))
    ent__RFQ_NO.insert(0,a0)
    print(ent__RFQ_NO.get())

    lbl_BID_OPEN= Entry(Frame01, font = ('arial',12, 'bold'), text= "BID_OPEN", fg = "black", bd = 20,  width = 16, bg = "white" , justify = 'left'  )
    lbl__BID_OPEN.grid(row = 1 , column = 1)
    ent_BID_OPEN= Entry(Frame01, font = ('arial',12, 'bold'), textvariable= BID_OPEN, fg = "black", bd = 20,  width = 16, bg = "white", justify = 'left'  )
    ent__BID_OPEN.grid(row = 1 , column = 1)
    a0 = (new.get("INTERNAL MATERIAL/S:"))
    ent__BID_OPEN.insert(0,a0)
    print(ent__BID_OPEN.get())


    lbl_BAYER_NAME= Entry(Frame01, font = ('arial',12, 'bold'), text= "BAYER_NAME", fg = "black", bd = 20,  width = 16, bg = "white" , justify = 'left'  )
    lbl__BAYER_NAME.grid(row = 1 , column = 1)
    ent_BAYER_NAME= Entry(Frame01, font = ('arial',12, 'bold'), textvariable= BAYER_NAME, fg = "black", bd = 20,  width = 16, bg = "white", justify = 'left'  )
    ent__BAYER_NAME.grid(row = 1 , column = 1)
    a0 = (new.get("INTERNAL MATERIAL/S:"))
    ent__BAYER_NAME.insert(0,a0)
    print(ent__BAYER_NAME.get())

    lbl_BAYER_TELPHONE= Entry(Frame01, font = ('arial',12, 'bold'), text= "BAYER_TELPHONE", fg = "black", bd = 20,  width = 16, bg = "white" , justify = 'left'  )
    lbl__BAYER_TELPHONE.grid(row = 1 , column = 1)
    ent_BAYER_TELPHONE= Entry(Frame01, font = ('arial',12, 'bold'), textvariable= BAYER_TELPHONE, fg = "black", bd = 20,  width = 16, bg = "white", justify = 'left'  )
    ent__BAYER_TELPHONE.grid(row = 1 , column = 1)
    a0 = (new.get("INTERNAL MATERIAL/S:"))
    ent__BAYER_TELPHONE.insert(0,a0)
    print(ent__BAYER_TELPHONE.get())

    lbl_REQ_UNIT= Entry(Frame01, font = ('arial',12, 'bold'), text= "REQ_UNIT", fg = "black", bd = 20,  width = 16, bg = "white" , justify = 'left'  )
    lbl__REQ_UNIT.grid(row = 1 , column = 1)
    ent_REQ_UNIT= Entry(Frame01, font = ('arial',12, 'bold'), textvariable= REQ_UNIT, fg = "black", bd = 20,  width = 16, bg = "white", justify = 'left'  )
    ent__REQ_UNIT.grid(row = 1 , column = 1)
    a0 = (new.get("INTERNAL MATERIAL/S:"))
    ent__REQ_UNIT.insert(0,a0)
    print(ent__REQ_UNIT.get())

    lbl_REQ_QTY= Entry(Frame01, font = ('arial',12, 'bold'), text= "REQ_QTY", fg = "black", bd = 20,  width = 16, bg = "white" , justify = 'left'  )
    lbl__REQ_QTY.grid(row = 1 , column = 1)
    ent_REQ_QTY= Entry(Frame01, font = ('arial',12, 'bold'), textvariable= REQ_QTY, fg = "black", bd = 20,  width = 16, bg = "white", justify = 'left'  )
    ent__REQ_QTY.grid(row = 1 , column = 1)
    a0 = (new.get("INTERNAL MATERIAL/S:"))
    ent__REQ_QTY.insert(0,a0)
    print(ent__REQ_QTY.get())

    #---------------------------------------------INTERNAL_MATERIALS
#01
    lbl_INTERNAL_MATERIALS= Entry(Frame01, font = ('arial',12, 'bold'), text= "INTERNAL_MATERIALS", fg = "black", bd = 20,  width = 16, bg = "white" , justify = 'left'  )
    lbl__INTERNAL_MATERIALS.grid(row = 1 , column = 1)
    ent_INTERNAL_MATERIALS= Entry(Frame01, font = ('arial',12, 'bold'), textvariable= INTERNAL_MATERIALS, fg = "black", bd = 20,  width = 16, bg = "white", justify = 'left'  )
    ent__INTERNAL_MATERIALS.grid(row = 1 , column = 1)
    a0 = (new.get("INTERNAL MATERIAL/S:"))
    ent__INTERNAL_MATERIALS.insert(0,a0)
    print(ent__INTERNAL_MATERIALS.get())

#02
    lbl_VOLTAGE= Entry(Frame01, font = ('arial',12, 'bold'), text= "VOLTAGE", fg = "black", bd = 20,  width = 16, bg = "white" , justify = 'left'  )
    lbl__VOLTAGE.grid(row = 1 , column = 1)
    ent_VOLTAGE= Entry(Frame01, font = ('arial',12, 'bold'), textvariable= VOLTAGE, fg = "black", bd = 20,  width = 16, bg = "white", justify = 'left'  )
    ent__VOLTAGE.grid(row = 1 , column = 1)
    a0 = (new.get("VOLTAGE:"))
    ent__VOLTAGE.insert(0,a0)
    print(ent__VOLTAGE.get())
#03
    lbl_SIZE= Entry(Frame01, font = ('arial',12, 'bold'), text= "SIZE", fg = "black", bd = 20,  width = 16, bg = "white" , justify = 'left'  )
    lbl__SIZE.grid(row = 1 , column = 1)
    ent_SIZE= Entry(Frame01, font = ('arial',12, 'bold'), textvariable= SIZE, fg = "black", bd = 20,  width = 16, bg = "white", justify = 'left'  )
    ent__SIZE.grid(row = 1 , column = 1)
    a0 = (new.get("SIZE:"))
    ent__SIZE.insert(0,a0)
    print(ent__SIZE.get())
#04
    lbl_CONNECTION= Entry(Frame01, font = ('arial',12, 'bold'), text= "CONNECTION", fg = "black", bd = 20,  width = 16, bg = "white" , justify = 'left'  )
    lbl__CONNECTION.grid(row = 1 , column = 1)
    ent_CONNECTION= Entry(Frame01, font = ('arial',12, 'bold'), textvariable= CONNECTION, fg = "black", bd = 20,  width = 16, bg = "white", justify = 'left'  )
    ent__CONNECTION.grid(row = 1 , column = 1)
    a0 = (new.get("CONNECTION:"))
    ent__CONNECTION.insert(0,a0)
    print(ent__CONNECTION.get())
#05
    lbl_STANDARD_SPECIFICATION= Entry(Frame01, font = ('arial',12, 'bold'), text= "STANDARD_SPECIFICATION", fg = "black", bd = 20,  width = 16, bg = "white" , justify = 'left'  )
    lbl__STANDARD_SPECIFICATION.grid(row = 1 , column = 1)
    ent_STANDARD_SPECIFICATION= Entry(Frame01, font = ('arial',12, 'bold'), textvariable= STANDARD_SPECIFICATION, fg = "black", bd = 20,  width = 16, bg = "white", justify = 'left'  )
    ent__STANDARD_SPECIFICATION.grid(row = 1 , column = 1)
    a0 = (new.get("STANDARD/SPECIFICATION:"))
    ent__STANDARD_SPECIFICATION.insert(0,a0)
    print(ent__STANDARD_SPECIFICATION.get())
#06
    lbl_ADDITIONAL_DATA= Entry(Frame01, font = ('arial',12, 'bold'), text= "ADDITIONAL_DATA", fg = "black", bd = 20,  width = 16, bg = "white" , justify = 'left'  )
    lbl__ADDITIONAL_DATA.grid(row = 1 , column = 1)
    ent_ADDITIONAL_DATA= Entry(Frame01, font = ('arial',12, 'bold'), textvariable= ADDITIONAL_DATA, fg = "black", bd = 20,  width = 16, bg = "white", justify = 'left'  )
    ent__ADDITIONAL_DATA.grid(row = 1 , column = 1)
    a0 = (new.get("ADDITIONAL DATA:"))
    ent__ADDITIONAL_DATA.insert(0,a0)
    print(ent__ADDITIONAL_DATA.get())
    
    


    """i = 0
    while i < (len(a1)):
      x0 = Label(root,text =a1[i]).pack()
      x1 = Entry(root,textvariable =a1[i] )
      x1.pack()
      z = new.get(a1[i])
      x1.insert(0,z)
      print(type(x1))
      i +=2
    """
    
    


  btn = Button(root, text="doit", command =v)
  btn.pack()
  btn = Button(root, text="delete", command =deleted)
  btn.pack()

  









  root.mainloop()
