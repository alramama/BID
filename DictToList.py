data ="""MOUNT:
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
(3) LOAD BREAK BUSHING INSERT FOR 4160 V, (4) ENCLOSED 4-HOLES SPADE TERMINATI ONS FOR 480 V;"""
clean1 = data.replace(";","")
clean2 = clean1.replace(":"," ")
clean3 = clean2.replace(","," ")
clean4 = clean3.strip()
#print(clean4)
#clean5 = clean4.pop(1)


#print(clean3)

#A = data.splitlines()
A = clean4.split("\n")
#print(A)
B = str(A).replace("n"," ")
#print(B)
C = str(A).replace("\\"," ")
#print(C)

#A = data.splitlines()
print(len(A))


def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct
         
# Driver code
#lst = ['AMPERAGE:', '2500 A;', 'CONNECTION:', 'DRAWABLE;', 'INTERRUPTING CAPACITY:', '31.5 KA;', 'KV RATING:', '33 KV;', 'PHASE:', '3 PHASE;', 'STANDARD/SPECIFICATION:', 'IEC 56;']
lst = A 
Z = (Convert(lst))
print(Z)
#print(Z["MOUNT"])
#print(Z["KVARATING"])
#print(Z["PHASE"])
#print(Z["APPLICATION"])






#print(Z["MOUNT "])
#clean1 = str(Z).replace(";","")
#clean2 = clean1.replace(":"," ")
#clean3 = clean2.replace(","," ")
#print(clean3)





