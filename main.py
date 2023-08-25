from PIL import Image
from pytesseract import pytesseract
import os

outPath = r"./out"
imagesPath = r"./images/"

pathToTesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = pathToTesseract


os.environ['TESSDATA_PREFIX'] = r"C:\Program Files\Tesseract-OCR\tessdata"
#my_var_value = os.environ['TESSDATA_PREFIX']
#print(my_var_value)


with os.scandir(imagesPath) as entries:
    for entry in entries:
        if entry.is_file():

            img = Image.open(entry.path)
            text = pytesseract.image_to_string(img, lang= 'rus+eng')

            with open(f"{outPath}/{entry.name.split('.')[0]}.txt", 'w', encoding = 'utf-8') as outFile:
                outFile.write(text)

 
