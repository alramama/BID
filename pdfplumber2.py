import PyPDF2
import pdfplumber
import re


def extract_whole():
    pdf = pdfplumber.open("CV.pdf")
    n = len(pdf.pages)

    for page in range(n):
        data = pdf.pages[page].extract_text()
        data1 = re.split("\n",data)
        iqama = str(data1[4]).split()
        print(iqama[0])
        print(iqama[2])
        print(iqama[5])
        iqama1 = str(data1[7]).split()
        print(iqama1[0])
        print(iqama1[3])
        print(iqama1[6])
        iqama2 = str(data1[11]).split()
        print(iqama2[0])
        #print(iqama2[1])
        print(iqama2[2])
        iqama3 = str(data1[12]).split()
        print(iqama3[0])
        print(iqama3[3])
        print(iqama3[6])
        iqama4 = str(data1[14]).split()
        if (len(iqama4)) == 10:
          print(iqama4[4])
          print(iqama4[7])
        else:
          print(iqama4[5])
          print(iqama4[8])
        iqama3 = str(data1[5]).replace("ﻢﺳﻻﺍ","")
        print(iqama3)
        iqama5 = str(data1[6]).replace("ﻢﺟﺮﺘﻤﻟﺍ ﻢﺳﻻﺍ","")
        print(iqama5)
    
extract_whole()
