import requests
import pdfplumber
import re
from tkinter import *

root = Tk()
INTERNALMATERIALS = StringVar()
with pdfplumber.open("c.pdf") as pdf:
  page = pdf.pages[0]
  text1 = page.extract_tables()
  text2 = page.extract_table()
  text3 = page.extract_text()
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
    ent0 = Entry(root)
    ent0.pack()
    a0 = (new.get("INTERNAL MATERIAL/S:"))
    ent0.insert(0,a0)
    print(ent0.get())

    ent1 = Entry(root)
    ent1.pack()
    a1 = (new.get("VOLTAGE:"))
    ent.insert(0,a1)
    print(ent1.get())

    ent2 = Entry(root)
    ent2.pack()
    a2 = (new.get("SIZE:"))
    ent2.insert(0,a2)
    print(ent2.get())

    ent3 = Entry(root)
    ent3.pack()
    a3 = (new.get("CONNECTION:"))
    ent3.insert(0,a3)
    print(ent3.get())

    ent4 = Entry(root)
    ent4.pack()
    a4 = (new.get("STANDARD/SPECIFICATION:"))
    ent4.insert(0,a4)
    print(ent4.get())




    

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
