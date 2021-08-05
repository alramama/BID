  #هل انت متزوج؟ نعم
  #هل زوجتك تعيش معك؟ نعم
  #هل لديك اطفال؟ نعم
  #كم عدد الاولاد؟ نعم
  #كم عدد البنات؟ نعم

  #هل انت متزوج؟ لا
  

def Nationalty(e):
    if Are_you_Saudi.get() == "Yes":
        NAME_MainFrame =             Frame(Name, bd=16, width=1350, height=600, relief=RIDGE)
        NAME_MainFrame.grid(row=0, column=0)
        #===================================================================FRAM_Name_Emp_Info.=================================================
        FRAM_Name_Emp_Info =         Frame(NAME_MainFrame, bd=16, width=70, height=60, relief=RIDGE)
        FRAM_Name_Emp_Info.grid(row=1, column=0)
        FRAM_Name_Emp_Info1 =         Frame(NAME_MainFrame, bd=16, width=70, height=60, relief=RIDGE)
        FRAM_Name_Emp_Info1.grid(row=1, column=0)
  
  else:

    lbl_GOSI=Label(root,text="name",fg="black", bd=5).grid(row=1,column=8)

BTN = Button(root, text = "Check", command = check)
BTN.grid(row=2, column=1)

ID = StringVar()
NAME = StringVar()
JobTitle = StringVar()
Nationality = StringVar()
Status_of_Social = StringVar()
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

lbl_ID =                     Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'),text="ID",                fg="black", bd=5).grid(row=1, column=0)
lbl_ID =                     Enter(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'),text="ID",                fg="black", bd=5).grid(row=1, column=0)

if (Are You Saudi == yes):

  NAME_MainFrame =             Frame(Name, bd=16, width=1350, height=600, relief=RIDGE)
  NAME_MainFrame.grid(row=0, column=0)
  #===================================================================FRAM_Name_Emp_Info.=================================================
  FRAM_Name_Emp_Info =         Frame(NAME_MainFrame, bd=16, width=70, height=60, relief=RIDGE)
  FRAM_Name_Emp_Info.grid(row=1, column=0)
  FRAM_Name_Emp_Info1 =         Frame(NAME_MainFrame, bd=16, width=70, height=60, relief=RIDGE)
  FRAM_Name_Emp_Info1.grid(row=1, column=0)
  lbl_ID =                     Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'),text="ID",                fg="black", bd=5).grid(row=1, column=0)
  lbl_Name =                   Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'),text="NAME",              fg="black", bd=5).grid(row=2, column=0)
  lbl_Job_Title =              Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'),text="Job Title",         fg="black", bd=5).grid(row=3, column=0)
  lbl_Qualification =          Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'),text="Qualification",     fg="black", bd=5).grid(row=4, column=0)
  lbl_ID =                     Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'),text="ID",                fg="black", bd=5).grid(row=1, column=1)
  lbl_Name =                   Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'),text="NAME",              fg="black", bd=5).grid(row=2, column=1)
  lbl_Job_Title =              Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'),text="Job Title",         fg="black", bd=5).grid(row=3, column=1)
  lbl_Qualification =          Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'),text="Qualification",     fg="black", bd=5).grid(row=4, column=1)
  lbl_Salary =                Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Salary",            fg="black", bd=5).grid(row=1, column=2)
  lbl_Housing_allowance =     Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Housing allowance", fg="black", bd=5).grid(row=2, column=2)
  lbl_Trans_allowance =       Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Trans allowance",   fg="black", bd=5).grid(row=3, column=2)
  lbl_Salary =                Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Salary",            fg="black", bd=5).grid(row=1, column=3)
  lbl_Housing_allowance =     Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Housing allowance", fg="black", bd=5).grid(row=2, column=3)
  lbl_Trans_allowance =       Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Trans allowance",   fg="black", bd=5).grid(row=3, column=3)
  lbl_Health_Insurance =      Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Health Insurance",   fg="black", bd=5).grid(row=1,column=4)
  lbl_Phone_Charge=           Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Phone Charge",       fg="black", bd=5).grid(row=3,column=4)
  lbl_Health_Insurance =      Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Health Insurance",   fg="black", bd=5).grid(row=1,column=5)
  lbl_Phone_Charge=           Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Phone Charge",       fg="black", bd=5).grid(row=3,column=5)
  lbl_SCE=                    Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="SCE",                fg="black", bd=5).grid(row=3,column=6)
  lbl_SCE=                    Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="SCE",                fg="black", bd=5).grid(row=3,column=7)
  lbl_GOSI=                   Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="GOSI",               fg="black", bd=5).grid(row=1,column=8)
  lbl_GOSI=                   Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="GOSI",               fg="black", bd=5).grid(row=1,column=9)

else:
  NAME_MainFrame =             Frame(Name, bd=16, width=1350, height=600, relief=RIDGE)
  NAME_MainFrame.grid(row=0, column=0)
    #===================================================================FRAM_Name_Emp_Info.=================================================
  FRAM_Name_Emp_Info =         Frame(NAME_MainFrame, bd=16, width=70, height=60, relief=RIDGE)
  FRAM_Name_Emp_Info.grid(row=1, column=0)
  FRAM_Name_Emp_Info1 =         Frame(NAME_MainFrame, bd=16, width=70, height=60, relief=RIDGE)
  FRAM_Name_Emp_Info1.grid(row=1, column=0)
    
  lbl_ID =                     Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'),text="ID",                fg="black", bd=5).grid(row=1, column=0)
  lbl_Name =                   Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'),text="NAME",              fg="black", bd=5).grid(row=2, column=0)
  lbl_Job_Title =              Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'),text="Job Title",         fg="black", bd=5).grid(row=3, column=0)
  lbl_Qualification =          Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'),text="Qualification",     fg="black", bd=5).grid(row=4, column=0)
  lbl_ID =                     Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'),text="ID",                fg="black", bd=5).grid(row=1, column=1)
  lbl_Name =                   Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'),text="NAME",              fg="black", bd=5).grid(row=2, column=1)
  lbl_Job_Title =              Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'),text="Job Title",         fg="black", bd=5).grid(row=3, column=1)
  lbl_Qualification =          Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'),text="Qualification",     fg="black", bd=5).grid(row=4, column=1)
  lbl_Salary =                Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Salary",            fg="black", bd=5).grid(row=1, column=2)
  lbl_Housing_allowance =     Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Housing allowance", fg="black", bd=5).grid(row=2, column=2)
  lbl_Trans_allowance =       Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Trans allowance",   fg="black", bd=5).grid(row=3, column=2)
  lbl_Salary =                Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Salary",            fg="black", bd=5).grid(row=1, column=3)
  lbl_Housing_allowance =     Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Housing allowance", fg="black", bd=5).grid(row=2, column=3)
  lbl_Trans_allowance =       Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Trans allowance",   fg="black", bd=5).grid(row=3, column=3)
  lbl_Health_Insurance =      Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Health Insurance",   fg="black", bd=5).grid(row=1,column=4)
  lbl_Annual_Tickets =        Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Annual Tickets",     fg="black", bd=5).grid(row=2,column=4)
  lbl_Phone_Charge=           Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Phone Charge",       fg="black", bd=5).grid(row=3,column=4)
  lbl_Health_Insurance =      Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Health Insurance",   fg="black", bd=5).grid(row=1,column=5)
  lbl_Annual_Tickets =        Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Annual Tickets",     fg="black", bd=5).grid(row=2,column=5)
  lbl_Phone_Charge=           Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Phone Charge",       fg="black", bd=5).grid(row=3,column=5)
  lbl_Work_license=           Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Work license",       fg="black", bd=5).grid(row=1,column=6)
  lbl_Residence_permit=       Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Residence permit",   fg="black", bd=5).grid(row=2,column=6)
  lbl_SCE=                    Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="SCE",                fg="black", bd=5).grid(row=3,column=6)
  lbl_Work_license=           Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Work license",       fg="black", bd=5).grid(row=1,column=7)
  lbl_Residence_permit=       Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="Residence permit",   fg="black", bd=5).grid(row=2,column=7)
  lbl_SCE=                    Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="SCE",                fg="black", bd=5).grid(row=3,column=7)
  lbl_GOSI=                   Label(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="GOSI",               fg="black", bd=5).grid(row=1,column=8)
  lbl_GOSI=                   Entry(FRAM_Name_Emp_Info1, font=('arial', 10, 'bold'), text="GOSI",               fg="black", bd=5).grid(row=1,column=9)
  
  
Are_you_Saudi = ttk.Combobox(Name)
Are_you_Saudi['values'] = "Yes", "NO"
Are_you_Saudi.current()
Are_you_Saudi.bind('<<ComboboxSelected>>', Nationalty)
Are_you_Saudi.grid(row=0, column=1)

