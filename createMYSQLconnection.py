import re
from tkinter import *
root = Tk()
'''
#z0 = BREAKER:CIRCUIT, GAS,2500 A,DRAWABLE

z00 = (z0.replace(":","_"))

z000 = (z00.index(","))
z10 = (z00[0:z000])

z = """
AMPERAGE:
CONNECTION:
KVRATING: 
INTERRUPTINGCAPACITY:
PHASE:
STANDARDSPECIFICATION:"""

'''
z0 = "TFMR,DIST,PD,1.5MVA,34.5K,4160/480,150KV TRANSFORMER,DISTRIBUTION:"

z = '''MOUNT:
KVA RATING:
PHASE:
APPLICATION PRIMARY VOLT:
ACTUAL PRIMARY VOLT:
SECONDARY VOLT:
FREQUENCY:
PRIMARY BIL RATING:
SECONDARY BIL RATINGS:
VECTOR GROUP:
PRIMARY BUSHINGS:'''
z000 = (z0.index(","))
z10 = (z0[0:z000])
#print(z10)



step_1 = z.replace("/","_")
step_2 = step_1.replace(" ","_")
step_3 = step_2.replace(":","=%s,")
#print(step_3)
# Craete update
step0 = " ' update "
step1 = z10
step2 = " set "
step3 = step_3
step4 = step0+step1+step2+step_3
step5 = len(step4)
step6 = step5 - 1
step7 = (step4[0:step6])
step8 = " where"
step9 = " ID=%s"
step10 = " ' "
step10_2 = ","
step10_3 = "("
step11 = step_2.replace(":",".get(),")
step12 = len(step11)
step13 = step12 - 1
step14 = (step11[0:step13])
step12 = ")"
step10_1 =step7+step8+step9 +step10 + step10_2 + step10_3+step14 + step12
print(step10_1)


'''cursor.execute("update nps_new set  NAME=%s, Eqamano=%s,Birthday=%s,BloodGroup=%s where ID=%s "
               , (NAME.get(), Eqamano.get(), BirthDay.get(), BloodGroup.get(), ID.get()))
'''

# create Lable


# create Variable
step3 = step_2.replace(":"," = StringVar()")
print(step3)
print("____________________________________________________")

# create table
step0 = "CREATE TABLE "
step1 = z10
step2 = "( "
step3 = step_2.replace(":"," varchar(20),")
step4 = step0+step1+step2+step3
step5 = len(step4)
step6 = step5 - 1
step7 = (step4[0:step6])
step8 = step7 + ")"
print(step8)
print("____________________________________________________")
# create Insert

step0 = "INSERT INTO TABLE "
step1 = z10
step2 = " ("
step3 = step_2.count(":")
step4 = "%s,"
step5 = step3 * step4
step4 = step0+step1+step2+step5
step5 = len(step4)
step6 = step5 - 1
step7 = (step4[0:step6])
#print(step5)
step8 = step7 + ")"
step9 = ","
step10 = "("
step11 = step_2.replace(":",".get(),")
step12 = len(step11)
step13 = step12 - 1
step14 = (step11[0:step13])
#print(step14)
step12 = ")"
step13 = step8+step9+step10+step14+step12
print(step13)

root.mainloop()

""" ' update TFMR set MOUNT=%s,
KVA_RATING=%s,
PHASE=%s,
APPLICATION_PRIMARY_VOLT=%s,
ACTUAL_PRIMARY_VOLT=%s,
SECONDARY_VOLT=%s,
FREQUENCY=%s,
PRIMARY_BIL_RATING=%s,
SECONDARY_BIL_RATINGS=%s,
VECTOR_GROUP=%s,
PRIMARY_BUSHINGS=%s where ID=%s ' ,(MOUNT.get(),
KVA_RATING.get(),
PHASE.get(),
APPLICATION_PRIMARY_VOLT.get(),
ACTUAL_PRIMARY_VOLT.get(),
SECONDARY_VOLT.get(),
FREQUENCY.get(),
PRIMARY_BIL_RATING.get(),
SECONDARY_BIL_RATINGS.get(),
VECTOR_GROUP.get(),
PRIMARY_BUSHINGS.get())
MOUNT = StringVar()
KVA_RATING = StringVar()
PHASE = StringVar()
APPLICATION_PRIMARY_VOLT = StringVar()
ACTUAL_PRIMARY_VOLT = StringVar()
SECONDARY_VOLT = StringVar()
FREQUENCY = StringVar()
PRIMARY_BIL_RATING = StringVar()
SECONDARY_BIL_RATINGS = StringVar()
VECTOR_GROUP = StringVar()
PRIMARY_BUSHINGS = StringVar()
____________________________________________________
CREATE TABLE TFMR( MOUNT varchar(20),
KVA_RATING varchar(20),
PHASE varchar(20),
APPLICATION_PRIMARY_VOLT varchar(20),
ACTUAL_PRIMARY_VOLT varchar(20),
SECONDARY_VOLT varchar(20),
FREQUENCY varchar(20),
PRIMARY_BIL_RATING varchar(20),
SECONDARY_BIL_RATINGS varchar(20),
VECTOR_GROUP varchar(20),
PRIMARY_BUSHINGS varchar(20))
____________________________________________________
INSERT INTO TABLE TFMR (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s),(MOUNT.get(),
KVA_RATING.get(),
PHASE.get(),
APPLICATION_PRIMARY_VOLT.get(),
ACTUAL_PRIMARY_VOLT.get(),
SECONDARY_VOLT.get(),
FREQUENCY.get(),
PRIMARY_BIL_RATING.get(),
SECONDARY_BIL_RATINGS.get(),
VECTOR_GROUP.get(),
PRIMARY_BUSHINGS.get())
"""
