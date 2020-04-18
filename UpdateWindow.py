from tkinter import *
import sqlite3

##def updateHours():
##    connection = sqlite3.connect('SOS.db')
##    cursor = connection.cursor()
##
##    ID1_str= enterID.get()
##    ID1 = int(ID1_str)
##    print(ID1)
##
##    
##    selectID = cursor.execute("update sos_hours set hours=hours+1 where id= %d" %ID1)
##
##    labelSuccess = Label(root3, text="Update Successful").grid(row=5, column=0)

def newWindow(adminDeets):
    #root2.destroy()
    root3 = Tk()
    adminDetails = adminDeets
    enterID = Entry(root3)
    root3.geometry("300x300")
    def updateHours():
        connection = sqlite3.connect('SOS.db')
        cursor = connection.cursor()

        ID1_str= enterID.get()
        ID1 = int(ID1_str)
        print(ID1)

        
        selectID = cursor.execute("update sos_hourlog set hours=hours+1 where id= %d" %ID1)


        labelSuccess = Label(root3, text="Update Successful").grid(row=2, column=1)
        connection.commit()

    def showAll():
        root4 = Tk()
        root4.title("Showing all details")

        connection = sqlite3.connect('SOS.db')
        cursor = connection.cursor()
        ff = cursor.execute(f"select oname from sos_admin where adminid = '{adminDeets[0]}'")
        orgName = str(ff.fetchone()[0])
        f = cursor.execute(f"select id,name,hours,duecert from sos_hourlog natural join sos_student where oname = '{orgName}'")
        allDetails = f.fetchall()

        listOfIDs = []
        listOfNames = []
        listOfHours = []
        listOfCert = []

        for i in allDetails:
            listOfIDs.append(i[0])
            listOfNames.append(i[1])
            listOfHours.append(i[2])
            listOfCert.append(i[3])

        print(listOfIDs)
        listIDs = Listbox(root4)
        listIDs.insert(END, *listOfIDs)

        listNames = Listbox(root4)
        listNames.insert(END, *listOfNames)

        listHours = Listbox(root4)
        listHours.insert(END, *listOfHours)

        listCert = Listbox(root4)
        listCert.insert(END, *listOfCert)

        listIDs.grid(row=0,column=0)
        listNames.grid(row=0,column=1)
        listHours.grid(row=0, column=2)
        listCert.grid(row=0, column=3)

        root4.mainloop()

    def showElig():
        root4 = Tk()
        root4.title("Showing eligible people")

        connection = sqlite3.connect('SOS.db')
        cursor = connection.cursor()
        ff = cursor.execute(f"select oname from sos_admin where adminid = '{adminDeets[0]}'")
        orgName = str(ff.fetchone()[0])

        f = cursor.execute(f"select id,name from sos_hourlog natural join sos_student where oname = '{orgName}' and hours>9")
        eligDetails = f.fetchall()

        listOfIDs = [i for i, j in eligDetails]
        listOfNames = [j for i, j in eligDetails]

        listIDs = Listbox(root4)
        listIDs.insert(END, *listOfIDs)

        listNames = Listbox(root4)
        listNames.insert(END, *listOfNames)

        listIDs.grid(row=1, column=0)
        listNames.grid(row=1, column=1)
        root4.mainloop()

    def UpdateElig():
        connection = sqlite3.connect('SOS.db')
        cursor = connection.cursor()

        cursor.execute("update sos_hourlog set dueCert='yes' where hours>9")
        connection.commit()

        Label(root3, text="Database updated.").grid(row=2, column=0)
    def updateCert():
        connection = sqlite3.connect('SOS.db')
        cursor = connection.cursor()

        cursor.execute("update sos_hourlog set dueCert='given' where id = %d" %int(enterID.get()))
        connection.commit()
    def deletion():
        delID_str = enterID.get()
        delID = int(delID_str)
        connection = sqlite3.connect('SOS.db')
        cursor = connection.cursor()
        try:
            cursor.execute("delete from sos_hourlog where id = %d" % delID)
            cursor.execute("delete from sos_student where id = %d" % delID)
            Label(root3, text="Record deleted.").grid(row=2, column=0)
        except:
            Label(root3, text="Record could not be deleted.").grid(row=2, column=1)

        connection.commit()


    connection = sqlite3.connect('SOS.db')
    cursor = connection.cursor()
    f = cursor.execute(f"select oname from sos_admin where adminid = '{adminDeets[0]}'")
    orgName = str(f.fetchone()[0])
    root3.title(f"Admin {orgName}")
    root3.geometry("300x300")
    listOfNames= []
    listOfHours = []
    listOfCert = []

    fetchNames = cursor.execute("select name from sos_hourlog natural join sos_student where oname= '%s'" %orgName)

    for i in fetchNames:
        for j in i:
            listOfNames.append(j)

    print(listOfNames)

    listNames = Listbox(root3)
    listNames.insert(END, *listOfNames)

    """fetchHours = cursor.execute("select hours from sos_hourlog natural join sos_student where oname = '%s'" %orgName)
    for i in fetchHours:
        for j in i:
            listOfHours.append(j)
            
    listHours = Listbox(root3)
    listHours.insert(END, *listOfHours)
    """
    fetchID = cursor.execute("select id from sos_hourlog natural join sos_student where oname= '%s'" %orgName)
    for i in fetchID:
        for j in i:
            listOfCert.append(j)

    listCert = Listbox(root3)
    listCert.insert(END, *listOfCert)

    #BUTTONS
    showAllbutton = Button(root3, text="Show All", command= showAll)

    showEligbutton = Button(root3, text="Show Eligible", command=showElig)

    updateEligbutton = Button(root3, text="Update Eligible", command=UpdateElig )
    
    #GRID
    Label(root3,text="          ").grid(row=0,column=0)
    
    IDlabel = Label(root3, text="Enter the ID:  ").grid(row=1, column=0)
    
    enterID.grid(row=1, column=1)

    Label(root3,text="          ").grid(row=2,column=0)
    
    updateButton = Button(root3, text="Update", command= updateHours)
    updateButton.grid(row=3, column=1)
    
    Label(root3,text="          ").grid(row=4,column=0)

    showAllbutton.grid(row=5, column=1)
    
    Label(root3,text="          ").grid(row=6,column=0)
    
    showEligbutton.grid(row=7, column=1)
    
    Label(root3,text="          ").grid(row=8,column=0)
    
    updateEligbutton.grid(row=9, column=1)
    #listNames.grid(row=5, column=0)
    #listHours.grid(row=5, column=1)
    #listCert.grid(row=5, column=2)
    Label(root3, text="          ").grid(row=10, column=0)
    Button(root3,text = "Delete Record",command=deletion).grid(row=11,column = 1)

    Label(root3, text="          ").grid(row=12, column=0)
    Button(root3, text="Update certificate", command=updateCert).grid(row=13, column=1)


    root3.mainloop()
    
