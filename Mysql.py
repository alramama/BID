
        import mysql.connector
  
  
        ID = StringVar()
        NAME = StringVar()
        JobTitle = StringVar()
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

        Name = mysql.connector.connect(host="localhost", user="root", password="12345678", database="tender")
        cursor = Name.cursor()
        cursor.execute("select NAME from Name")
        row = cursor.fetchall()

        Name.commit()
        Name.close()
        
        
                import mysql.connector
        conn = mysql.connector.connect(user='root', password="12345678", host='localhost', database='tender')
        print(conn)
        conn.close()
        # =====================================================Mysql.Create table===============================================
        import mysql.connector
        conn = mysql.connector.connect(user='root', password="12345678", host='localhost', database='tender')
        mycursor = conn.cursor()
        mycursor.execute("CREATE TABLE IF NOT EXISTS Name("
                         "ID VARCHAR(255),"
                         "NAME VARCHAR(255),"
                         "Qualification VARCHAR(255) ,"
                         "JobTitle VARCHAR(255),"
                         "Salary DOUBLE,"
                         "Housing_allowance DOUBLE,"
                         "Trans_allowance DOUBLE,"
                         "Health_Insurance DOUBLE,"
                         " Annual_Tickets DOUBLE ,"
                         "Phone_Charge DOUBLE,"
                         "Work_license DOUBLE,"
                         "Residence_permit DOUBLE,"
                         "SCE DOUBLE,"
                         "GOSI DOUBLE)")
        conn.close()

        # ====================================================================INSERT
        def insert():
            sqlcon = mysql.connector.connect(host="localhost", user="root", password="12345678", database="tender")
            cursor = sqlcon.cursor()
            isrting = "INSERT INTO Name (ID, NAME, JobTitle, Qualification, Salary, Housing_allowance, Health_Insurance, Trans_allowance, Annual_Tickets,Phone_Charge, Work_license, SCE, GOSI) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            values = self.ENT_ID.get(),self.ENT_Name.get(),self.ENT_Job_Title.get(),self.ENT_Qualification.get(),self.ENT_Salary.get(),self.ENT_Housing_allowance.get(),self.ENT_Health_Insurance.get(),self.ENT_Trans_allowance.get(),self.ENT_Annual_Tickets.get(),self.ENT_Phone_Charge.get(),self.ENT_Work_license.get(),self.ENT_SCE.get(),self.ENT_GOSI.get()
            cursor.execute(isrting,values)
            sqlcon.commit()
            sqlcon.close()
        # =====================================================Update
        def Update():
            sqlcon = mysql.connector.connect(host="localhost", user="root", password="12345678", database="tender")
            cursor = sqlcon.cursor()
            cursor.execute("update BID set ID=%s,"
                           "NAME=%s,"
                           "JobTitle=%s,"
                           "Salary=%s,"
                           "Housing_allowance=%s,"
                           "Trans_allowance=%s,"
                           "Health_Insurance=%s,"
                           "Phone_Charge=%s,"
                           "Work_license=%s,"
                           "Residence_permit=%s,"
                           "SCE=%s,"
                           "GOSI=%s)",
                           (ID.get(),
                            NAME.get(),
                            JobTitle.get(),
                            Salary.get(),
                            Housing_allowance.get(),
                            Trans_allowance.get(),
                            Health_Insurance.get(),
                            Phone_Charge.get(),
                            Work_license.get(),
                            Residence_permit.get(),
                            SCE.get(),
                            GOSI.get()))
            sqlcon.commit()

        # ======================================================search
        def search():
            sqlcon = mysql.connector.connect(host="localhost", user="root", password="12345678", database="tender")
            cursor = sqlcon.cursor()
            cursor.execute("select * from Name where NAME='%s'" % NAME.get())
            row = cursor.fetchall()

            ID.set(row[0])
            NAME.set(row[1])
            JobTitle.set(row[2])
            Salary.set(row[3])
            Housing_allowance.set(row[4])
            Trans_allowance.set(row[5])
            Health_Insurance.set(row[6])
            Phone_Charge.set(row[7])
            Work_license.set(row[8])
            Residence_permit.set(row[9])
            SCE.set(row[10])
            GOSI.set(row[11])
            sqlcon.commit()
            sqlcon.close()

        # =====================================================Combobox
        NAME = mysql.connector.connect(host="localhost", user="root", password="12345678", database="tender")
        cursor = NAME.cursor()
        cursor.execute("select NAME from Name")
        row = cursor.fetchall()
        NAME.commit()
        NAME.close()

