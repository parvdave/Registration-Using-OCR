import pytesseract
from PIL import Image
from datetime import date
import re
import sqlite3
from datetime import date

def ImageOpener(self):
    im1 = Image.open(self)
    width, height = im1.size
    #print((width,height))
    im = im1.crop((width/4,height/2,width,height))
    im.show()
    return ImageToText(im)
def ImageToText(self):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
    text = pytesseract.image_to_string(self)
    l = text.split('\n')
    l1=[]
    for i in l:
        if len(i) == 0 or i.count(" ")==len(i):
            pass
        else:
            l1.append(i)
    return detailsReturn(l1)
def detailsReturn(self):
    name = str(self[0])
    name = re.findall("[A-Za-z]{1,}",name)
    nameUser = ""
    nameUser=name[0]+" "+name[len(name)-1]
    nameUser=nameUser.strip(" ")
    name = nameUser.title()

    #print(name)
    sapid = str(re.findall("\d\d\d\d\d\d\d\d\d\d\d",self[1])[0])
    #print(sapid)

    course = self[1].split()[0]
    #print(course)

    self[1]=self[1].split()
    stream = self[1][1][1:-1]
    #print(stream)

    contactNo = str(re.findall("\d\d\d\d\d\d\d\d\d\d",self[len(self)-1])[0])
    #print(contactNo)
    return [sapid,name,course,stream,contactNo]