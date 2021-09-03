from PIL import Image
import pytesseract
import cv2



pytesseract.tesseract_cmd = r"C:\Tesseract"
myfile =  Image.open("CCC.PNG")
text = pytesseract.image_to_string(myfile,lang ='eng')

# Displaying the extracted text
print(text)
