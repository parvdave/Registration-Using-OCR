from tkinter import *
import DataExtraction
import sqlite3

root = Tk()
nameEntry = Entry(root)
ngoType=StringVar()
ngoSelected=StringVar()

ngoList = ["Pet Care Centre","Old Age Home","Teaching"]
ngoType.set("Make your choice")

def createGUI():
    initiateGUI()
    nameLabel = Label(root,text="Name : ")
    nameLabel.grid(row=0,column=0)
    nameEntry.grid(row=0,column=1)
    ngoTypeMenu = OptionMenu(root,ngoType,*ngoList)
    ngoLabel = Label(root,text="Choose type of NGO : ")
    ngoLabel.grid(row=1,column=0)
    ngoTypeMenu.grid(row=1,column=1)
    nextButton = Button(root, text="Next", command=createRadioButton)
    nextButton.grid(row=2, column=1)
    shutGUI()
def createRadioButton():
    connection = sqlite3.connect('SOS.db')
    cursor = connection.cursor()
    q = f"select oname,location from sos_org where type = '{ngoType.get()}'"
    f=cursor.execute(q)
    t1=f.fetchone()
    t2=f.fetchone()
    t3=f.fetchone()
    ngoOption1 = Radiobutton(root, text=f"{t1[0]}({t1[1]})", variable=ngoSelected, value=f"{t1[0]}")
    ngoOption2 = Radiobutton(root, text=f"{t2[0]}({t2[1]})", variable=ngoSelected, value=f"{t2[0]}")
    ngoOption3 = Radiobutton(root, text=f"{t3[0]}({t3[1]})", variable=ngoSelected, value=f"{t3[0]}")
    ngoOption1.grid(row=3, column=1)
    ngoOption2.grid(row=4, column=1)
    ngoOption3.grid(row=5, column=1)
    submitButton = Button(root, text="Submit", comm=enterData)
    submitButton.grid(row=6, column=1)
def enterData():
    nameOfUser = nameEntry.get()
    nameOfUser = nameOfUser.split()
    nameOfUser = "".join(nameOfUser)
    fileName = f"ID_{nameOfUser}.png"
    listOfData=DataExtraction.ImageOpener(fileName)
    connection = sqlite3.connect('SOS.db')
    cursor = connection.cursor()
    q = f"insert into Sos_student values('{listOfData[0]}','{listOfData[1]}','{listOfData[2]}','{listOfData[3]}','{listOfData[4]}')"
    cursor.execute(q)
    q = f"insert into sos_hourlog values('{listOfData[0]}','{ngoSelected.get()}',0,'no')"
    cursor.execute(q)
    connection.commit()
def initiateGUI():
    root.title("Serve Out Smiles")
    root.geometry("400x400")
def shutGUI():
    root.mainloop()