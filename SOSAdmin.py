from tkinter import *
import sqlite3
import UpdateWindow

root2 = Tk()
root2.geometry("300x300")

adminOrg=""

usernameAdmin = Entry(root2)
adminDeets=()
passwordAdmin = Entry(root2,show="*")



##check1 = StringVar()
##check2 = StringVar()
##check3 = StringVar()
##check4 = StringVar()

def updateHours():
    connection = sqlite3.connect('SOS.db')
    cursor = connection.cursor()

    ID1_str= enterID.get()
    ID1 = int(ID1_str)

    selectID = cursor.execute("update sos_hours set hours=hours+1 where id= %d" %ID1)

    labelSuccess = Label(root3, text="Update Successful").grid(row=5, column=0)

def adminLogin():
    connection = sqlite3.connect('SOS.db')
    cursor = connection.cursor()
    f = cursor.execute("select adminID,password,oname from SOS_Admin")
    t = f.fetchall()
    global adminDeets
    adminDeets = (usernameAdmin.get(),passwordAdmin.get())
    global adminOrg
    for i in t:
        if adminDeets == i[0:2]:
            adminOrg = i[2]
    if adminOrg == "":
        Label(root2,text="Incorrect login details.").grid(row=7,column=2)
    else:
        Label(root2,text="Access Granted").grid(row=7,column=2)
        UpdateWindow.newWindow(adminDeets)
        
##def newWindow():
##    #root2.destroy()
##    
##    root3 = Tk()
##    enterID = Entry(root3)
##    
##    connection = sqlite3.connect('SOS.db')
##    cursor = connection.cursor()
##    f = cursor.execute(f"select oname from sos_admin where adminid = '{adminDeets[0]}'")
##    orgName = str(f.fetchone()[0])
##    root3.title(f"Admin {orgName}")
##    root3.geometry("300x300")
##
##    listOfNames= []
##    listOfHours = []
##    listOfCert = []
##    #oname1=f[0]
##
##    fetchNames = cursor.execute("select name from sos_hourlog natural join sos_student where oname= '%s'" %orgName)
##
##    for i in fetchNames:
##        for j in i:
##            listOfNames.append(j)
##            
##    print(listOfNames)
##    
##    listNames = Listbox(root3)
##    listNames.insert(END, *listOfNames)
##
##    fetchHours = cursor.execute("select hours from sos_hourlog natural join sos_student where oname = '%s'" %orgName)
##    for i in fetchHours:
##        for j in i:
##            listOfHours.append(j)
##            
##    listHours = Listbox(root3)
##    listHours.insert(END, *listOfHours)
##    
##    fetchCert = cursor.execute("select dueCert from sos_hourlog natural join sos_student where oname= '%s'" %orgName)
##    for i in fetchCert:
##        for j in i:
##            listOfCert.append(j)
##
##    listCert = Listbox(root3)
##    listCert.insert(END, *listOfCert)
##
##    
##    Label(root3,text="          ").grid(row=0,column=0)
##    
##    IDlabel = Label(root3, text="Enter the ID:  ").grid(row=1, column=0)
##    
##    enterID.grid(row=1, column=1)
##
##    Label(root3,text="          ").grid(row=2,column=0)
##    
##    updateButton = Button(root3, text="Update", command= updateHours)
##    updateButton.grid(row=3, column=0)
##    
##    Label(root3,text="          ").grid(row=4,column=0)
##
##    listNames.grid(row=5, column=0)
##    listHours.grid(row=5, column=1)
##    listCert.grid(row=5, column=2)
##    
def logout():
    Label(root2,text="          ").grid(row=0,column=0)
    Label(root2,text="          ").grid(row=1,column=0)
    Label(root2,text="          ").grid(row=0,column=1)
    Label(root2,text="          ").grid(row=3,column=1)
    Label(root2,text="Enter username : ").grid(row=2,column=1)
    Label(root2,text="Enter password : ").grid(row=4,column=1)
    Label(root2,text="                  ").grid(row=5,column=1)

    usernameAdmin.grid(row=2,column=2)

    passwordAdmin.grid(row=4,column=2)
    
    loginButton = Button(root2,text="Login",comm=adminLogin)
    loginButton.grid(row=6,column=2)
    root2.title("Admin Login Page")
    root2.mainloop()

logout()
