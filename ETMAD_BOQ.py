def extract_whole():
  pdf = pdfplumber.open("75.pdf")
  n = len(pdf.pages)
  for page in range(n):
    
    f = pdf.pages[page].extract_tables()
    #print(f[0][5])
    #res = list(filter(None, f))
    for i in range(len(list(f))):
      #print(i , len(f[i]))
      for j in range(len(f[i])):
        #print(page, "i:",i,"j:",j,f[i][j])
        a = (list(filter(None, f[i][j])))
        if len(a) == 8:
          #print(a)
          print(str(a).replace("\n",""))
extract_whole()

