import sqlite3

connection = sqlite3.connect("SOS.db")
cursor = connection.cursor()

print(cursor.execute("select * from sos_hourlog").fetchall())