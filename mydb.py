import mysql.connector

dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Password@SQL25'
)

 #prepare a cursor object

CursorObject=dataBase.cursor()

#create a database
CursorObject.execute("CREATE DATABASE Mydatabase")

print("All Done!")