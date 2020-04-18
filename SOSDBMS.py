import GUI
import sqlite3
import pandas as pd
import matplotlib
import matplotlib.pyplot as plot

def create_table():
    connection = sqlite3.connect('SOS.db')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS SOS_STUDENT(id number(11) primary key,name varchar(20),course varchar(10),stream varchar(20),contact number(10))")
    cursor.execute("CREATE TABLE IF NOT EXISTS SOS_ORG(oname varchar(10),location varchar(20),type varchar(10))")
    cursor.execute("CREATE TABLE IF NOT EXISTS SOS_HourLog(id number(11),oname varchar(10),hours number(2),dueCert varchar(3),foreign key (id) references sos_student(id),foreign key (oname) references sos_org(oname))")
    cursor.execute("CREATE TABLE IF NOT EXISTS SOS_ADMIN(ADMINID VARCAR(10),ONAME VARCHAR(10),PASSWORD VARCHAR(10),foreign key (oname) references sos_org(oname))")
    """cursor.execute("insert into SOS_admin values('adminpcc1','Petsville','2000')")
    cursor.execute("insert into SOS_admin values('adminpcc2','Paws N Claws','2000')")
    cursor.execute("insert into SOS_admin values('adminpcc3','Pawcity','2000')")
    cursor.execute("insert into SOS_admin values('adminoah1','Cheshire Homes','2000')")
    cursor.execute("insert into SOS_admin values('adminoah2','Royal Seniors Home','2000')")
    cursor.execute("insert into SOS_admin values('adminoah3','Ashray Foundation','2000')")
    cursor.execute("insert into SOS_admin values('admint1','Furlora','2000')")
    cursor.execute("insert into SOS_admin values('admint2','VYF','2000')")
    cursor.execute("insert into SOS_admin values('admint3','Spark A Change','2000')")
    cursor.execute("insert into SOS_ORG values ('Furlora','Versova','Teaching')")
    cursor.execute("insert into SOS_org values('VYF','Juhu','Teaching')")
    cursor.execute("insert into sos_org values('Spark A Change','Irla','Teaching')")
    cursor.execute("insert into sos_org values('Cheshire Homes','Andheri East','Old Age Home')")
    cursor.execute("insert into SOS_Org values('Royal Seniors Home','Palghar','Old Age Home')")
    cursor.execute("insert into SOS_Org values('Ashray Foundation','Mumbai Central','Old Age Home')")
    cursor.execute("insert into SOS_Org values('Petsville','Oshiwara','Pet Care Centre')")
    cursor.execute("insert into SOS_Org values('Paws N Claws','Ghatkopar West','Pet Care Centre')")
    cursor.execute("insert into SOS_Org values('Pawcity','Santacruz East','Pet Care Centre')")"""
    connection.commit()
create_table()
GUI.createGUI()
connection = sqlite3.connect('SOS.db')
cursor = connection.cursor()
print()
print()
#f = cursor.execute("select * from sos_student")
#f = cursor.execute("select name from sos_student")
#print(f.fetchall())
print("Student details : ")
print("SAPID\t\tName\t\tCourse\tStream\t\tContact\t\t")
f = cursor.execute("select * from sos_student")
for i in f.fetchall():
    print(f"{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}")
f = cursor.execute("select * from sos_hourlog")
print(f.fetchall())
f = cursor.execute("select count(id),type from sos_hourlog natural join sos_org group by type")
dictData = {}
for i in f.fetchall():
    dictData.update({i[1]:int(i[0])})
df = pd.DataFrame({'Type of Organisation':list(dictData.keys()),'No. of applicants':list(dictData.values())})
ax = df.plot.bar(x='Type of Organisation',y='No. of applicants',rot=0)
plot.show(block = True)