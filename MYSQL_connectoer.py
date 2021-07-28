from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import mysql.connector

#cursor.execute("CREATE TABLE npss (StudentID VARCHAR(255), Fname VARCHAR(255),Mobail VARCHAR(255), Address VARCHAR(255),Gender VARCHAR(255) )")


# import pymysql

class ConnectorDB:

    def __init__(self, root):
        self.root = root
        titelspace = " "
        self.root.geometry("810x800+500+0")
        self.root.title("MYSQL_connectoer")


        #===============================================================

        ID = StringVar()
        NAME = StringVar()
        Eqamano = StringVar()
        BirthDay = StringVar()
        BloodGroup = StringVar()
        #===============================================================

        MainFrame = Frame(self.root, bd=10, width=770, height=700, relief=RIDGE, bg="cadet blue")
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=7, width=770, height=100, relief=RIDGE)
        TitleFrame.grid(row = 0 , column = 0)
        TopFrame3 = Frame(MainFrame, bd=5, width=770, height=500, relief=RIDGE)
        TopFrame3.grid(row=1, column=0)

        LeftFrame = Frame(TopFrame3, bd=5, width=770, height=400, relief=RIDGE, padx=2, pady=4, bg="cadet blue")
        LeftFrame.pack(side=LEFT)
        LeftFrame1 = Frame(LeftFrame, bd=5, width=600, height=180, relief=RIDGE, padx=2, pady=4)
        LeftFrame1.pack(side= TOP, padx=0, pady=0)

        RightFrame1 = Frame(TopFrame3, bd=5, width=200, height=400, relief=RIDGE, padx=2, bg="cadet blue")
        RightFrame1.pack(side=RIGHT)
        RightFrame1a = Frame(RightFrame1, bd=5, width=200, height=300, relief=RIDGE, padx=2, pady=2)
        RightFrame1a.pack(side=TOP)

        #===========================================================
        self.lbltitle = Label(TitleFrame, font=('arial',40,'bold'), text="Mysql Connection", bd=7)
        self.lbltitle.grid(row=0, column=0, padx=132)

        self.lblID = Label(LeftFrame1, font=('arial', 12, 'bold'), text="StudentID", bd=7)
        self.lblID.grid(row=1, column=0, sticky=W,padx = 5)
        self.EntID = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left', textvariable = ID )
        self.EntID.grid(row=1, column=1, sticky=W, padx=5)

        self.lblNAME = Label(LeftFrame1, font=('arial', 12, 'bold'), text="NAME", bd=7)
        self.lblNAME.grid(row=2, column=0, sticky=W, padx=5)
        self.EntNAME = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left', textvariable = NAME)
        self.EntNAME.grid(row=2, column=1, sticky=W, padx=5)

        self.lblEqamano = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Eqamano", bd=7)
        self.lblEqamano.grid(row=3, column=0, sticky=W, padx=5)
        self.EntEqamano = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left', textvariable = Eqamano)
        self.EntEqamano.grid(row=3, column=1, sticky=W, padx=5)


        '''self.lblEqamano = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Eqamano", bd=7, textvariable = Eqamano)
        self.lblEqamano.grid(row=3, column=0, sticky=W, padx=5)
        self.EEqamano = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left')
        self.EEqamano.grid(row=3, column=1, sticky=W, padx=5)
'''
        self.lblBirthDay = Label(LeftFrame1, font=('arial', 12, 'bold'), text="BirthDay", bd=7)
        self.lblBirthDay.grid(row=4, column=0, sticky=W, padx=5)
        self.EBirthDay = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left', textvariable = BirthDay)
        self.EBirthDay.grid(row=4, column=1, sticky=W, padx=5)

        self.lblBloodGroup = Label(LeftFrame1, font=('arial', 12, 'bold'), text="BloodGroup", bd=7)
        self.lblBloodGroup.grid(row=5, column=0, sticky=W, padx=5)
        self.BloodGroup = ttk.Combobox(LeftFrame1, font=('arial', 12, 'bold'), width=44 , state = "readonly",textvariable = BloodGroup)
        self.BloodGroup["value"] = ('', 'A+','B+', 'B-','O+', 'O-','AB')
        self.BloodGroup.grid(row=5, column=1, sticky=W, padx=5)
        #==


        def Iexit():
            Iexit = tkinter.messagebox.askyesno("MYSQL connectoer" , "Cinfirm if you want exit")
            if Iexit > 0:
                root.destroy()
                return

        def Rest():
            self.EntID.delete(0, END)
            self.EntNAME.delete(0, END)
            self.EntEqamano.delete(0, END)
            self.EBirthDay.delete(0, END)
            BloodGroup.set(" ")

        '''
        def ADDnew():

            sql_command = "INSERT INTO npss  (StudentID,Fname,Address,Gender) VALUES (%s, %s, %s, %s)"
            values = (self.EntStudentID.get(), self.EntFname.get(), self.EAddress.get(),self.Gender.get())
            cursor.execute(sql_command, values)
            db.commit()
        '''

        def Desplay():
            sqlcon = mysql.connector.connect(host="localhost", user="root", password="12345678", database="naizak")
            cursor= sqlcon.cursor()
            cursor.execute("select * from nps_new")
            result = cursor.fetchall()
            if len(result) !=0:
                self.student_records.delete(*self.student_records.get_children())
                for row in result:
                    self.student_records.insert('',END,values = row)
                    sqlcon.commit()
            sqlcon.close()

        def TraineeInfo(ev):
            viewInfo = self.student_records.focus()
            learnDate = self.student_records.item(viewInfo)
            row = learnDate['values']
            ID.set(row[0])
            NAME.set(row[1])
            Eqamano.set(row[2])
            BirthDay.set(row[3])
            BloodGroup.set(row[4])

        #== == == == == == == == == == == == == == == == == == == =Table
        #treeviwe == == == == == == == == == == == == == == == == == == == == == == == == == == == =

        scroll_Y = Scrollbar(LeftFrame, orient=VERTICAL)
        scroll_Y.pack(side=RIGHT, fill=Y)


        self.student_records = ttk.Treeview(LeftFrame, height=12,columns=("ID","NAME","Eqamano","BirthDay","BloodGroup"),xscrollcommand=scroll_Y.set)
        self.student_records["show"] = 'headings'
        self.student_records.column("ID", width=120, minwidth=25)
        self.student_records.column("NAME", width=120, minwidth=25)
        self.student_records.column("Eqamano", width=120, minwidth=25)
        self.student_records.column("BirthDay", width=120, minwidth=25)
        self.student_records.column("BloodGroup", width=120, minwidth=25)

        self.student_records.heading("ID", text="ID")
        self.student_records.heading("NAME", text="NAME")
        self.student_records.heading("Eqamano", text="Eqamano")
        self.student_records.heading("BirthDay", text="BirthDay")
        self.student_records.heading("BloodGroup", text="BloodGroup")
        self.student_records.pack(fill =BOTH, expand = 1)
        self.student_records.bind("<ButtonRelease-1>",TraineeInfo)
        Desplay()
        def search():
            return

        def insert():
            sqlcon = mysql.connector.connect(host="localhost", user="root", password="12345678", database="naizak")
            cursor = sqlcon.cursor()
            cursor.execute("INSERT INTO nps_new VALUES (%s, %s, %s,%s,%s)" ,(ID.get(),NAME.get(),Eqamano.get(),BirthDay.get(),BloodGroup.get(),))
            sqlcon.commit()
            sqlcon.close()
        def Update():
            sqlcon = mysql.connector.connect(host="localhost", user="root", password="12345678", database="naizak")
            cursor = sqlcon.cursor()
            cursor.execute("update nps_new set  NAME=%s, Eqamano=%s,Birthday=%s,BloodGroup=%s where ID=%s "
                           ,(NAME.get(),Eqamano.get(),BirthDay.get(),BloodGroup.get(),ID.get()))
            sqlcon.commit()
            Desplay()
            sqlcon.close()
        def delete():
            sqlcon = mysql.connector.connect(host="localhost", user="root", password="12345678", database="naizak")
            cursor = sqlcon.cursor()
            cursor.execute("delete from nps_new where ID='%s'"% ID.get())
            sqlcon.commit()
            Desplay()
            sqlcon.close()
        def search():
            sqlcon = mysql.connector.connect(host="localhost", user="root", password="12345678", database="naizak")
            cursor = sqlcon.cursor()
            cursor.execute("select * from nps_new where ID='%s'" %ID.get())

            row = cursor.fetchall()

            ID.set(row[0])
            NAME.set(row[1])
            Eqamano.set(row[2])
            BirthDay.set(row[3])
            BloodGroup.set(row[4])

            sqlcon.commit()
            sqlcon.close()




        def checkdatabaseconection():

            sql = mysql.connector.connect(host="localhost", user="root", password="12345678")
            print(tkinter.messagebox.askquestion(sql, "connected"))

        #===============================================================

        self.btnaddnwe = Button(RightFrame1a, font = ('arial',16,'bold'), text = "ADDNEW", bd = 2, padx = 1 , pady = 20, width = 8, height = 1, command = insert)
        self.btnaddnwe.grid(row  = 0, column =0, padx =2 )
        self.btndisplay = Button(RightFrame1a, font = ('arial',16,'bold'), text = "DISPLY", bd = 2, padx = 1 , pady = 20, width = 8, height = 1, command = Desplay)
        self.btndisplay.grid(row  = 1, column =0, padx =2 )
        self.btndelete = Button(RightFrame1a, font = ('arial',16,'bold'), text = "DELETE", bd = 2, padx = 1 , pady = 20, width = 8, height = 1, command = delete)
        self.btndelete.grid(row  = 2, column =0, padx =2 )
        self.btnupdate = Button(RightFrame1a, font = ('arial',16,'bold'), text = "UPDATE", bd = 2, padx = 1 , pady = 20, width = 8, height = 1,command = Update)
        self.btnupdate.grid(row  = 3, column =0, padx =2 )
        self.btnRest = Button(RightFrame1a, font = ('arial',16,'bold'), text = "REST", bd = 2, padx = 1 , pady = 20, width = 8, height = 1, command = Rest)
        self.btnRest.grid(row  = 4, column =0, padx =1 )
        self.btnExit = Button(RightFrame1a, font = ('arial',16,'bold'), text = "EXIT", bd = 2, padx = 1 , pady = 20, width = 8, height = 1, command = Iexit)
        self.btnExit.grid(row  = 5, column =0, padx =1 )
        self.btnSearch = Button(RightFrame1a, font = ('arial',16,'bold'), text = "SEARCH", bd = 2, padx = 1 , pady = 20, width = 8, height = 1, command = search)
        self.btnSearch.grid(row  = 6, column =0, padx =1 )
        #self.btnconnection = Button(RightFrame1a, font = ('arial',16,'bold'), text = "CONNECTION", bd = 5, padx = 1 , pady = 24, width = 8, height = 1, command = checkdatabaseconection)
        #self.btnconnection.grid(row  = 7, column =0, padx =1 )

        #=======================================================================================================================================










if __name__ == '__main__':

    root = Tk()
    application = ConnectorDB(root)
    root.mainloop()
